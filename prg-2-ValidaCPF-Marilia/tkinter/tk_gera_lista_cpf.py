#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  gera_lista_cpf.py

from tkinter import *
import gera_lista_cpf


def main():
    janela = Tk()
    janela.title('Gera Lista CPF')
    janela.geometry("360x150") #tamanho da janela
    
    title = Label(janela, text="Gerar lista de CPFs", font=('bold') ).pack()
    
    hint = Label(janela, text="Informe o tamanho da lista:").pack()
    et = Entry(janela)
    et.pack()
  
    def gerar_cpf():
        len_lista = et.get()
        if len_lista == '':
            lista_cpf = [gera_lista_cpf.gera_lista_cpf()]
        else:
            lista_cpf = [gera_lista_cpf.gera_lista_cpf(len_lista)]
        label["text"] = lista_cpf

    def limpar():
       label["text"] = ""

    b = Button(janela, text="Gerar CPF", width=10, command=gerar_cpf).pack()
    b = Button(janela, text="Limpar", width=10, command=limpar).pack()
    
    label = Label(janela)
    label.pack()

    janela.mainloop()

if __name__ == '__main__':
    main()

