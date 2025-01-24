from flask import Flask, render_template, request, flash, redirect, url_for, make_response, session, Blueprint
from models.Usuario import Usuario
from utils import db

user_bp = Blueprint('usuario', __name__, template_folder='templates')

 
@user_bp.route('/cadastro', methods=['POST', 'GET'])
def criar_usuario():
    if request.method == 'GET':
        return render_template('signup.html')

    nome = request.form['nome']
    email = request.form['email']
    telefone = request.form['telefone']
    senha = request.form['senha']
    confirmarsenha = request.form['confirmarsenha']
    tipo_user = 0

    user_existente = Usuario.query.filter_by(email=email).first()
    if user_existente:
        flash('Email já cadastrado!', 'warning')
        return render_template('signup.html')
    elif senha != confirmarsenha:
        flash('Senha e confirmação de senha precisam ser iguais!', 'warning')
        return render_template('signup.html')

    user = Usuario(nome, telefone, email, senha, tipo_user)

    db.session.add(user)
    db.session.commit()

    return 'logado'





#usar sessão de usuario para guardar o user logado e fazer o crud

@user_bp.route('/login', methods=['POST', 'GET'])
def login_usuario():
    if request.method == 'GET':
        return render_template('login.html')
    
    email = request.form['email']
    senha = request.form['senha']

    user = Usuario.query.filter_by(email=email).first()

    if user:
        if user.senha == senha:
            return 'ĺogado'
        else:
            flash('Senha incorreta!', 'warning')
            return render_template('login.html')
    else:
        flash('There is no user bounded with this email', 'warning')
        return render_template('login.html')


