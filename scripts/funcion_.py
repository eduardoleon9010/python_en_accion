# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 20:41:57 2024

@author: USUARIO
"""

matriz = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]

def funcion(matriz: list)->int:
    suma = 0
    for i in range (0, len(matriz)):
        for j in range (i, len(matriz[0])):
            suma = suma + matriz[i][j]
    return suma

print(funcion(matriz))