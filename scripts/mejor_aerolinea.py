# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 18:13:13 2024

@author: USUARIO
"""

def mejor_aerolinea(vuelos):
    """
    Encuentra la mejor aerolínea basada en la puntualidad de los vuelos.

    Args:
    vuelos (dict): Diccionario de diccionarios con la información de los vuelos.

    Returns:
    str: El nombre de la mejor aerolínea (la que tenga menor retraso promedio).
    """
    # Diccionario para almacenar los totales de retraso por aerolínea y la cantidad de vuelos
    total_retraso_por_aerolinea = {}
    cantidad_vuelos_por_aerolinea = {}

    # Iterar sobre los vuelos
    for vuelo_id, info_vuelo in vuelos.items():
        aerolinea = info_vuelo['aerolinea']
        retraso = info_vuelo['retraso']

        # Agregar el retraso al total de retraso de la aerolínea
        if aerolinea in total_retraso_por_aerolinea:
            total_retraso_por_aerolinea[aerolinea] += retraso
            cantidad_vuelos_por_aerolinea[aerolinea] += 1
        else:
            total_retraso_por_aerolinea[aerolinea] = retraso
            cantidad_vuelos_por_aerolinea[aerolinea] = 1

    # Calcular el retraso promedio por aerolínea
    retraso_promedio_por_aerolinea = {}
    for aerolinea, total_retraso in total_retraso_por_aerolinea.items():
        cantidad_vuelos = cantidad_vuelos_por_aerolinea[aerolinea]
        retraso_promedio = total_retraso / cantidad_vuelos
        retraso_promedio_por_aerolinea[aerolinea] = retraso_promedio

    # Encontrar la aerolínea con el menor retraso promedio
    mejor_aerolinea = min(retraso_promedio_por_aerolinea, key=retraso_promedio_por_aerolinea.get)

    return mejor_aerolinea

# Ejemplo de uso
if __name__ == "__main__":
    # Ejemplo de diccionario de vuelos
    vuelos = {
        '001': {'aerolinea': 'Delta', 'retraso': 10},
        '002': {'aerolinea': 'American Airlines', 'retraso': 5},
        '003': {'aerolinea': 'United Airlines', 'retraso': 15},
        '004': {'aerolinea': 'Delta', 'retraso': 8},
        '005': {'aerolinea': 'American Airlines', 'retraso': 12}
    }

    # Encontrar la mejor aerolínea
    mejor = mejor_aerolinea(vuelos)
    print(f"La mejor aerolínea es: {mejor}")
