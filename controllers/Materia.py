from flask import Flask, render_template, request, flash, redirect, url_for, make_response, session, Blueprint
from models.Materia import Materia
from utils import db

materia_bp = Blueprint('materia', __name__, template_folder='templates')

# @materia_bp.route('/criarmateria', methods=['GET', 'POST'])
# def criar_materia():

@materia_bp.route('/recuperarmateria/<str: nome_materia>')
def recuperar_materia(nome_materia):
     pass