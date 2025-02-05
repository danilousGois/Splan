from flask import Flask, render_template, request, flash, redirect, url_for, make_response, session, Blueprint
from models.Usuario import Usuario
from utils import db, login_manager
import hashlib
from flask_login import current_user
from flask_login import login_user, logout_user, login_required

user_bp = Blueprint('usuario', __name__, template_folder='templates')


@login_manager.user_loader
def load_user(user_id):
    print(f"🔍 Tentando carregar usuário com ID: {user_id}")
    if not user_id:
        return None  
    return Usuario.query.get(user_id)



@user_bp.route('/cadastro', methods=['POST', 'GET'])
def criar_usuario():
    if request.method == 'GET':
        return render_template('signup.html')

    nome = request.form['nome']
    email = request.form['email']
    telefone = request.form['telefone']
    senha = request.form['senha']
    confirmarsenha = request.form['confirmarsenha']
    tipo_user = request.form['tipo_user']

    user_existente = Usuario.query.filter_by(email=email).first()
    if user_existente:
        flash('Email já cadastrado. Faça login!', 'warning')
        return render_template('login.html')
    elif senha != confirmarsenha:
        flash('Senha e confirmação de senha precisam ser iguais!', 'warning')
        return render_template('signup.html')
    
    hash_senha = hashlib.sha256(senha.encode()).hexdigest()
    user = Usuario(nome, telefone, email, hash_senha, tipo_user)

    db.session.add(user)
    db.session.commit()

    login_user(user)
    return redirect(url_for('formulario.carregar_formulario'))




@user_bp.route('/login', methods=['POST', 'GET'])
def login_usuario():
    if request.method == 'GET':
        if current_user.is_authenticated:
            return redirect(url_for('inicio'))
        return render_template('login.html')
    
    email = request.form['email']
    senha = request.form['senha']

    user = Usuario.query.filter_by(email=email).first()

    if user:
        hash_senha = hashlib.sha256(senha.encode()).hexdigest()
        if user.senha == hash_senha:
            login_user(user)
            print(f'Usuário logado: {user.id}')
            return redirect(url_for('inicio'))
        else:
            flash('Senha incorreta!', 'warning')
            return render_template('login.html')
    else:
        flash('There is no user bounded with this email', 'warning')
        return render_template('login.html')
    


#falta fazer verificação de senha e confirmação(botar flash card no html), se os valores nao sao iguais... 
@user_bp.route('/alterarperfil', methods=['POST'])
@login_required
def update_user():
    if request.method == 'GET':
        return render_template('perfil_user.html')
    user = Usuario.query.filter_by(nome=current_user.nome).first()
    user.nome = request.form['nome']
    user.email = request.form['email']
    user.telefone = request.form['telefone']
    senha = request.form['novasenha']
    confirmarsenha = request.form['confirmacaonovasenha']

    if senha != confirmarsenha:
        flash('Nova senha e confirmação não são iguais!')
        return redirect(url_for('usuario.update_user'))

    user.senha = hashlib.sha256(senha.encode()).hexdigest()
    login_user(user)

    db.session.add(user)
    db.session.commit()
    
    return redirect(url_for('inicio'))

@user_bp.route('/cronograma')
# @login_required
def show_cronograma():
    return render_template('cronograma.html', nome=session['user'])

@user_bp.route('/deletarperfil')
@login_required
def deletar_user():
    if not current_user.is_authenticated:
        return redirect(url_for("login")) 
    user = current_user
    logout_user()
    db.session.delete(user)
    db.session.commit()
    session.pop('user', None)
    return redirect(url_for('index'))


@user_bp.route('/logoff')
@login_required
def logoff():
    if not current_user.is_authenticated:
        return redirect(url_for("login")) 
    logout_user() 
    session.clear()
    return redirect(url_for('index'))


@user_bp.route('/perfil')
@login_required
def carregar_perfil():
    print(current_user)
    user = current_user
    return render_template('perfil_user.html', user=user)