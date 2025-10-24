from flask import flask, render_template

# cria uma nstancia de um servidor flask
app = flask (__name__)

# cria rota para pagina inicial "do site"
@app.route('/')
def index():
    return render_template('index.html')

