#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  gera_cpf.py

from tkinter import *
import gera_cpf



def main():
    janela = Tk()
    janela.title('Gera CPF')
    janela.geometry("200x115") #tamanho da janela
    
    title = Label(janela, text="Gera CPF", font=('bold') ).pack()
    
    
    def gerar_cpf():
        cpf = gera_cpf.gera_cpf()
        label["text"] = cpf

    def limpar():
        label["text"] = ""

    b = Button(janela, text="Gerar CPF", width=10, command=gerar_cpf).pack()
    b = Button(janela, text="Limpar", width=10, command=limpar).pack()
    
    label = Label(janela)
    label.pack()

    janela.mainloop()

if __name__ == '__main__':
    main()


