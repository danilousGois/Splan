from flask import Flask, render_template, request, flash, redirect, url_for, make_response, session, Blueprint
from models.Materia import Materia
from utils import db

materia_bp = Blueprint('materia', __name__, template_folder='templates')

def listar_materias():
    lista_materias = Materia.query.all()
    

def criar_materia(nome):
    materia = Materia(nome)

    db.session.add(materia)
    db.session.commit()


@materia_bp.route('/inserir_materias')
def inserir_materia():
    lista_materias = ['matemática', 'português', 'história', 'geografia', 'física', 'química', 'filosofia', 'sociologia', 'artes', 'biologia', 'inglês', 'literatura']

    # for materia in lista_materias:
    #     criar_materia(materia)
        
    return 'hello'

@materia_bp.route('/mostrar_materias')
def recuperar_materias():
    
    # db.session.query(Materia).delete()
    # db.session.commit()

    return 'excluded'
        
    
@materia_bp.route('/carregar_materias')
def index_materias():
    return render_template('create_materias.html')