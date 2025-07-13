# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 10:18:29 2024

@author: USUARIO
"""

import pandas as pd
from math import radians, sin, cos, sqrt, atan2

# Cargar el archivo CSV en un DataFrame
peajes = pd.read_csv('peajes.csv', sep=';')

# Función para calcular la distancia entre dos puntos en la Tierra
def calcular_distancia(lat1, lon1, lat2, lon2):
    # Radio de la Tierra en kilómetros
    R = 6371.0

    # Convertir coordenadas de grados a radianes
    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    # Diferencia de latitud y longitud
    dlon = lon2 - lon1
    dlat = lat2 - lat1

    # Fórmula de Haversine para calcular la distancia
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    # Distancia entre los dos puntos
    distancia = R * c

    return distancia

# Función para agregar columnas calculadas de peaje más cercano y distancia
def agregar_columnas_calculadas(df):
    # Listas para almacenar las distancias y nombres de peajes más cercanos
    distancias = []
    peajes_cercanos = []

    # Recorrido para calcular el peaje más cercano y su distancia
    for i, peaje_actual in df.iterrows():
        distancia_minima = float('inf')
        peaje_cercano = ''

        for j, otro_peaje in df.iterrows():
            if i != j:  # Evitar comparar el mismo peaje
                distancia = calcular_distancia(peaje_actual['latitud'], peaje_actual['longitud'], otro_peaje['latitud'], otro_peaje['longitud'])
                if distancia < distancia_minima:
                    distancia_minima = distancia
                    peaje_cercano = otro_peaje['NOMBRE']

        distancias.append(distancia_minima)
        peajes_cercanos.append(peaje_cercano)

    # Agregar las nuevas columnas al DataFrame
    df['Peaje Más Cercano'] = peajes_cercanos
    df['Distancia al Peaje Más Cercano (km)'] = distancias

# Función para mostrar el menú y ejecutar las opciones
def mostrar_menu():
    while True:
        print("\nMENU:")
        print("1. Mostrar peajes en Cundinamarca o Tolima")
        print("2. Mostrar peajes con tarifas altas (CAT6 o CAT7 > 50,000)")
        print("3. Mostrar peajes en Atlántico o Valle del Cauca")
        print("4. Agregar columnas calculadas de peaje más cercano y distancia")
        print("5. Salir")

        opcion = input("Seleccione una opción (1-5): ")

        if opcion == '1':
            mostrar_peajes_cundinamarca_tolima()
        elif opcion == '2':
            mostrar_tarifas_altas()
        elif opcion == '3':
            mostrar_peajes_atlantico_valle_cauca()
        elif opcion == '4':
            agregar_columnas_calculadas(peajes)
            print("Se han agregado las columnas calculadas.")
        elif opcion == '5':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

# Funciones para mostrar los resultados de los filtros
def mostrar_peajes_cundinamarca_tolima():
    peajes_cundinamarca_tolima = peajes[(peajes['DEP'] == 'Cundinamarca') | (peajes['DEP'] == 'Tolima')]
    print("Peajes en Cundinamarca o Tolima:")
    print(peajes_cundinamarca_tolima[['NOMBRE', 'DEP']])

def mostrar_tarifas_altas():
    tarifas_altas = peajes[(peajes['CAT6'] > 50000) & (peajes['CAT7'] > 50000)]
    print("Peajes con tarifas altas (CAT6 o CAT7 > 50,000):")
    print(tarifas_altas[['NOMBRE', 'CAT6', 'CAT7']])

def mostrar_peajes_atlantico_valle_cauca():
    peajes_atlantico_valle_cauca = peajes[peajes['DEP'].isin(['Atlántico', 'Valle del Cauca'])]
    print("Peajes en Atlántico o Valle del Cauca:")
    print(peajes_atlantico_valle_cauca[['NOMBRE', 'DEP']])

# Función para agregar columnas calculadas de peaje más cercano y distancia
def agregar_columnas_calculadas(df):
    # Listas para almacenar las distancias y nombres de peajes más cercanos
    distancias = []
    peajes_cercanos = []

    # Recorrido para calcular el peaje más cercano y su distancia
    for i, peaje_actual in df.iterrows():
        distancia_minima = float('inf')
        peaje_cercano = ''

        for j, otro_peaje in df.iterrows():
            if i != j:  # Evitar comparar el mismo peaje
                distancia = calcular_distancia(peaje_actual['latitud'], peaje_actual['longitud'], otro_peaje['latitud'], otro_peaje['longitud'])
                if distancia < distancia_minima:
                    distancia_minima = distancia
                    peaje_cercano = otro_peaje['NOMBRE']

        distancias.append(distancia_minima)
        peajes_cercanos.append(peaje_cercano)

    # Agregar las nuevas columnas al DataFrame
    df['Peaje Más Cercano'] = peajes_cercanos
    df['Distancia al Peaje Más Cercano (km)'] = distancias

# Programa principal para probar la función de agregar columnas calculadas
def programa_principal():
    # Agregar las columnas calculadas al dataframe 'peajes'
    agregar_columnas_calculadas(peajes)

    # Mostrar nombre, peaje más cercano y distancia al mismo de cinco peajes ubicados en Cundinamarca (posiciones 5 a 10)
    print("\nNombre, peaje más cercano y distancia al mismo de cinco peajes ubicados en Cundinamarca:")
    print(peajes.loc[5:10, ['NOMBRE', 'Peaje Más Cercano', 'Distancia al Peaje Más Cercano (km)']])

# Ejecutar el programa principal
programa_principal()

# Ejecutar el menú
mostrar_menu()
