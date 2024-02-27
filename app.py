from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('menu_inicial.html')


@app.route('/filipi')
def filipi():
    return render_template('filipi.html')

@app.route('/ronald')
def ronald():
    return render_template('ronald.html')

#render_template vai sempre procurar na pasta 'templates'
#a pasta templates tem que estar na mesma hierarquia do venv e do __pycache__

#criar o gitignore na linha de comando: touch .gitignore


if __name__ == '__main__':
    app.run()