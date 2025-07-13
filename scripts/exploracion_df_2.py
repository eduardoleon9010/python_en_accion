# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 08:34:06 2024

@author: USUARIO
"""

import pandas as pd

# Leer el archivo CSV y cargarlo en un DataFrame
df_secop = pd.read_csv('SECOP_II_-_Contratos_Electr_nicos.csv')

# Seleccionar solo las columnas numéricas
numericos = df_secop.select_dtypes(include='number')

# Obtener un resumen estadístico de las columnas numéricas
resumen_estadistico = numericos.describe()

# Imprimir el resumen estadístico
print("Resumen estadístico de las columnas numéricas:")
print(resumen_estadistico)

# Obtener el promedio de cada columna numérica
promedios = numericos.mean()

# Obtener la desviación estándar de cada columna numérica
desviaciones_estandar = numericos.std()

# Obtener el valor máximo de cada columna numérica
maximos = numericos.max()

# Obtener el valor mínimo de cada columna numérica
minimos = numericos.min()

# Obtener el índice del valor máximo de cada columna numérica
indices_maximos = numericos.idxmax()

# Obtener el índice del valor mínimo de cada columna numérica
indices_minimos = numericos.idxmin()

# Imprimir los resultados
print("\nPromedio de cada columna numérica:")
print(promedios)
print("\nDesviación estándar de cada columna numérica:")
print(desviaciones_estandar)
print("\nValor máximo de cada columna numérica:")
print(maximos)
print("\nValor mínimo de cada columna numérica:")
print(minimos)
print("\nÍndice del valor máximo de cada columna numérica:")
print(indices_maximos)
print("\nÍndice del valor mínimo de cada columna numérica:")
print(indices_minimos)
