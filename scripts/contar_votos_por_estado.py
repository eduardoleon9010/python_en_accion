# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 20:29:14 2024

@author: USUARIO
"""

import random

def contar_votos_por_estado(votos, estado):
    """
    Cuenta los votos recibidos por cada candidato en un estado específico.

    Args:
        votos (list): Lista de tuplas representando los votos.
        estado (str): Nombre del estado del cual se contabilizarán los votos.

    Returns:
        tuple: Una tupla con la cantidad de votos recibidos por cada candidato en el estado.
    """
    # Inicializar contadores de votos para cada candidato
    votos_trump = 0
    votos_biden = 0
    
    # Recorrer la lista de votos
    for voto_actual in votos:
        # Desempaquetar la tupla de voto_actual
        _, candidato, estado_voto, _ = voto_actual
        
        # Verificar si el voto es del estado de interés
        if estado_voto == estado:
            # Contabilizar el voto al candidato correspondiente
            if candidato == 'Trump':
                votos_trump += 1
            elif candidato == 'Biden':
                votos_biden += 1
    
    # Retornar una tupla con la cantidad de votos de Trump y Biden en el estado
    return (votos_trump, votos_biden)

def contar_votos_por_estado_en_todo_el_pais(votos, estados):
    """
    Calcula los votos recibidos por cada candidato en cada uno de los 50 estados del país.

    Args:
        votos (list): Lista de tuplas representando los votos.
        estados (tuple): Tupla con los nombres de los 50 estados.

    Returns:
        dict: Un diccionario donde las llaves son los nombres de los estados y los valores son tuplas
        con la cantidad de votos recibidos por cada candidato en el estado.
    """
    # Inicializar el diccionario para almacenar los votos por estado
    votos_por_estado = {}
    
    # Recorrer la tupla de estados
    for estado_actual in estados:
        # Contabilizar los votos para el estado actual
        total_de_su_estado = contar_votos_por_estado(votos, estado_actual)
        
        # Agregar los votos al diccionario
        votos_por_estado[estado_actual] = total_de_su_estado
    
    # Retornar el diccionario con los votos por estado
    return votos_por_estado

# Generar algunos votos de ejemplo para cada estado
# Suponemos que hay 50 estados en la lista de estados
estados = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", 
           "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", 
           "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", 
           "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", 
           "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]

# Programa Principal. Generar votos aleatorios para cada estado
votos = []
for estado in estados:
    for _ in range(random.randint(100, 1000)):  # Generar entre 100 y 1000 votos por estado
        voto = (random.randint(1, 100000), random.choice(['Trump', 'Biden']), estado, random.choice(['Condado 1', 'Condado 2']))
        votos.append(voto)

# Contar los votos por estado en todo el país
resultados = contar_votos_por_estado_en_todo_el_pais(votos, estados)

# Imprimir los resultados
for estado, votos_estado in resultados.items():
    print(f"Resultados en {estado}:")
    print(f"Votos para Trump: {votos_estado[0]}")
    print(f"Votos para Biden: {votos_estado[1]}")
    print()  # Salto de línea entre estados
