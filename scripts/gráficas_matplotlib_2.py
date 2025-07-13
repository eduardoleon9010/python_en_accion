# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 20:27:33 2024

@author: USUARIO
"""
import matplotlib.pyplot as plt
import random
import numpy as np

# Datos simulados de temperatura para diferentes estaciones con valores atípicos
datos_climaticos = {
    'Estacion1': [random.uniform(15, 25) for _ in range(90)] + [random.uniform(40, 50) for _ in range(10)],
    'Estacion2': [random.uniform(10, 20) for _ in range(90)] + [random.uniform(5, 35) for _ in range(10)],
    'Estacion3': [random.uniform(20, 30) for _ in range(90)] + [random.uniform(25, 40) for _ in range(10)],
    'Estacion4': [random.uniform(18, 28) for _ in range(90)] + [random.uniform(15, 35) for _ in range(10)],
}

# Crear el gráfico de caja (boxplot)
plt.figure(figsize=(10, 6))  # Tamaño de la figura
plt.boxplot(datos_climaticos.values(), labels=datos_climaticos.keys(), showfliers=True)  # Crear el boxplot con outliers
plt.title('Distribución de temperaturas por estación')  # Título del gráfico
plt.xlabel('Estación')  # Etiqueta del eje X
plt.ylabel('Temperatura (°C)')  # Etiqueta del eje Y
plt.xticks(rotation=45)  # Rotación de las etiquetas en el eje X para mejor visualización
plt.grid(True)  # Mostrar cuadrícula en el gráfico
plt.tight_layout()  # Ajustar el diseño del gráfico
plt.show()  # Mostrar el boxplot
