#!/usr/bin/env python
# -*- coding: utf-8 -*-


from django.shortcuts import render_to_response
from django.template import RequestContext
import valida_cpfs
import gera_cpfs
import gera_lista_cpfs

# chama página principal

def index(request):
    return render_to_response("index.html", {}, context_instance = RequestContext(request))

def valida_cpf(request):
    resposta = None
    cpf = None

    if request.method=="POST":
        cpf = request.POST.get("cpf")
        item = valida_cpfs.valida_cpf(cpf)
        if item:
            resposta = 'CPF válido!'
        else:
            resposta = 'Informe um CPF válido!'
    return render_to_response("valida_cpf.html", {'resposta':resposta, 'cpf':cpf}, context_instance = RequestContext(request))

def gera_cpf(request):
    cpf = None
    if request.method=="POST":
        cpf = gera_cpfs.gera_cpf()
    return render_to_response("gera_cpf.html", {'cpf':cpf}, context_instance = RequestContext(request))

def gera_lista_cpf(request):
    len_lista = None 
    lista = None

    if request.method=="POST":
        if len_lista == '':
            lista = gera_lista_cpfs.gera_lista_cpf()
        else:
            len_lista = request.POST.get("len_lista")
            lista = gera_lista_cpfs.gera_lista_cpf(len_lista)
    return render_to_response("gera_lista_cpf.html", {'lista':lista, 'len_lista':len_lista}, context_instance = RequestContext(request))
