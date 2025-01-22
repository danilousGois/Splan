from flask import Flask, render_template, request, flash, redirect, make_response, session
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, declarative_base
import json
import os
from flask_migrate import Migrate
from utils import db
import uuid
from controllers.Usuario import user_bp
from controllers.Materia import materia_bp
from controllers.Assunto import assunto_bp
from controllers.Conteudo import conteudo_bp
from controllers.Formulario import formulario_bp
from controllers.Progresso import progresso_bp
from controllers.Materia_peso import peso_bp

app = Flask(__name__)

app.register_blueprint(user_bp, url_prefix='/usuario')
app.register_blueprint(materia_bp, url_prefix='/materia')
app.register_blueprint(assunto_bp, url_prefix='/assunto')
app.register_blueprint(conteudo_bp, url_prefix='/conteudo')
app.register_blueprint(formulario_bp, url_prefix='/formulario')
app.register_blueprint(progresso_bp, url_prefix='/progresso')
app.register_blueprint(peso_bp, url_prefix='/peso')

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

db_usuario = os.getenv('DB_USERNAME')
db_senha = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST')
db_mydb = os.getenv('DB_DATABASE')

conexao = f"mysql+pymysql://{db_usuario}:{db_senha}@{db_host}/{db_mydb}"
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)


@app.route('/')
def index():
    return render_template('home.html')


# def carregar_materias():
#    if os.path.exists('static/materias.json'):
#       with open('static/materias.json', 'r') as json_file:
#          materias = json.load(json_file)
#       return materias
#    return {}

# def verificar_user_logado():
#    ID_Usuario = request.cookies.get('ID_Usuario')
#    if ID_Usuario == None:
#       return False
#    if os.path.exists('static/dados_usuario.json'):
#       with open('static/dados_usuario.json', 'r') as json_file:
#          lista_usuarios = json.load(json_file)
#          for lista_dict in lista_usuarios:
#             if lista_dict.get('ID_Usuario') == ID_Usuario:
#                return True
#    return False

# @app.route('/')
# def index():
#    if verificar_user_logado() == True:
#       return redirect('/inicio')
#    return render_template('home.html')

# @app.route('/inicio')
# def carregarLandingPage():
#    if 'ID_Usuario' not in session:
#       return redirect('/autenticar')
#    nomeuser = session['nomeuser']
#    return render_template('base_landingpage.html', nome = nomeuser)



# @app.route('/<valor>')
# def paginainicial(valor):
#    if verificar_user_logado() == True:
#       return redirect('/inicio')
#    elif valor == 'autenticar':
#       return render_template('login.html')
#    else:
#       return render_template('signup.html')

# @app.route('/formulario')
# def formulario():
#    return render_template('formulario.html')


# @app.route('/cadastrar', methods=['POST'])
# def validarsignup():
#    nomeuser = request.form['nome']
#    emailUser = request.form['email']
#    senhaUser = request.form['senha']
#    confirmarsenha = request.form['confirmarsenha']
#    ID_Usuario = str(uuid.uuid4())

#    if emailUser and senhaUser and confirmarsenha:
#       if senhaUser == confirmarsenha:
#          if os.path.exists('static/dados_usuario.json'):
#             with open('static/dados_usuario.json', 'r') as json_file:
#                lista_usuarios = json.load(json_file)
#             for lista_dict in lista_usuarios:
#                if emailUser == lista_dict['email']:
#                   flash('E-mail já cadastrado, faça login!', "primary")
#                   return redirect('/autenticar')
#          else:
#             lista_usuarios = []

#          dados_user = {
#             "ID_Usuario": ID_Usuario,
#             "nomeuser": nomeuser,
#             "email": emailUser,
#             "senha": senhaUser
#          }

#          lista_usuarios.append(dados_user)
#          with open('static/dados_usuario.json', 'w') as json_file:
#             json.dump(lista_usuarios, json_file, indent=4)

#          session['ID_Usuario'] = ID_Usuario
#          session['nomeuser'] = nomeuser
#          session['email'] = emailUser     

#          return redirect('/inicio')
      
#       else:
#          flash('Senha e confirmação devem ser iguais!', "warning")
#          return redirect('/cadastrar')
#    else:
#       flash('Todos os campos devem ser preenchidos!', "warning")
#       return redirect('/cadastrar')


# @app.route('/autenticar', methods=['POST'])
# def verificarlogin():
#    email = request.form['email']
#    senha = request.form['senha']
#    Ver_email = False
#    Ver_senha = False
#    with open('static/dados_usuario.json', 'r') as json_file:
#       lista_usuarios = json.load(json_file)

#    if email and senha:
#       for lista_dict in lista_usuarios:
#          if email == lista_dict['email'] and senha == lista_dict['senha']:
#             Ver_email = True
#             Ver_senha = True
#             session['ID_Usuario'] = lista_dict['ID_Usuario']
#             session['nomeuser'] = lista_dict['nomeuser']
#             session['email'] = lista_dict['email']
#             return redirect('/inicio')

#       if not (Ver_email and Ver_senha):
#          flash('Esse usuário não existe! Faça o cadastro!')
#          return redirect('/cadastrar')
#    else:
#       flash('Todos os campos devem ser preenchidos!')
#       return redirect('/autenticar')


# @app.route('/inicio/<materia>')
# def carregarmateria(materia):
#    nomeuser = session['nomeuser']
#    materias = carregar_materias()
#    if materia in materias:
#       return render_template('carregarmaterias.html', materia=materias[materia], nome = nomeuser)
#    else:
#       return "Matéria não encontrada", 404

# @app.route('/cronograma')
# def cronograma():
#    if verificar_user_logado() == True:
#       return redirect('/inicio')
#    return render_template('cronograma.html')


# @app.route('/logout')
# def logout():
#    session.clear()
#    resp = make_response(redirect('/autenticar'))
#    return resp


# if __name__ == "__main__":
#    app.run(debug=True)