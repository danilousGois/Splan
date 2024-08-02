from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
   return render_template('paginainicial.html')


@app.route('/<valor>')
def login_signin():
   renderizar_arquivo = ''

   if valor == 'login':
      renderizar_arquivo = 'login'
   else:
      renderizar_arquivo = 'signin'

   return render_template(renderizar_arquivo + '.html')

@app.route('/signin', methods=['POST'])
def validarsignin():
   email = request.form['email']
   senha = request.form['senha']
   confirmarsenha = request.form['confirmarsenha']

   if senha != confirmarsenha:
      


@app.route('/login')
def verificarlogin():
   if email != '' and senha != '':




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