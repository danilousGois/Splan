from flask import Flask, render_template, request, flash, redirect, make_response, session
import json
import os
import uuid

app = Flask(__name__)
app.config['SECRET_KEY'] = 'chave_secreta_projeto_PSI'

def carregar_materias():
   if os.path.exists('static/materias.json'):
      with open('static/materias.json', 'r') as json_file:
         materias = json.load(json_file)  # Use '=' para atribuir os dados do arquivo à variável
      return materias
   return {} 

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
   if 'ID_Usuario' not in session:
      return redirect('/autenticar')
   nomeuser = session['nomeuser']
   return render_template('onboarding.html', nome = nomeuser)



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
   nomeuser = request.form['nome']
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
               if emailUser == lista_dict['email']:
                  flash('E-mail já cadastrado, faça login!', "primary")
                  return redirect('/autenticar')
         else:
            lista_usuarios = []

         dados_user = {
            "ID_Usuario": ID_Usuario,
            "nomeuser": nomeuser,
            "email": emailUser,
            "senha": senhaUser
         }

         lista_usuarios.append(dados_user)
         with open('static/dados_usuario.json', 'w') as json_file:
            json.dump(lista_usuarios, json_file, indent=4)

         session['ID_Usuario'] = ID_Usuario
         session['nomeuser'] = nomeuser
         session['email'] = emailUser     

         return redirect('/inicio')
      
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
         if email == lista_dict['email'] and senha == lista_dict['senha']:
            Ver_email = True
            Ver_senha = True
            session['ID_Usuario'] = lista_dict['ID_Usuario']
            session['nomeuser'] = lista_dict['nomeuser']
            session['email'] = lista_dict['email']
            return redirect('/inicio')

      if not (Ver_email and Ver_senha):
         flash('Esse usuário não existe! Faça o cadastro!')
         return redirect('/cadastrar')
   else:
      flash('Todos os campos devem ser preenchidos!', "warning")
      return redirect('/autenticar')


@app.route('/inicio/<materia>')
def carregarmateria(materia):
   nomeuser = session['nomeuser']
   materias = carregar_materias()
   if materia in materias:
      return render_template('carregarmaterias.html', materia=materias[materia], nome = nomeuser)
   else:
      return "Matéria não encontrada", 404

@app.route('/cronograma')
def cronograma():
   nomeuser = session['nomeuser']
   if verificar_user_logado() == True:
      return redirect('/inicio')
   return render_template('cronograma.html', nome = nomeuser)

@app.route('/profile')
def profile():
   if verificar_user_logado() == True:
      return redirect('/inicio')
   nomeuser = session['nomeuser']
   return render_template('perfil_user.html', nome=nomeuser)

@app.route('/formulario')
def formulario():
   return render_template('formulario.html')


@app.route('/logout')
def logout():
   session.clear()
   resp = make_response(redirect('/autenticar'))
   return resp

@app.route('/gerenciar_usuarios')
def base_adm():
   nomeuser = session['nomeuser']
   return render_template('gerenciar_usuario.html', nome=nomeuser)


if __name__ == "__main__":
   app.run(debug=True)