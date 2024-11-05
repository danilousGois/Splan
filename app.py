from flask import Flask, render_template, request
from flask import flash, redirect, make_response
import json
import os
import uuid

app = Flask(__name__)
app.config['SECRET_KEY'] = 'chave secreta projeto PSI'

def verificar_user_logado():
   ID_Usuario = request.cookies.get('ID_Usuario')

   if ID_Usuario == None:
      return False
   if os.path.exists('static/dados_usuario.json'):
      with open('static/dados_usuario.json', 'r') as json_file:
         lista_usuarios = json.load(json_file)
         for lista_dict in lista_usuarios:
               if lista_dict.get('ID_Usuario') == ID_Usuario:
                  return True
   return False

@app.route('/')
def index():
   if verificar_user_logado() == True:
      return redirect('/inicio')
   return render_template('home.html')

@app.route('/inicio')
def carregarLandingPage():
   if verificar_user_logado() == False:
      return redirect('/autenticar')
   return render_template('base_landingpage.html')


@app.route('/<valor>')
def paginainicial(valor):
   if verificar_user_logado() == True:
      return redirect('/inicio')
   elif valor == 'autenticar':
      return render_template('login.html')
   else:
      return render_template('signup.html')


@app.route('/cadastrar', methods=['POST'])
def validarsignup():
   emailUser = request.form['email']
   senhaUser = request.form['senha']
   confirmarsenha = request.form['confirmarsenha']
   ID_Usuario = str(uuid.uuid4())

   if emailUser and senhaUser and confirmarsenha:
      if senhaUser == confirmarsenha:
         if os.path.exists('static/dados_usuario.json'):
            with open('static/dados_usuario.json', 'r') as json_file:
               lista_usuarios = json.load(json_file)
               
            for lista_dict in lista_usuarios:
               for chave, valor in lista_dict.items():
                  if emailUser in valor:
                     flash('E-mail já cadastrado, faça login!!', "primary")
                     return redirect('/autenticar')
         else:
            lista_usuarios = []  

         dados_user = {
            "ID_Usuario": ID_Usuario,
            "email": emailUser,
            "senha": senhaUser
         }
         
         lista_usuarios.append(dados_user)
         with open('static/dados_usuario.json', 'w') as json_file:
            json.dump(lista_usuarios, json_file, indent=4)

         resp = make_response(redirect('/inicio'))
         resp.set_cookie('ID_Usuario', ID_Usuario)
         return resp
      else:
         flash('Senha e confirmação devem ser iguais!', "warning")
         return redirect('/cadastrar')
   else:
      flash('Todos os campos devem ser preenchidos!', "warning")
      return redirect('/cadastrar')


@app.route('/autenticar', methods=['POST'])
def verificarlogin():
   email = request.form['email']
   senha = request.form['senha']
   Ver_email = False
   Ver_senha = False
   with open('static/dados_usuario.json', 'r') as json_file:
      lista_usuarios = json.load(json_file)

   if email and senha:
      for lista_dict in lista_usuarios:
         for chave, valor in lista_dict.items():
            if email in valor:
               Ver_email = True
            if senha in valor:
               Ver_senha = True
      if Ver_email == True and Ver_senha == True:
         ID_Usuario = str(uuid.uuid4())

         resp = make_response(redirect('/inicio'))
         resp.set_cookie('ID_Usuario', ID_Usuario)

         with open('static/dados_usuario.json', 'r') as json_file:
               lista_usuarios = json.load(json_file)

         for lista_dict in lista_usuarios:
            if lista_dict.get('email') == email:
               lista_dict['ID_Usuario'] = ID_Usuario

               with open('static/dados_usuario.json', 'w') as json_file:
                  json.dump(lista_usuarios, json_file, indent=4)
                  
               return resp
      else:
         flash('Esse usuário não existe! Faça o cadastro!', "danger")
      return redirect('/cadastrar')
   else:
      flash('Todos os campos devem ser preenchidos!', "warning")
   return redirect('/autenticar')

@app.route('/inicio/<materia>')
def carregarmateria(materia):

   materias = {
      'Matemática': {
         'nome': 'matemática',
         'conteudos': ['análise combinatória', 'funções', 'trigonometria', 'geometria', 'algebra', 'logaritmo', 'operações', 'sistemas lineares']
      }, 
      'Física': {
         'nome': 'física',
         'conteudos': ['dinâmica', 'eletrodinâmica', 'eletromagneteismo', 'óptica', 'calorimetria', 'ondulatória', 'vetores']
      },
      'Química': {
         'nome': 'química',
         'conteudos': ['reações químicas', 'química inorgânica', 'química orgânica', 'estequiometria', 'balanceamento', 'cinética química', 'forças intermoleculares']
      },
      'Português': {
         'nome': 'português',
         'conteudos': ['análise sintática', 'interpretação de texto', 'sequências textuais', 'coesão e coerência', 'gramática']
      },
      'Biologia': {
         'nome': 'biologia',
         'conteudos': ['citologia', 'reações metabólicas', 'histologia', 'anatomia e fisiologia', 'microbiologia', 'ecologia', 'biotecnologia']
      },
      'História': {
         'nome': 'história',
         'conteudos': ['idade média', 'idade antiga', 'américa espanhola', 'renascimento','Egito antigo', 'Grécia antiga', 'Brasil império', 'Brasil colonial', 'grandes navegações']
      },
      'Geografia': {
         'nome': 'geografia',
         'conteudos': ['Escalas', 'Coordenadas geográficas', 'geopolítica', 'biomas', 'solos', 'relevos']
      },
      'Filosofia': {
         'nome': 'filosofia',
         'conteudos': ['filósofos pré-socráticos', 'filosofia antropocêntrica', 'ética e moral']
      }
   }

   return render_template('carregarmaterias.html', materia=materias[materia])

@app.route('/logout')
def logout():
   resp = make_response(redirect('/autenticar'))
   resp.delete_cookie('ID_Usuario')
   return resp

if __name__ == "__main__":
   app.run(debug=True)