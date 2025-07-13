"""
Análisis de Datos de Peajes
Descripción
Este script utiliza la biblioteca Pandas en Python para cargar un archivo CSV que contiene información sobre peajes. 
Luego, realiza una serie de filtrados y manipulaciones en los datos para extraer información específica.

"""

import pandas as pd

# Cargar datos de peajes desde un archivo CSV
peajes = pd.read_csv("peajes.csv", sep=";")

# Filtrar peajes de Cundinamarca o Tolima
cundinamarca_tolima = peajes[(peajes['DEP'] == 'Cundinamarca') | (peajes['DEP'] =='Tolima')]
cundinamarca_tolima[['NOMBRE','DEP']]

# Filtrar peajes con tarifas de categoría 6 y 7 superiores a 50000
peajes_cat6y7_costosa = peajes[(peajes['CAT6'] > 50000) & (peajes['CAT7'] > 50000)]
peajes_cat6y7_costosa[['NOMBRE', 'CAT6', 'CAT7']]

# Filtrar peajes de Atlántico o Valle del Cauca
valle_atlantico = peajes[peajes['DEP'].isin(['Atlántico','Valle del Cauca'])]
valle_atlantico[['NOMBRE','DEP']]


"""
Uso y Funcionalidad
El código carga un archivo CSV llamado "peajes.csv", luego realiza tres filtrados diferentes:

Filtrado por Departamento: Extrae los peajes ubicados en Cundinamarca o Tolima y muestra el nombre del peaje y el 
departamento correspondiente.
Filtrado por Tarifas Costosas: Identifica los peajes con tarifas de categoría 6 y 7 superiores a 50000 y 
muestra el nombre del peaje, así como las tarifas de estas dos categorías.
Filtrado por Otros Departamentos: Extrae los peajes ubicados en Atlántico o Valle del Cauca y muestra el 
nombre del peaje y el departamento correspondiente.
Estos filtros permiten explorar y analizar específicamente ciertos peajes basados en criterios como ubicación 
geográfica y tarifas.
"""


