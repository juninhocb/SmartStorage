from flask import Flask, jsonify, request
from funcs import *
from lendoEtiqueta import lerEtiqueta
from peewee import *
from Dados import Dado
from Dados import User
from playhouse.shortcuts import dict_to_model
import os


app = Flask("Server Smart Storage")

#dado1 = Dado.create(nome = 'Marcela',endereco = 'Rua Tal numero tal', bloco = 'C', ap = '110', img = 'Etiqueta2.jpg' )

for d in Dado.select():
    print("Nome:  ")
    print(d.nome)

@app.route("/cadastro", methods = ['POST'])
def cadastraUsuarios():
    
    body = request.get_json()
    
    usuarioAPP = novoUsuario(body["nome"], body["email"], body["senha"])
    
    return {"status:": 200 ,"dados": usuarioAPP}

@app.route("/dados", methods = ['POST'])
def recebeDados():
    
    body = request.get_json()
    
    dado = novoDado(body["nome"], body["endereco"], body["bloco"], body["ap"])
    
    Dado.create(nome = dado.get("nome"), endereco = dado.get("endereco"), bloco = dado.get("bloco"), ap = dado.get("ap"))
    
    return {"status:": 200, "informações de entrega": dado}

@app.route("/enviar", methods = ['Get'])
def enviaDados():
    
    body = request.get_json()
    
    receber  = body["imagem"] 
    
    ok = "OK!"
    
    usuario = lerEtiqueta(receber)
    
    User.create(usuario = usuario, img = (receber))
    
    return {"status:": 200, "Encomenda de":usuario, "Status da Entrega": ok}


app.run()