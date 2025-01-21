#Criar cronograma
#pegar horas totais de estudo do user
#somar os pesos das materias
#dividir o tempo total pela soma dos pesos
#distribuir essa unidade de tempo para cada materia(multiplicar essa unidade de tempo pelo peso da materia para obter o tempo total)
#

from flask import Flask
from controllers.Usuario import user_bp
from utils import db
from flask_migrate import Migrate

app = Flask(__name__)
app.secret_key = 'secret_key_splan'

app.register_blueprint(user_bp, url_prefix='/usuario')