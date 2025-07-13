# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 18:16:54 2024

@author: USUARIO
"""

import pandas as pd
import matplotlib.pyplot as plt

# Creamos un DataFrame de ejemplo con datos de estaturas y pesos
data = {
    'Estatura (cm)': [160, 165, 170, 175, 180, 185, 190],
    'Peso (kg)': [55, 60, 65, 70, 75, 80, 85],
    'Edad': [25, 30, 35, 40, 45, 50, 55],
    'IMC': [21.48, 22.04, 22.49, 22.86, 23.15, 23.37, 23.53] # Índice de Masa Corporal
}
df = pd.DataFrame(data)

# Creamos el gráfico de dispersión
plt.figure(figsize=(10, 8))
plt.scatter(
    df['Estatura (cm)'],
    df['Peso (kg)'],
    s=df['Edad']*10,  # Tamaño de los puntos según la edad
    c=df['IMC'],  # Color de los puntos según el IMC
    cmap='viridis',  # Mapa de colores
    alpha=0.7,  # Transparencia de los puntos
    marker='o',  # Estilo de marcador
    edgecolors='black',  # Color del borde de los puntos
    linewidths=1.5,  # Grosor del borde de los puntos
)

# Añadimos una barra de color
plt.colorbar(label='IMC')  # Etiqueta de la barra de color

# Añadimos títulos y etiquetas
plt.title('Relación entre Estatura, Peso y Edad con el IMC')
plt.xlabel('Estatura (cm)')
plt.ylabel('Peso (kg)')

# Añadimos una leyenda
plt.legend(['Edad'], loc='upper right')

# Mostramos la figura
plt.grid(True)
plt.show()
