from flask import Flask, jsonify, request
from funcs import *
from lendoEtiqueta import lerEtiqueta

app = Flask("Server Smart Storage")

@app.route("/cadastro", methods = ['POST'])
def cadastraUsuarios():
    
    body = request.get_json()
    
    usuarioAPP = novoUsuario(body["nome"], body["email"], body["senha"])
    
    return {"status:": 200 ,"dados": usuarioAPP}

@app.route("/dados", methods = ['POST'])
def recebeDados():
    
    body = request.get_json()
    
    dado = novoDado(body["usuario"], body["apartamento"])
    
    return {"status:": 200, "informações de entrega": dado}

@app.route("/enviar", methods = ['Get'])
def enviaDados():
    
    body = request.get_json()
    
    receber  = body["imagem"] 
    
    ok = "OK!"
    
    usuario = lerEtiqueta(receber)
    
    return {"status:": 200, "Encomenda de":usuario, "Status da Entrega": ok}


app.run()