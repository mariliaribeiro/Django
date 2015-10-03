#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  valida_cpf.py

from tkinter import *
import valida_cpf


def main():
    janela = Tk()
    janela.title('Valida CPF')
    janela.geometry("200x125") #tamanho da janela
    
    title = Label(janela, text="Valida CPF", font=('bold') ).pack()
    
    et = Entry(janela)
    et.pack()

    def validacao():
        #print (et.get())
        cpf = et.get()
        if valida_cpf.valida_cpf(cpf):
            label["text"] = 'CPF válido!'
        else:
            label["text"] = 'Informe um CPF válido!'
    
    def limpar():
        label["text"] = ''
        et["textvariable"]= ''

    b = Button(janela, text="Validar", width=10, command=validacao).pack()
    b = Button(janela, text="Limpar", width=10, command=limpar).pack()
    
    label = Label(janela)
    label.pack()
    
    
    janela.mainloop()

if __name__ == '__main__':
    main()

