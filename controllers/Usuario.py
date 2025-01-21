from flask import Flask, render_template, request, flash, redirect, url_for, make_response, session, Blueprint
from models.Usuario import Usuario
from utils import db

user_bp = Blueprint('usuario', __name__, template_folder='templates')


#fazer as verificações necesárias


@user_bp.route('/', methods=['POST', 'GET'])
def criar_usuario():

    nome = request.form['nome']
    email = request.form['email']
    telefone = request.form['telefone']
    senha = request.form['senha']


    user = Usuario(nome, telefone, email, senha)
    db.session.add(user)
    db.session.commit()

    #usar sessão de usuario para guardar o user logado e fazer o crud

    return render_template('signup.html')


@user_bp.route('/perfil/<int: id_user>')
def recuperar_user(id_user):
    db.session.query(Usuario).filter(id_usuario=id_user)
    db.session.commit()    

    return render_template('perfil_user.html') # nome de arquivo inventado



@user_bp.route('/perfil/<int: id_user>')
def deletar_usuario(id_user):
    db.session.delete(Usuario).filter(id_usuario=id_user)
    db.session.commit()    

    return render_template('perfil_user.html') # nome de arquivo inventado



@user_bp.route('/perfil/<int: id_user>', methods=['POST', 'GET'])
def alterar_usuario(id_user):

    user = db.session.query(Usuario).filter(id_usuario=id_user)

    user.nome = request.form['nome']
    user.email = request.form['email']
    user.telefone = request.form['telefone']
    user.senha = request.form['senha']

    db.session.add(user)
    db.session.commit()

    return redirect(url_for('.perfil', id_user=id_user))