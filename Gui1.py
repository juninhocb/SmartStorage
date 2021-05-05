from tkinter import *
import os
from Dados import Dado
from Dados import User

class Gui1():
   
    def showMain(self):
         
        #command = messagebox.showwarning(title=None, message="Confira os dados Por Favor!")
        
                                    ### CRIÇÃO DA FRAME ###
        self.frame1 = Frame(self.root, bg = '#F8F8FF')
        self.frame1.place(relx = 0.025, rely = 0.025, relwidth = 0.95, relheight = 0.95)
        
                                    ### LABELS ###
        self.lb_projetos = Label(self.frame1, text = "Smart Storage - Receptor de Encomendas"
                                 , font = ('verdana', 15, 'bold'), bg = '#F8F8FF')
        self.lb_projetos.place(relx = 0.025, rely = 0.025)
        
        self.lb_Nome = Label(self.frame1, text = "Os dados do favorecido serão exibidos nos campos abaixo!"
                                 , font = ('verdana', 10, 'bold'), bg = '#F8F8FF')
        self.lb_Nome.place(relx = 0.025, rely = 0.15)
        
        self.lb_Nome = Label(self.frame1, text = "Nome"
                                 , font = ('verdana', 10, 'bold'), bg = '#F8F8FF')
        self.lb_Nome.place(relx = 0.025, rely = 0.24)
        
        self.lb_Nome = Label(self.frame1, text = "Endereço"
                                 , font = ('verdana', 10, 'bold'), bg = '#F8F8FF')
        self.lb_Nome.place(relx = 0.025, rely = 0.42)
        
        self.lb_Nome = Label(self.frame1, text = "Bloco"
                                 , font = ('verdana', 10, 'bold'), bg = '#F8F8FF')
        self.lb_Nome.place(relx = 0.025, rely = 0.60)
        
        self.lb_Nome = Label(self.frame1, text = "AP"
                                 , font = ('verdana', 10, 'bold'), bg = '#F8F8FF')
        self.lb_Nome.place(relx = 0.20, rely = 0.60)
        
        self.lb_Nome = Label(self.frame1, text = "Por favor, insira abaixo o nome do receptor da encomenda"
                                 , font = ('verdana', 10, 'bold'), bg = '#F8F8FF')
        self.lb_Nome.place(relx = 0.027, rely = 0.78)
        
                                    ### Entry ###
        
        self.entryName = Entry(self.frame1, textvariable="teste conteudo")
        self.entryName.place(relx = 0.027, rely = 0.30, height = 30, width = 250)
        
        self.entryEnd = Entry(self.frame1)
        self.entryEnd.place(relx = 0.027, rely = 0.48, height = 30, width = 250)
        
        self.entryBloco = Entry(self.frame1)
        self.entryBloco.place(relx = 0.027, rely = 0.67, height = 30, width = 115)
        
        self.entryAp = Entry(self.frame1)
        self.entryAp.place(relx = 0.20, rely = 0.67, height = 30, width = 115)
        
        self.entryNomeKey = Entry(self.frame1)
        self.entryNomeKey.place(relx = 0.027, rely = 0.87, height = 30, width = 200)
        
        self.entryNomeKey.insert(0, "Digite Aqui")
        
                                                   ###  Botões###
        
        self.btOk = Button(self.frame1, text = "Carregar Dados",bg = "grey", command=lambda:setTextInput(self, self.entryNomeKey.get(), self.frame1)
                                , font = ('verdana', 12, 'bold'))
        self.btOk.place(relx = 0.37  , rely = 0.87, relwidth = 0.40, relheight = 0.1)
        
        
        
                                                ### FIM BOTÕES ###
        
def setTextInput(self, key, frame1):
    
    outKey = False
    self.nome = ""
    self.endereco = ""
    self.bloco = ""
    self.ap = ""
    self.nomeKey = key
    self.img = ""
    
    for d in Dado.select():
        if (d.nome == self.nomeKey):
            self.nome = d.nome
            self.endereco = d.endereco
            self.bloco = d.bloco
            self.ap = d.ap
            #self.img = d.img
            outKey = True
        elif (outKey == False):
            self.nome = "não consta no banco de dados"
            self.endereco = "não consta no banco de dados"
            self.bloco = "não consta no BD"
            self.ap = "não consta no BD"
            
            
    for u in User.select():
        if (u.usuario == self.nomeKey):
            self.img = u.img
    
    
    if(self.img):
        self.imagem = PhotoImage(file= self.img)
        self.w = Label(frame1, image = self.imagem)
        self.w.imagem = self.imagem
        self.w.place(relx = 0.37, rely = 0.3, height = 130, width = 350)
    else:
        print("ok")
        self.imagem = PhotoImage(file= "ProdutoS.png")
        self.w = Label(frame1, image = self.imagem)
        self.w.imagem = self.imagem
        self.w.place(relx = 0.5, rely = 0.3, height = 130, width = 180)
        
    self.entryName.delete(0,"end")
    self.entryName.insert(0, self.nome)
    
    self.entryEnd.delete(0,"end")
    self.entryEnd.insert(0, self.endereco)
    
    self.entryBloco.delete(0,"end")
    self.entryBloco.insert(0, self.bloco)
    
    self.entryAp.delete(0,"end")
    self.entryAp.insert(0, self.ap)
    
    



        
        
        
        
         

   