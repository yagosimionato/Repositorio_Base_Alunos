# exercicio 3.3: condicionais em templates
# crie uma rota que envie uma idade e, no template, use if para
# mostrar uma mensagem se a pessoa for maior de idade e outra se for menor de idade.

from flask import flask, render_template
app = flask(__name__)

@app.route('/') # primeira pagina (home ou index)
def index():
    return 'hello flask'
@app.route('/sobre')# segunda pagina
def sobre():
    return 'ola, eu sou aluno do projeto fabrica de programadores.'
@app.route('/idade/<int:idade>') # terceira pagina
def idade(idade):
    return render_template('ex_3-3.html',idade=idade)
