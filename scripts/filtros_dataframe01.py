"""
Cálculo del Peaje más Cercano
Descripción
Este script utiliza la biblioteca Pandas en Python para cargar un archivo CSV que contiene información sobre peajes. 
Luego, realiza un cálculo para determinar el peaje más cercano a cada uno de los peajes existentes en la base de 
datos en términos de distancia geográfica.
"""

import pandas as pd
import math

# Cargar datos de peajes desde un archivo CSV
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
        
    peajes['MAS_CERCANO'] = cercanos
    peajes['DIST_MAS_CERCA'] = distancias
    
def calcular_distancia_tierra(t1:float, g1:float, t2:float, g2:float)->float:
    t1_rad = math.radians(t1)
    g1_rad = math.radians(g1)
    t2_rad = math.radians(t2)
    g2_rad = math.radians(g2)
    dist = 6371.01 * math.acos(math.sin(t1_rad) * math.sin(t2_rad) + math.cos(t1_rad) * math.cos(t2_rad) * math.cos(g1_rad - g2_rad))
    return round(dist, 2)

# Calcular el peaje más cercano para cada peaje
calcular_peaje_cercano(peajes)

# Filtrar peajes de Cundinamarca y mostrar algunos resultados
filtro = peajes[peajes['DEP'] == 'Cundinamarca']
print(filtro[['NOMBRE', 'MAS_CERCANO', 'DIST_MAS_CERCA']].iloc[5:10])


"""
Uso y Funcionalidad
El código calcula el peaje más cercano para cada peaje en la base de datos. Para ello, emplea una fórmula de 
cálculo de distancia geográfica entre puntos en la superficie terrestre. Luego, muestra información específica 
sobre peajes ubicados en Cundinamarca, incluyendo el nombre del peaje más cercano y la distancia a este peaje cercano.

Este proceso es útil para analizar la ubicación de los peajes y entender su proximidad geográfica con respecto 
a otros peajes en la base de datos.
"""
                
                
