# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 08:44:34 2024

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

# Obtener el valor del cuartil 95
cuartil_95 = numericos.quantile(0.95)

# Imprimir el valor del cuartil 95
print("\nValor del cuartil 95:")
print(cuartil_95)

# Calcular la suma de cada fila y agregarla como una nueva columna
suma_por_fila = numericos.sum(axis=1)
df_secop['Suma por fila'] = suma_por_fila

# Imprimir las primeras filas del DataFrame con la nueva columna
print("\nDataFrame con la columna 'Suma por fila':")
print(df_secop.head())
