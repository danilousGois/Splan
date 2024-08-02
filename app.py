from flask import Flask, render_template, request
from flask import flash, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'chave secreta projeto PSI'


@app.route('/')
def index():
   return render_template('paginainicial.html')


@app.route('/<valor>')
def login_signin(valor):
   renderizar_arquivo = ''

   if valor == 'login':
      renderizar_arquivo = 'login'
   else:
      renderizar_arquivo = 'signin'

   return render_template(renderizar_arquivo + '.html')



@app.route('/signin', methods=['POST'])
def validarsignin():
   emailUser = request.form['email']
   senhaUser = request.form['senha']
   confirmarsenha = request.form['confirmarsenha']

   if senhaUser != confirmarsenha:
      flash('A confirmação da senha está incorreta!')
      redirect('/signin')
      # fazer a verificação do email
   else:
      pass

   return render_template('login.html')




@app.route('/login', methods=['POST'])
def verificarlogin():
   emailUser = "danilo"
   senhaUser = "123"
   senha = request.form['senha']
   email = request.form['email']

   if emailUser == '' and senhaUser == '':
      flash('Verificamos que ainda não possui um cadastro no nosso sistema! Faça agora mesmo!')
      redirect('/signin')
   elif senha != senhaUser:
      flash('Senha inválida!')
      redirect('/login')
   elif email != emailUser:
      flash('E-mail inválida')
      redirect('/login')
   else:
      pass

   return render_template('base_landingpage.html')



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