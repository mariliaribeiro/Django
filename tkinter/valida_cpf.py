#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  valida_cpf.py
#  
#  Marilia Ribeiro da Silva <marilia.ifc@gmail.com>



def limpa_cpf(cpf):
    '''
    Recebe como parâmetros uma string.
    Retorna somente os números digitados.
    >>> limpa_cpf('08313671998')
    '08313671998'
    >>> limpa_cpf("083.136.719-98")
    '08313671998'
    >>> limpa_cpf("083.136.719@98")
    '08313671998'
    >>> limpa_cpf("")
    ''
    >>> limpa_cpf("1")
    '1'
    >>> limpa_cpf("aaaa")
    ''
    '''
    import string
    return "".join([caracter for caracter in cpf if caracter in string.digits])

def verifica_digitos(cpf):
    '''
    Recebe como parâmetro uma string.
    Verifica o tamanho da string e retorna somente os de tamanho 11.
    >>> verifica_digitos('08313671998')
    True
    >>> verifica_digitos("083.136.719-98")
    False
    >>> verifica_digitos("083.136.719@98")
    False
    >>> verifica_digitos("")
    False
    >>> verifica_digitos("1")
    False
    >>> verifica_digitos("aaaa")
    False
    '''
    return len(cpf) == 11

def inverte_cpf(cpf, contador):
    '''
    Recebe como parâmetros uma string contendo somente números e um contador.
    Cria uma lista com esses números e retorna a lista invertida.
    >>> inverte_cpf('08313671998', 0)
    ['9', '1', '7', '6', '3', '1', '3', '8', '0']
    >>> inverte_cpf('08313671998', 1)
    ['9', '9', '1', '7', '6', '3', '1', '3', '8', '0']
    '''
    cpf = list(cpf)
    return cpf[-3::-1] if contador < 1 else cpf[-2::-1]

def soma_produto_lista_cpf(cpf, contador):
    '''
    Recebe como parâmetros uma string contendo somente números e um contador.
    Converte o digito para inteiro e efetua a soma de produtos (digito da lista * i+2) da lista.
    >>> soma_produto_lista_cpf('08313671998', 0)
    200
    >>> soma_produto_lista_cpf('08313671998', 1)
    256
    '''
    cpf_invertido = inverte_cpf(cpf, contador)
    return sum([int(dig) *(i+2) for i, dig in enumerate(cpf_invertido)])

def gera_digito_verificador(cpf, contador):
    '''
    Recebe como parâmetros uma string contendo somente números e um contador.
    Recebe a soma de produtos da lista e divide por 11.
    Se o resto < 2 o digito = 0
    Senão: digito = 11 - resto da divisão
    Retorna os valores em string
    >>> gera_digito_verificador('08313671998', 0)
    '9'
    >>> gera_digito_verificador('08313671998', 1)
    '8'
    '''
    numero = soma_produto_lista_cpf(cpf, contador)
    resto = (numero % 11)        
    return str(0) if resto < 2 else str(11 - resto)

def valida_cpf(cpf):
    '''
    Recebe como parâmetro uma string.
    Faz a validação de um CPF, retornando verdadeiro se satisfazer as 
    condições de validação de um cpf.
    >>> valida_cpf('08313671998')
    True
    >>> valida_cpf("083.136.719-98")
    True
    >>> valida_cpf("083.136.719@98")
    True
    >>> valida_cpf("")
    False
    >>> valida_cpf("1")
    False
    >>> valida_cpf("aaaa")
    False
    '''
    cpf = limpa_cpf(cpf)
    if verifica_digitos(cpf):
        digitos = ''.join([gera_digito_verificador(cpf, i) for i in range(2)])
        return digitos == cpf[-2:]
    return False

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    
