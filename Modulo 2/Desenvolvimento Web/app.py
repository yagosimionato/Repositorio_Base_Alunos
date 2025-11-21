
# importamos as bibliotecas que iremos utilizador
from flask import Flask, render_template, request, jsonify, redirect, url_for
from datetime import datetime
import json
import resend

# adicionamos a chave da API para recebimento de email
resend.api_key="re_TZXg7yEh_EmGSmfpisEx3MYR4FQcAy1fz"

# instanciamos a aplicação web
app= Flask(__name__)

# comando para construir o banco de dados com as mensagens recebidas
with open('dados.json','r',encoding='utf-8') as arquivo:
    dados=json.load(arquivo)

@app.route('/',methods=['POST','GET'])
def index():
    if request.method == 'POST':
        nome= request.form['name']
        email=request.form['email']
        mensagem=request.form['message']

# montar o dicionario da nova mensagem 
        dados_mensagem={
            'nome':nome,
            'email':email,
            'mensagem':mensagem,
            'data':f'{datetime.today()}'
         }
# adicionar e salvar no JSON
        dados.append(dados_mensagem)
        with open('dados.json', 'w', encoding='utf-8') as arquivo:
            json.dump(dados, arquivo, indent=4, ensure_ascil=False)

# envia e-mail usando resend
            r = resend.Emails.send({
            "from": "onboarding@resend.dev",
            "to": "yagosimionato351@gmail.com",
            "subject": f"Solicitaçao de adoção{nome}",
            "html": f"<p>Email:{email}<br>{mensagem}</p>"
            })
# apos o POST - redireciona para enviar reenvio do formulario
        return redirect(url_for('index')) # esse é um endpoint de retorno
    
# # GET - renderiza a página
    return render_template('index.html')

        
if __name__ =='__main__':
    app.run(debug=True)