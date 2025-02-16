from flask import Flask, render_template, request, flash, redirect, url_for, make_response, session, Blueprint
from models.Formulario import Formulario
from models.Materia import Materia
from models.Materia_peso import Materia_peso
from utils import db, login_manager
from flask_login import current_user
from flask_login import login_user, logout_user, login_required

formulario_bp = Blueprint('formulario', __name__, template_folder='templates')


@formulario_bp.route('/responder')
def carregar_formulario():
   return render_template('formulario.html')


@formulario_bp.route('/receberformulario', methods=['POST'])
def processar_formulario():
   if request.method == "GET":
      return render_template('formulario.html')
    
#cadastrar formulario
   horas_estudo = request.form['horas_estudo']
   form = Formulario(current_user.id, horas_estudo)
   print(current_user.id, horas_estudo)
   db.session.add(form)
   db.session.commit()

   id_form = form.id_formulario

#cadastrar pesos e materias
   materias_selecionadas = request.form.getlist("materias[]")
   
   dificuldades = {}
   if "portugues" in materias_selecionadas:
      dificuldade_portugues = request.form.get("dificuldade_portugues")
      dificuldades["portugues"] = dificuldade_portugues
      pegar_materia = Materia.query.filter_by(nome='portugues').first()
      id_mat = pegar_materia.id_materia
      print(dificuldade_portugues, id_form, id_mat)
      instancia = Materia_peso(dificuldade_portugues, id_form, id_mat)
      db.session.add(instancia)
      db.session.commit()

   if "matematica" in materias_selecionadas:
      dificuldade_matematica = request.form.get("dificuldade_matematica")
      dificuldades["matematica"] = dificuldade_matematica
      pegar_materia = Materia.query.filter_by(nome='matematica').first()
      id_mat = pegar_materia.id_materia
      print(dificuldade_matematica, id_form, id_mat)
      instancia = Materia_peso(dificuldade_matematica, id_form, id_mat)
      db.session.add(instancia)
      db.session.commit()

   if "historia" in materias_selecionadas:
      dificuldade_historia = request.form.get("dificuldade_historia")
      dificuldades["historia"] = dificuldade_historia
      pegar_materia = Materia.query.filter_by(nome='historia').first()
      id_mat = pegar_materia.id_materia
      print(dificuldade_historia, id_form, id_mat)
      instancia = Materia_peso(dificuldade_historia, id_form, id_mat)
      db.session.add(instancia)
      db.session.commit()

   if "biologia" in materias_selecionadas:
      dificuldade_biologia = request.form.get("dificuldade_biologia")
      dificuldades["biologia"] = dificuldade_biologia
      pegar_materia = Materia.query.filter_by(nome='biologia').first()
      id_mat = pegar_materia.id_materia
      print(dificuldade_biologia, id_form, id_mat)
      instancia = Materia_peso(dificuldade_biologia, id_form, id_mat)
      db.session.add(instancia)
      db.session.commit()

   if "quimica" in materias_selecionadas:
      dificuldade_quimica = request.form.get("dificuldade_quimica")
      dificuldades["quimica"] = dificuldade_quimica
      pegar_materia = Materia.query.filter_by(nome='quimica').first()
      id_mat = pegar_materia.id_materia
      print(dificuldade_quimica, id_form, id_mat)
      instancia = Materia_peso(dificuldade_quimica, id_form, id_mat)
      db.session.add(instancia)
      db.session.commit()

   if "geografia" in materias_selecionadas:
      dificuldade_geografia = request.form.get("dificuldade_geografia")
      dificuldades["geografia"] = dificuldade_geografia
      pegar_materia = Materia.query.filter_by(nome='quimica').first()
      id_mat = pegar_materia.id_materia
      print(dificuldade_quimica, id_form, id_mat)
      instancia = Materia_peso(dificuldade_geografia, id_form, id_mat)
      db.session.add(instancia)
      db.session.commit()

   if "filosofia" in materias_selecionadas:
      dificuldade_filosofia = request.form.get("dificuldade_filosofia")
      dificuldades["filosofia"] = dificuldade_filosofia
      pegar_materia = Materia.query.filter_by(nome='filosofia').first()
      id_mat = pegar_materia.id_materia
      print(dificuldade_filosofia, id_form, id_mat)
      instancia = Materia_peso(dificuldade_filosofia, id_form, id_mat)
      db.session.add(instancia)
      db.session.commit()

   if "sociologia" in materias_selecionadas:
      dificuldade_sociologia = request.form.get("dificuldade_sociologia")
      dificuldades["sociologia"] = dificuldade_sociologia
      pegar_materia = Materia.query.filter_by(nome='sociologia').first()
      id_mat = pegar_materia.id_materia
      print(dificuldade_sociologia, id_form, id_mat)
      instancia = Materia_peso(dificuldade_sociologia, id_form, id_mat)
      db.session.add(instancia)
      db.session.commit()

   if "ingles" in materias_selecionadas:
      dificuldade_ingles = request.form.get("dificuldade_ingles")
      dificuldades["ingles"] = dificuldade_ingles
      pegar_materia = Materia.query.filter_by(nome='ingles').first()
      id_mat = pegar_materia.id_materia
      print(dificuldade_ingles, id_form, id_mat)
      instancia = Materia_peso(dificuldade_ingles, id_form, id_mat)
      db.session.add(instancia)
      db.session.commit()

   if "artes" in materias_selecionadas:
      dificuldade_artes = request.form.get("dificuldade_artes")
      dificuldades["artes"] = dificuldade_artes
      pegar_materia = Materia.query.filter_by(nome='artes').first()
      id_mat = pegar_materia.id_materia
      print(dificuldade_artes, id_form, id_mat)
      instancia = Materia_peso(dificuldade_artes, id_form, id_mat)
      db.session.add(instancia)
      db.session.commit()

   if "fisica" in materias_selecionadas:
      dificuldade_fisica = request.form.get("dificuldade_fisica")
      dificuldades["fisica"] = dificuldade_fisica
      pegar_materia = Materia.query.filter_by(nome='fisica').first()
      id_mat = pegar_materia.id_materia
      print(dificuldade_fisica, id_form, id_mat)
      instancia = Materia_peso(dificuldade_fisica, id_form, id_mat)
      db.session.add(instancia)
      db.session.commit()

   if "literatura" in materias_selecionadas:
      dificuldade_literatura = request.form.get("dificuldade_literatura")
      dificuldades["literatura"] = dificuldade_literatura
      pegar_materia = Materia.query.filter_by(nome='literatura').first()
      id_mat = pegar_materia.id_materia
      print(dificuldade_literatura, id_form, id_mat)
      instancia = Materia_peso(dificuldade_literatura, id_form, id_mat)
      db.session.add(instancia)
      db.session.commit()


   # resultado = "Matérias selecionadas e suas dificuldades:<br>"
   # for materia, dificuldade in dificuldades.items():
   #    resultado += f"{materia}: Dificuldade {dificuldade}<br>"
   # print(resultado)
   # print(horas_estudo)

   return redirect(url_for('inicio'))