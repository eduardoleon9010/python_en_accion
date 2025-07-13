# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 21:04:45 2024

@author: USUARIO
"""

import pandas as pd
import numpy as np

def aumentar_notas(notas):
    # Calcular la media de las notas
    media_notas = notas.mean()
    
    # Verificar si la media es mayor que 2.5
    if media_notas > 2.5:
        # Aumentar todas las notas en una desviación estándar
        notas_aumentadas = notas + notas.std()
        
        # Redondear las notas a dos decimales
        notas_aumentadas = notas_aumentadas.round(2)
        
        # Verificar si alguna nota supera 5 y ajustarla si es necesario
        notas_aumentadas = notas_aumentadas.apply(lambda x: min(x, 5))
        
        return notas_aumentadas
    else:
        # Si la media no es mayor que 2.5, retornar las notas originales sin cambios
        return notas

# Ejemplo de uso
notas_originales = pd.Series(np.random.normal(loc=3, scale=1, size=15))
print("Notas originales:")
print(notas_originales)

notas_actualizadas = aumentar_notas(notas_originales)
print("\nNotas después del aumento:")
print(notas_actualizadas)
