from flask import Flask, render_template, request, flash, redirect, url_for, make_response, session, Blueprint
from models.Materia import Materia
from utils import db
from models.Assunto import Assunto

materia_bp = Blueprint('materia', __name__, template_folder='templates')

@materia_bp.route('/<materia>')
def listar_assuntos(materia):
    # materia_objeto = Materia.query.filter_by(nome=materia).first()
    # lista_assuntos = Assunto.query.filter_by(id_materia=materia_objeto.id_materia).all()
    # return lista_assuntos
    return f'Olá, voce acaba de acessar a matéria de {materia}'
