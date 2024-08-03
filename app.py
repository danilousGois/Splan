from flask import Flask, render_template, request
from flask import flash, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'chave secreta projeto PSI'


@app.route('/')
def index():
   return render_template('paginainicial.html')


@app.route('/<valor>')
def paginainicial(valor):
   return render_template(valor + '.html')


@app.route('/inicio', methods=['POST'])
def verificarlogin():
   email = request.form['email']
   senha = request.form['senha']

   if senha == '123' and email == 'danilo':
      return render_template('base_landingpage.html')
   else:
      return render_template('login.html')
   # fazer o resto das verificações



@app.route('/signin', methods=['POST'])
def validarsignin():
   emailUser = request.form['email']
   senhaUser = request.form['senha']
   confirmarsenha = request.form['confirmarsenha']

   if senhaUser == confirmarsenha:
      return render_template('login.html')
   else:
      return render_template('signin.html')
   




@app.route('/<materia>')
def carregarmateria(materia):

   materias = {
      'Matemática': {
         'nome': 'matemática',
         'conteudos': ['análise combinatória', 'funções', 'trigonometria', 'geometria', 'algebra']
      }, 
      'Física': {
         'nome': 'física',
         'conteudos': ['dinâmica', 'eletrodinâmica', 'eletromagneteismo', 'óptica', 'calorimetria']
      },
      'Química': {
         'nome': 'química',
         'conteudos': ['reações químicas', 'química inorgânica', 'química orgânica', 'estequiometria', 'balanceamento', 'cinética química']
      },
      'Português': {
         'nome': 'português',
         'conteudos': ['análise sintática', 'interpretação de texto', 'sequências textuais', 'coesão e coerência']
      },
      'Biologia': {
         'nome': 'biologia',
         'conteudos': ['citologia', 'reações metabólicas', 'histologia', 'anatomia e fisiologia', 'microbiologia']
      },
      'História': {
         'nome': 'história',
         'conteudos': ['idade média', 'idade antiga', 'américa espanhola', 'renascimento','Rgito antigo', 'Grécia antiga']
      }
   }

   return render_template('carregarmaterias.html', materia=materias[materia])



if __name__ == "__main__":
    app.run