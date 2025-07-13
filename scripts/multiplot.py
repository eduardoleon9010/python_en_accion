"""
Este código en Python utiliza Pandas y Matplotlib para generar múltiples gráficos de dispersión 
a partir de un conjunto de datos cargado desde un archivo CSV ('peajes.csv'). Los gráficos 
muestran relaciones entre las columnas 'CAT1', 'CAT2', 'CAT3' y 'CAT4' para la región 
'Cundinamarca'. Cada gráfico está representado por un color diferente para facilitar la 
comparación visual de los datos.
"""


import pandas as pd
import matplotlib.pyplot as plt

# Carga de datos desde un archivo CSV
peajes = pd.read_csv('peajes.csv', sep=";")

# Reemplazo de valores en la columna 'DEP'
peajes['DEP'] = peajes['DEP'].replace(to_replace="<Null>", value='Otro')
peajes['DEP'] = peajes['DEP'].replace(to_replace="ANTIQUIA", value='Antioquia')

# Multiplots
# Creación de múltiples gráficos de dispersión para comparar datos
primera = peajes[peajes['DEP'] == 'Cundinamarca'].plot(
    kind='scatter', x='CAT1', y='CAT2', color='DarkBlue', label='1 a 2', figsize=(10, 6)
)
segunda = peajes[peajes['DEP'] == 'Cundinamarca'].plot(
    kind='scatter', x='CAT1', y='CAT3', color='DarkGreen', label='1 a 3',
    ax=primera, figsize=(10, 6)
)
tercera = peajes[peajes['DEP'] == 'Cundinamarca'].plot(
    kind='scatter', x='CAT1', y='CAT4', color='DarkRed', label='1 a 4',
    ax=primera, figsize=(10, 6)
)
plt.show()







