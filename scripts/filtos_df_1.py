# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 10:06:48 2024

@author: USUARIO
"""

import pandas as pd

# Cargar el archivo CSV en un DataFrame
df_contratos = pd.read_csv('SECOP_II_-_Contratos_Electr_nicos.csv')

# Función para ordenar los contratos por estado
def ordenar_contratos_por_estado():
    # Crear un nuevo DataFrame ordenado por el estado del contrato
    df_contratos_ordenados = df_contratos.sort_values(by='Estado Contrato')
    return df_contratos_ordenados

# Función para mostrar información de los contratos activos
def mostrar_contratos_activos():
    # Obtener los contratos activos del DataFrame ordenado
    df_activos = df_contratos_ordenados[df_contratos_ordenados['Estado Contrato'] == 'Activo']
    print("Contratos Activos:")
    print(df_activos)

# Función para mostrar información de los contratos en borrador
def mostrar_contratos_borrador():
    # Obtener los contratos en borrador del DataFrame ordenado
    df_borrador = df_contratos_ordenados[df_contratos_ordenados['Estado Contrato'] == 'Borrador']
    print("\nContratos en Borrador:")
    print(df_borrador)

# Función para mostrar información de los contratos terminados
def mostrar_contratos_terminados():
    # Obtener los contratos terminados del DataFrame ordenado
    df_terminados = df_contratos_ordenados[df_contratos_ordenados['Estado Contrato'] == 'Terminado']
    print("\nContratos Terminados:")
    print(df_terminados)

# Función para mostrar el menú de opciones
def mostrar_menu():
    print("\nMENU:")
    print("1. Mostrar información de los contratos activos")
    print("2. Mostrar información de los contratos en borrador")
    print("3. Mostrar información de los contratos terminados")
    print("4. Salir")

# Ordenar los contratos por estado
df_contratos_ordenados = ordenar_contratos_por_estado()

# Mostrar el menú y procesar la selección del usuario
while True:
    mostrar_menu()
    opcion = input("Seleccione una opción (1-4): ")

    if opcion == '1':
        mostrar_contratos_activos()
    elif opcion == '2':
        mostrar_contratos_borrador()
    elif opcion == '3':
        mostrar_contratos_terminados()
    elif opcion == '4':
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
