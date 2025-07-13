"""
Este script se encarga de contar los votos para cada candidato (Donald Trump y Joe Biden) en una 
lista de votos por estado. 

Este script hace uso de dos funciones:
contar_votos_estado: Cuenta los votos para Trump y Biden en un estado específico.
contar_total_votos_por_estado: Calcula el total de votos para ambos candidatos en todos los estados.
"""

def contar_votos_estado(votos: list, estado_interes: str) -> tuple:
    """
    Cuenta los votos para cada candidato en un estado específico.

    Parámetros:
    votos (list): Lista de tuplas de votos, cada una con (id_voto, candidato, estado, condado).
    estado_interes (str): El estado del cual se quieren contar los votos.

    Retorna:
    tuple: Tupla con la cantidad de votos para Trump y Biden en el estado de interés.
    """
    cant_votos_trump = 0
    cant_votos_biden = 0
    
    for voto_actual in votos:
       id_voto, candidato, estado, condado = voto_actual
       
       if estado == estado_interes:
           if candidato == "Donald Trump":
               cant_votos_trump += 1
           else:
               cant_votos_biden += 1
               
    return (cant_votos_trump, cant_votos_biden)


def contar_total_votos_por_estado(votos: list, estados: tuple) -> dict:
    """
    Cuenta el total de votos por estado para ambos candidatos.

    Parámetros:
    votos (list): Lista de tuplas de votos, cada una con (id_voto, candidato, estado, condado).
    estados (tuple): Tupla de nombres de estados.

    Retorna:
    dict: Diccionario con el total de votos para Trump y Biden en cada estado.
    """
    totales_estado = {}
    for estado_actual in estados:
        votos_estado_actual = contar_votos_estado(votos, estado_actual)
        totales_estado[estado_actual] = votos_estado_actual
        
    return totales_estado


import random
# Lista de estados
estados = ('Alaska','Alabama', 'Arkansas', 'Arizona', 'California', 'Colorado', 'Connecticut', 'District of Columbia', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Iowa', 'Idaho', 'Illinois', 'Indiana', 'Kansas', 'Kentucky', 'Lousiana', 'Massachusetts', 'Maryland', 'Maine', 'Michigan', 'Minnesota', 'Missouri', 'Mississippi', 'Montana', 'Nort Carolina', 'Nort Dackota', 'Nebraska', 'New Hampshire', 'New Jersey', 'New Mexico', 'Nevada', 'New York', 'Ohio', 'Oklahoma', 'Oregon', 'Pensilvania', 'Rhode Island', 'Soud Carolina', 'Sout Dakota', 'Tennessee', 'Texas', 'Utah', 'Virginia', 'Vermont', 'Washington', 'Wisconsin', 'West Virginia', 'Wyming')


# Generación de datos de votos aleatorios para cada estado
votos = []
for est in estados:
    cant_votos = random.randint(4000, 8000)
    for i in range(cant_votos):
        elegido = random.randint(0,1)
        candidato = "Donald Trump"
        if elegido == 1:
            candidato = "Joe Biden"
        id_voto = est+str(i)
        voto = (id_voto, candidato, est, "Some Country")
        votos.append(voto)
        
# Cálculo del total de votos por estado para cada candidato
cuenta = contar_total_votos_por_estado(votos, estados)

# Imprimir los totales de votos por estado
for estado in cuenta:
    print(estado, "\nTOTAL ->", "Trump: "+str(cuenta[estado][0]), 
          "Biden: "+str(cuenta[estado][1])+"\n")
        
        
        
        
        
