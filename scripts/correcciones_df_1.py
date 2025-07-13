# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 10:59:45 2024

@author: USUARIO
"""
import pandas as pd

# Función para cargar el archivo CSV
def cargar_csv():
    archivo = input("Introduce la ruta del archivo CSV: ")
    try:
        df = pd.read_csv(archivo, delimiter=';')
        print("Archivo cargado exitosamente.")
        return df
    except FileNotFoundError:
        print("Archivo no encontrado.")
        return None

# Función para mostrar las primeras filas del DataFrame
def mostrar_primeras_filas(df):
    print(df.head())

# Función para mostrar información sobre el DataFrame
def mostrar_info(df):
    print(df.info())

# Función para llenar valores nulos en el DataFrame
def llenar_valores_nulos(df):
    columna = input("Introduce el nombre de la columna con valores nulos: ")
    valor = input("Introduce el valor con el que deseas llenar los nulos: ")
    df[columna].fillna(valor, inplace=True)
    print("Valores nulos llenados correctamente.")

# Función para convertir una columna a tipo datetime
def convertir_a_datetime(df):
    columna = input("Introduce el nombre de la columna que deseas convertir a datetime: ")
    try:
        df[columna] = pd.to_datetime(df[columna], infer_datetime_format=True)
        print("Columna convertida a tipo datetime correctamente.")
    except KeyError:
        print("La columna especificada no existe en el DataFrame.")

# Menú principal
def menu():
    df = None
    while True:
        print("\nMenu:")
        print("1. Cargar archivo CSV")
        print("2. Mostrar las primeras filas del DataFrame")
        print("3. Mostrar información sobre el DataFrame")
        print("4. Llenar valores nulos en una columna")
        print("5. Convertir una columna a tipo datetime")
        print("6. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            df = cargar_csv()
        elif opcion == "2":
            if df is not None:
                mostrar_primeras_filas(df)
            else:
                print("Primero debes cargar un archivo CSV.")
        elif opcion == "3":
            if df is not None:
                mostrar_info(df)
            else:
                print("Primero debes cargar un archivo CSV.")
        elif opcion == "4":
            if df is not None:
                llenar_valores_nulos(df)
            else:
                print("Primero debes cargar un archivo CSV.")
        elif opcion == "5":
            if df is not None:
                convertir_a_datetime(df)
            else:
                print("Primero debes cargar un archivo CSV.")
        elif opcion == "6":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")

# Ejecutar el menú
menu()
