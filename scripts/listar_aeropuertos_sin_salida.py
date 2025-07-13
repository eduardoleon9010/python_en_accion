# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 22:24:11 2024

@author: USUARIO
"""

def listar_aeropuertos_sin_salida(vuelos: dict) -> list:
    # Conjunto para almacenar los códigos de aeropuertos con vuelos de salida
    aeropuertos_con_salida = set()
    
    # Recorrer todos los vuelos y agregar los códigos de origen al conjunto
    for vuelo in vuelos.values():
        aeropuertos_con_salida.add(vuelo['origen'])
    
    # Lista para almacenar los códigos de aeropuertos sin vuelos de salida
    aeropuertos_sin_salida = []
    
    # Recorrer nuevamente los vuelos y verificar si el destino no está en los aeropuertos con salida
    for vuelo in vuelos.values():
        if vuelo['destino'] not in aeropuertos_con_salida:
            aeropuertos_sin_salida.append(vuelo['destino'])
    
    # Eliminar duplicados y ordenar alfabéticamente la lista de aeropuertos sin salida
    aeropuertos_sin_salida = sorted(set(aeropuertos_sin_salida))
    
    return aeropuertos_sin_salida

# Ejemplo de uso con un diccionario de vuelos de muestra
vuelos_muestra = {
    'V1': {'aerolínea': 'Aerolínea A', 'origen': 'ATL', 'destino': 'LAX', 'distancia': 1500, 'retraso': 0, 'duracion': 180, 'salida': 800},
    'V2': {'aerolínea': 'Aerolínea B', 'origen': 'LAX', 'destino': 'JFK', 'distancia': 2500, 'retraso': 30, 'duracion': 240, 'salida': 1000},
    'V3': {'aerolínea': 'Aerolínea C', 'origen': 'DFW', 'destino': 'ORD', 'distancia': 800, 'retraso': 15, 'duracion': 120, 'salida': 930},
    'V4': {'aerolínea': 'Aerolínea D', 'origen': 'ORD', 'destino': 'MIA', 'distancia': 1200, 'retraso': 0, 'duracion': 150, 'salida': 1100},
    'V5': {'aerolínea': 'Aerolínea E', 'origen': 'JFK', 'destino': 'SFO', 'distancia': 2800, 'retraso': 45, 'duracion': 270, 'salida': 1200}
}

# Obtener la lista de aeropuertos sin salida
aeropuertos_sin_salida = listar_aeropuertos_sin_salida(vuelos_muestra)

# Imprimir el resultado
print("Aeropuertos sin vuelos de salida:")
print(aeropuertos_sin_salida)

