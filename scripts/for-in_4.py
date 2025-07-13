# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 11:04:27 2024

@author: USUARIO
"""

num = float(input("Digite un numero: "))

for n in range(1, 101):
    print("La raiz {0} de {1} es 2".format(n, num, num **(1/n)))
    
    