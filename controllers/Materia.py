from flask import Flask, render_template, request, flash, redirect, url_for, make_response, session, Blueprint
from models.Materia import Materia
from utils import db

materia_bp = Blueprint('materia', __name__, template_folder='templates')

# @materia_bp.route('/criarmateria', methods=['GET', 'POST'])
# def criar_materia():

@materia_bp.route('/recuperarmateria/<int:id_materia>')
def recuperar_materia(id_materia):
     materia = Materia.query(id_materia)
     db.session.commit()


@materia_bp.route('/materias')
def carregar_materias():
     materias = Materia.query.all()
     db.session.commit()

     return materias

@materia_bp.route('/deletarmateria/<int:id_materia>')
def deletar_materia(id_materia):
     db.session.delete(Materia).filter(id_materia=id_materia)
     db.session.commit()