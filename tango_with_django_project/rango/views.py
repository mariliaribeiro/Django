#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    #return HttpResponse("Rango says hey there world!")
    #return HttpResponse("Rango says: Hello world! <br/> <a href='about/'>About</a>")#<a href='/rango/about'>

    #construindo um dicionário para passar ao template
    #a chave boldmessage foi declarado no template {{ boldmessage }}
    context_dict = {'boldmessage': "I am bold font from the context"}
    return render(request, 'rango/index.html', context_dict)

def about(request):
    #return HttpResponse("Rango says here is the about page.")
    return HttpResponse("<a href='/'>Index</a>") #"<a href='/rango/'>Index</a>"




