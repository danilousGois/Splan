from flask import Flask, render_template, request
from flask import flash, redirect
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'chave secreta projeto PSI'
arquivo =  open('static/usuarios.json')
usuarios = json.load(arquivo)

@app.route('/')
def index():
   return render_template('paginainicial.html')

@app.route('/inicio')
def carregarLandingPage():
   return render_template('base_landingpage.html')


@app.route('/<valor>')
def paginainicial(valor):
   if valor == 'autenticar':
      return render_template('login.html')
   else:
      return render_template('signup.html')


@app.route('/cadastrar', methods=['POST'])
def validarsignup():
   emailUser = request.form['email']
   senhaUser = request.form['senha']
   confirmarsenha = request.form['confirmarsenha']
   dados_login = {}


   if len(emailUser) != 0 and len(senhaUser) != 0 and len(confirmarsenha) != 0:
      if senhaUser == confirmarsenha:
         dados_login = {'email': emailUser, 'senha':senhaUser}
         
         return redirect('/autenticar')
      else:
         flash('Senha e confirmação devem ser iguais!')
         return redirect('/cadastrar')
   else:
      flash('Todos os campos devem ser preenchidos!')
      return redirect('cadastrar')
      


@app.route('/autenticar', methods=['POST'])
def verificarlogin():
   email = request.form['email']
   senha = request.form['senha']

   if len(email) != 0 and len(senha) != 0:
      if email == 'admin' and senha == '123':
         return redirect('/inicio')
      elif email == 'admin' and senha != '123':
         flash('Senha incorreta!')
         return redirect('/autenticar') 
      elif email != 'admin' and senha == '123':
         flash('Dados inválidos')
         return redirect('/autenticar')
      else:
         flash('Dados inválidos')
         return redirect('/autenticar')
   else:
      flash('Todos os campos devem ser preenchidos!')
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



if __name__ == "__main__":
    app.run