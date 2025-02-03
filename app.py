from flask import Flask, render_template, request, flash, redirect, make_response, session
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, declarative_base
import json
import os
from flask_migrate import Migrate
from utils import db, login_manager
import uuid
from controllers.Usuario import user_bp
from controllers.Materia import materia_bp
from controllers.Assunto import assunto_bp
from controllers.Conteudo import conteudo_bp
from controllers.Formulario import formulario_bp
from controllers.Progresso import progresso_bp
from controllers.Materia_peso import peso_bp
from controllers.Materia import inserir_materia
app = Flask(__name__)

app.register_blueprint(user_bp, url_prefix='/usuario')
app.register_blueprint(materia_bp, url_prefix='/materia')
app.register_blueprint(assunto_bp, url_prefix='/assunto')
app.register_blueprint(conteudo_bp, url_prefix='/conteudo')
app.register_blueprint(formulario_bp, url_prefix='/formulario')
app.register_blueprint(progresso_bp, url_prefix='/progresso')
app.register_blueprint(peso_bp, url_prefix='/peso')

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# db_usuario = os.getenv('DB_USERNAME')
# db_senha = os.getenv('DB_PASSWORD')
# db_host = os.getenv('DB_HOST')
# db_mydb = os.getenv('DB_DATABASE')
# conexao = f"mysql+pymysql://{db_usuario}:{db_senha}@{db_host}/{db_mydb}"
conexao = "sqlite:///banco_splan.sqlite"
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)
login_manager.init_app(app)


@app.route('/')
def index():
   return render_template('home.html')



@app.route('/formulario')
def formulario():
   return render_template('formulario.html')



if __name__ == "__main__":
    app.run(debug=True)

