# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 19:08:03 2024

@author: USUARIO
"""


import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos desde el archivo CSV
datos = pd.read_csv('datos_climaticos.csv')

# Convertir la columna 'AÑO' a tipo datetime
datos['AÑO'] = pd.to_datetime(datos['AÑO'], format='%Y')

# Contar el número de estaciones por año
estaciones_por_año = datos.groupby('AÑO')['ESTACIÓN'].nunique()

# Crear la figura y los subplots
fig, ax = plt.subplots(figsize=(10, 6))

# Graficar el número de estaciones por año
ax.plot(estaciones_por_año.index, estaciones_por_año.values, color='b', marker='o', label='Número de Estaciones')

# Título y etiquetas
ax.set_title('Evolución del Número de Estaciones Climáticas por Año')
ax.set_xlabel('Año')
ax.set_ylabel('Número de Estaciones')
ax.grid(True)
ax.legend()

# Mostrar la gráfica
plt.tight_layout()
plt.show()
