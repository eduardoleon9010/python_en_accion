# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 11:09:21 2024

@author: USUARIO
"""

import pandas as pd

# Cargar el archivo CSV
def cargar_csv():
    archivo = input("Introduce la ruta del archivo CSV: ")
    try:
        df = pd.read_csv(archivo)
        print("Archivo cargado exitosamente.")
        return df
    except FileNotFoundError:
        print("Archivo no encontrado.")
        return None

# Función para agrupar los datos por una columna
def agrupar_por_columna(df):
    columna = input("Introduce el nombre de la columna por la cual quieres agrupar: ")
    try:
        grupos = df.groupby(columna)
        print("DataFrames agrupados correctamente.")
        return grupos
    except KeyError:
        print("La columna especificada no existe en el DataFrame.")
        return None

# Función para mostrar la cantidad de registros en cada grupo
def mostrar_cantidad_por_grupo(grupos):
    for nombre_grupo, grupo in grupos:
        print(f"Grupo: {nombre_grupo}, Cantidad de Registros: {len(grupo)}")

# Función para obtener un grupo específico
def obtener_grupo(grupos):
    nombre_grupo = input("Introduce el nombre del grupo que deseas obtener: ")
    try:
        grupo = grupos.get_group(nombre_grupo)
        print("Grupo obtenido correctamente.")
        return grupo
    except KeyError:
        print("El grupo especificado no existe en los grupos agrupados.")
        return None

# Función para realizar operaciones de agregación en los grupos
def operaciones_agregacion(grupos):
    operacion = input("Introduce la operación de agregación que deseas realizar (mean, count, sum, describe): ")
    try:
        if operacion == "mean":
            print(grupos.mean())
        elif operacion == "count":
            print(grupos.count())
        elif operacion == "sum":
            print(grupos.sum())
        elif operacion == "describe":
            print(grupos.describe())
        else:
            print("Operación no válida.")
    except AttributeError:
        print("Operación no válida para los grupos agrupados.")

# Menú principal
def menu():
    df = None
    grupos = None
    while True:
        print("\nMenu:")
        print("1. Cargar archivo CSV")
        print("2. Agrupar datos por una columna")
        print("3. Mostrar cantidad de registros por grupo")
        print("4. Obtener un grupo específico")
        print("5. Realizar operaciones de agregación en los grupos")
        print("6. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            df = cargar_csv()
        elif opcion == "2":
            if df is not None:
                grupos = agrupar_por_columna(df)
            else:
                print("Primero debes cargar un archivo CSV.")
        elif opcion == "3":
            if grupos is not None:
                mostrar_cantidad_por_grupo(grupos)
            else:
                print("Primero debes agrupar los datos.")
        elif opcion == "4":
            if grupos is not None:
                obtener_grupo(grupos)
            else:
                print("Primero debes agrupar los datos.")
        elif opcion == "5":
            if grupos is not None:
                operaciones_agregacion(grupos)
            else:
                print("Primero debes agrupar los datos.")
        elif opcion == "6":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")

# Ejecutar el menú
menu()
