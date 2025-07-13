# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 17:57:12 2024

@author: USUARIO
"""

sumatoria = 0
i = 1
iteraciones = 0
while i <= 1000:
    iteraciones+=1
    sumatoria += i
    i += 1
print("El resultado de la sumatoria es: ", sumatoria)
print("El número de iteraciones fue: ", iteraciones)
print("El valor de i es: ", i)