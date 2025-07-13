# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 19:55:33 2024

@author: USUARIO
"""

import pandas as pd

# Leer el archivo CSV y cargarlo en un DataFrame
df_secop = pd.read_csv('SECOP_II_-_Contratos_Electr_nicos.csv')

# Seleccionar solo las columnas categóricas
categoricos = df_secop.select_dtypes(include='object')

# Obtener valores únicos en la columna 'Estado Contrato'
valores_unicos = categoricos['Estado Contrato'].unique()

# Convertir la serie de valores únicos a una lista
lista_valores_unicos = valores_unicos.tolist()

# Obtener la cantidad de veces que aparece cada valor en la columna 'Estado Contrato'
conteo_valores = categoricos['Estado Contrato'].value_counts()

# Obtener solo los índices (valores únicos) de la serie de conteo de valores
indices_valores = conteo_valores.index

# Convertir los índices a una lista
lista_indices_valores = indices_valores.tolist()

# Imprimir resultados
print("Valores únicos en 'Estado Contrato':", lista_valores_unicos)
print("Índices (valores únicos) de conteo de valores en 'Estado Contrato':", lista_indices_valores)
