# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 18:03:47 2024

@author: USUARIO
"""
import pandas as pd
import matplotlib.pyplot as plt

# Creamos un DataFrame de ejemplo con datos de salud
data = {
    'Grupo': ['Control', 'Control', 'Control', 'Experimental', 'Experimental', 'Experimental'],
    'Presión Sistólica': [120, 130, 125, 135, 140, 145],
    'Presión Diastólica': [80, 85, 82, 90, 95, 92],
    'Colesterol': [150, 160, 155, 170, 175, 180]
}
df = pd.DataFrame(data)

# Creamos el boxplot sin colores personalizados
plt.figure(figsize=(8, 6))
df.boxplot(column=['Presión Sistólica', 'Presión Diastólica', 'Colesterol'], by='Grupo', notch=True, sym='o', showmeans=True)

# Añadimos títulos y etiquetas
plt.title('Boxplot de Parámetros de Salud por Grupo')
plt.xlabel('Grupo')
plt.ylabel('Valor')

# Mostramos la figura
plt.show()
