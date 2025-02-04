from flask import Flask, render_template, request, flash, redirect, url_for, make_response, session, Blueprint
from models.Formulario import Formulario
from utils import db

formulario_bp = Blueprint('formulario', __name__, template_folder='templates')


@formulario_bp.route('/responder')
def carregar_formulario():
   return render_template('formulario.html')


@formulario_bp.route('/receberformulario')
def receber_formulario():
   return 'forms recebido'