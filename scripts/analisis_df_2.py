# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 09:17:24 2024

@author: USUARIO
"""

import pandas as pd

# Cargar el archivo CSV en un DataFrame
df_peajes = pd.read_csv('peajes.csv', sep=';')

# Dividir el DataFrame en columnas categóricas y numéricas
categoricas = df_peajes[['TIPO', 'NOMBRE', 'CONCESION', 'GEN', 'SENTIDO', 'COD_VIA', 'DEP', 'CONCESIONA', 'INIC_OPER', 'ETIQUETA']]
numericas = df_peajes[['CAT1', 'CAT2', 'CAT3', 'CAT4', 'CAT5', 'CAT6', 'CAT7', 'longitud', 'latitud']]

def mostrar_info_categoricas():
    print("Información de las columnas categóricas:")
    print(categoricas.info())

def mostrar_info_numericas():
    print("\nInformación de las columnas numéricas:")
    print(numericas.info())

def mostrar_descripcion_categoricas():
    print("\nEstadísticas descriptivas de las columnas categóricas:")
    print(categoricas.describe())

def mostrar_descripcion_numericas():
    print("\nEstadísticas descriptivas de las columnas numéricas:")
    print(numericas.describe())

def mostrar_valores_unicos_concesion():
    if 'CONCESION' in categoricas.columns:
        print("\nValores únicos para la columna 'CONCESION':")
        print(categoricas['CONCESION'].unique())
    else:
        print("La columna 'CONCESION' no existe en el DataFrame.")

def mostrar_valores_unicos_sentido():
    if 'SENTIDO' in categoricas.columns:
        print("\nValores únicos para la columna 'SENTIDO':")
        print(categoricas['SENTIDO'].unique())
    else:
        print("La columna 'SENTIDO' no existe en el DataFrame.")

def mostrar_cantidad_valores_gen():
    if 'GEN' in categoricas.columns:
        print("\nCantidad de veces que aparece cada valor en la columna 'GEN':")
        print(categoricas['GEN'].value_counts())
    else:
        print("La columna 'GEN' no existe en el DataFrame.")

def mostrar_valores_columna():
    columna = input("\nIngrese el nombre de la columna específica: ")
    if columna in df_peajes.columns:
        print(f"\nValores únicos para la columna '{columna}':")
        print(df_peajes[columna].unique())
    else:
        print(f"La columna '{columna}' no existe en el DataFrame.")

# Menú de opciones
while True:
    print("\nMENU:")
    print("1. Mostrar información de las columnas categóricas")
    print("2. Mostrar información de las columnas numéricas")
    print("3. Mostrar estadísticas descriptivas de las columnas categóricas")
    print("4. Mostrar estadísticas descriptivas de las columnas numéricas")
    print("5. Mostrar valores únicos para la columna 'CONCESION'")
    print("6. Mostrar valores únicos para la columna 'SENTIDO'")
    print("7. Mostrar cantidad de veces que aparece cada valor en la columna 'GEN'")
    print("8. Mostrar valores de una columna específica")
    print("9. Salir")

    opcion = input("Seleccione una opción (1-9): ")

    if opcion == '1':
        mostrar_info_categoricas()
    elif opcion == '2':
        mostrar_info_numericas()
    elif opcion == '3':
        mostrar_descripcion_categoricas()
    elif opcion == '4':
        mostrar_descripcion_numericas()
    elif opcion == '5':
        mostrar_valores_unicos_concesion()
    elif opcion == '6':
        mostrar_valores_unicos_sentido()
    elif opcion == '7':
        mostrar_cantidad_valores_gen()
    elif opcion == '8':
        mostrar_valores_columna()
    elif opcion == '9':
        print("¡Hasta pronto!")
        break
    else:
        print("Opción inválida. Por favor seleccione una opción del 1 al 9.")

