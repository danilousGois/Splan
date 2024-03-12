from flask import Flask, render_template

app = Flask(__name__)

@app.route('/perfil/<user>/<cor>')
def perfil(user, cor):
    return render_template('perfil.html', usuario=user, cor=cor)

#render_template vai sempre procurar na pasta 'templates'
#a pasta templates tem que estar na mesma hierarquia do venv e do __pycache__

#criar o gitignore na linha de comando: touch .gitignore




if __name__ == '__main__':
    app.run()