from flask import Flask, render_template, request, flash, redirect, url_for, make_response, session, Blueprint
from models.Formulario import Formulario
from utils import db

formulario_bp = Blueprint('formulario', __name__, template_folder='templates')


@formulario_bp.route('/')
def criar_formulario():
    tempo_total = request.form['tempo_total']
    id_user = request.form['id_user']

    formulario = Formulario(id_user, tempo_total)

    db.session.add(formulario)
    db.session.commit()

    return render_template()


@formulario_bp.route('/atualizarformulario/<int:id_formulario>')
def atualizar_formulario(id_formulario):
    formulario = Formulario.query(id_formulario)

    formulario.tempo_total = request.form['tempo_total']

    db.session.add(formulario)
    db.session.commit()

    return redirect('/')


@formulario_bp.route('/recuperarformulario/<int:id_formulario>')
def recuperar_formulario(id_formulario):
    formulario = Formulario.query(id_formulario)
    db.session.commit()

    return redirect()


@formulario_bp.route('/deletarformulario<int:id_formulario>')
def deletar_formulario(id_formulario):
    db.session.delete(Formulario).filter(id_formulario=id_formulario)
    db.session.commit()

    return redirect()