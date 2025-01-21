from flask import Flask, render_template, request, flash, redirect, make_response, session
import json
import os
from flask_migrate import Migrate
from utils import db

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
db_usuario = os.getenv('danilo')
db_senha = os.getenv('danilo$pass')
db_host = os.getenv('psi2024.mysql.database.azure.com')
db_mydb = os.getenv('psi2024_danilo')

conexao = f"mysql+pymysql://{db_usuario}:{db_senha}@{db_host}/{db_mydb}"
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)