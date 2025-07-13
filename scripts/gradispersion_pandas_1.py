# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 18:25:35 2024

@author: USUARIO
"""
import pandas as pd
import matplotlib.pyplot as plt

# Cargamos el archivo de datos
df = pd.read_csv('peajes.csv', delimiter=';', dtype='object')

# Correcciones en el DataFrame
df['DEP'] = df['DEP'].replace('Null', pd.NA)
df['DEP'] = df['DEP'].str.capitalize()

# Convertimos las columnas relevantes a numéricas
numeric_columns = ['CAT1', 'CAT2', 'CAT3', 'CAT4']
df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric, errors='coerce')

# Eliminamos filas con valores no numéricos
df.dropna(subset=numeric_columns, inplace=True)

# Gráfica de dispersión para comparar múltiples columnas
plt.figure(figsize=(10, 6))
scatter = plt.scatter(df['CAT1'], df['CAT2'], c=df['CAT3'], s=df['CAT4'] / 100, cmap='viridis')
plt.colorbar(scatter, label='Tarifa categoría tres')
plt.title('Comparación de múltiples tarifas', fontsize=16)
plt.xlabel('Tarifa categoría uno', fontsize=12)
plt.ylabel('Tarifa categoría dos', fontsize=12)
plt.tight_layout()
plt.show()

