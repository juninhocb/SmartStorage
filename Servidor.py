from flask import Flask, jsonify, request
from funcs import *

app = Flask("Server Smart Storage")

@app.route("/cadastro", methods = ['POST'])
def cadastraUsuarios():
    
    body = request.get_json()
    
    usuario = novoUsuario(body["nome"], body["email"], body["senha"])
    
    return {"status:": 200 ,"dados": usuario}

@app.route("/dados", methods = ['POST'])
def recebeDados():
    
    body = request.get_json()
    
    dado = novoDado(body["usuario"], body["apartamento"])
    
    return {"status:": 200, "informações de entrega": dado}


app.run()