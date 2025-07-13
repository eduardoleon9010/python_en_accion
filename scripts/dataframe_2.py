# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 21:17:09 2024

@author: USUARIO
"""
import pandas as pd

# Leer el archivo CSV y cargarlo en un DataFrame
df_secop = pd.read_csv('SECOP_II_-_Contratos_Electr_nicos.csv')

# Mostrar las primeras filas del DataFrame para verificar la carga de datos
print(df_secop.head())
