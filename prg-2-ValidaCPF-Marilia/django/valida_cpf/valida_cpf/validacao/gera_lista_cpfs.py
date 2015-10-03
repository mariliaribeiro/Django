#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  gera_lista_cpf.py
#  
#  Marilia Ribeiro da Silva <marilia.ifc@gmail.com>

import gera_cpfs

def gera_lista_cpf(len_lista_cpf='3'):
    return [gera_cpfs.gera_cpf() for i in range(int(len_lista_cpf))]
    
def main():
    len_lista_cpf = (input('Informe quantos CPFs você deseja armazenar: '))
    print(gera_lista_cpf(len_lista_cpf))
    
    
 

if __name__ == '__main__':
    main()
