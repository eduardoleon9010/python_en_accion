# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 08:55:56 2024

@author: USUARIO
"""

archivo = open("Protesis.txt","r")

linea = archivo.readline()

while linea !="":
    print(linea)
    linea = archivo.readline()
    
archivo.close()