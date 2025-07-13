# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 18:49:31 2024

@author: USUARIO
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carga y correcciones en el DataFrame
df = pd.read_csv('peajes.csv', delimiter=';', dtype='object')
df['DEP'] = df['DEP'].replace('Null', pd.NA)
df['DEP'] = df['DEP'].str.capitalize()

# Convertir columnas relevantes a tipo numérico
columns_to_convert = ['CAT1', 'CAT2', 'CAT3', 'CAT4', 'CAT5', 'CAT6', 'CAT7']
df[columns_to_convert] = df[columns_to_convert].apply(pd.to_numeric, errors='coerce')

# Crear matriz de dispersión
sns.pairplot(df.drop(columns=['TIPO', 'NOMBRE', 'CONCESION', 'GEN', 'SENTIDO', 'COD_VIA', 'CONCESIONA', 'INIC_OPER', 'ETIQUETA', 'longitud', 'latitud']), hue='DEP')
plt.suptitle('Matriz de Dispersión para Peajes')
plt.show()
