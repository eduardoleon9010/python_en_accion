
"""
Este script usa la biblioteca Pandas para leer datos de un archivo CSV ("peajes.csv") 
y luego ejecuta una función calcular_peaje_cercano. Esta función calcula la distancia 
más corta entre los diferentes peajes basándose en sus coordenadas de latitud y longitud.

Importación de librerías y carga de datos:

Se importa Pandas y la librería math.
El archivo CSV "peajes.csv" se carga en un DataFrame llamado peajes utilizando pd.read_csv.
Función calcular_peaje_cercano:

Toma un DataFrame de peajes como entrada y calcula la distancia más cercana entre cada ubicación de peaje y los otros peajes.
Itera a través de cada fila en el DataFrame y, para cada peaje, calcula la distancia a todos los demás peajes.
Utiliza la fórmula de la distancia entre dos puntos en la superficie de la Tierra para calcular la distancia 
entre dos coordenadas geográficas.
Registra el peaje más cercano y la distancia más corta a ese peaje en dos listas: cercanos y distancias.
Función calcular_distancia_tierra:

Toma como entrada las coordenadas de latitud y longitud de dos ubicaciones y calcula la distancia entre ellas 
utilizando la fórmula de la distancia en la superficie de la Tierra.
Llamada a la función calcular_peaje_cercano:

Ejecuta la función calcular_peaje_cercano con el DataFrame peajes como argumento.

Filtrado y visualización de datos:

Filtra los datos para mostrar solo aquellos que pertenecen al departamento de "Cundinamarca".
Imprime las columnas 'NOMBRE', 'MAS_CERCANO' y 'DIST_MAS_CERCA' para las filas 5 a 9 de los peajes que pertenecen 
a "Cundinamarca".
En resumen, este código calcula la distancia más corta entre los peajes y luego filtra y muestra información 
específica sobre los peajes ubicados en el departamento de Cundinamarca y sus peajes más cercanos junto con las 
distancias correspondientes.
"""

import pandas as pd
import math

peajes = pd.read_csv("peajes.csv", sep=";")

def calcular_peaje_cercano(peajes:pd.DataFrame)->None:
    distancias = []
    cercanos = []
    for i in range(peajes.shape[0]):
        actual = peajes.iloc[i]
        min_distancia = float('inf')
        mas_cerca =""
        for j in range(peajes.shape[0]):
            if i !=j:
                otro = peajes.iloc[j]
                dist = calcular_distancia_tierra(actual['latitud'],
                                                 actual['longitud'],
                                                 otro['latitud'],
                                                 otro['longitud'])
                if dist < min_distancia:
                    min_distancia = dist
                    mas_cerca = otro['NOMBRE']
                    
        distancias.append(min_distancia)
        cercanos.append(mas_cerca)
    print(len(cercanos))
    peajes['MAS_CERCANO'] = distancias
    peajes['DIST_MAS_CERCA'] = distancias
    
def calcular_distancia_tierra(t1:float, g1:float, t2:float, g2:float)->float:
    t1_rad = math.radians(t1)
    g1_rad = math.radians(g1)
    t2_rad = math.radians(t2)
    g2_rad = math.radians(g2)
    dist = 6371.01 * math.acos(math.sin(t1_rad) * math.sin(t2_rad) + math.cos(t1_rad) * math.cos(t2_rad) * math.cos(g1_rad - g2_rad))
    return round(dist, 2)

calcular_peaje_cercano(peajes)
filtro = peajes[peajes['DEP'] == 'Cundinamarca']
print(filtro[['NOMBRE', 'MAS_CERCANO', 'DIST_MAS_CERCA']].iloc[5:10])




                
                
