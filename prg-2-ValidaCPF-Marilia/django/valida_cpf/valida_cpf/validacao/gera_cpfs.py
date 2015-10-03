#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  valida_cpf.py
#  
#  Marilia Ribeiro da Silva <marilia.ifc@gmail.com>

import random
import valida_cpfs

def gera_cpf():
    digitos_cpf = ''.join([str(random.randint(0,9)) for i in range(9)])
    for i in range(100):
        digito_verificador = str('%02d' %i)
        cpf = digitos_cpf + digito_verificador
        imprime_cpf = '%s.%s.%s-%s' %(cpf[:3], cpf[3:6], cpf[6:9],cpf[9:])
        if valida_cpfs.valida_cpf(cpf): return imprime_cpf

def main():
    print(gera_cpf())
 

if __name__ == '__main__':
    main()
