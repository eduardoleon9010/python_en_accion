"""
Comparador de tiempos y determinador del vuelo que llega más tarde.

Este script contiene dos funciones: `comparar_tiempos` y `vuelo_llega_mas_tarde`.
La función `comparar_tiempos` compara dos tiempos en formato HH:MM:SS y devuelve
1 si el primer tiempo es posterior al segundo, -1 si es anterior y 0 si son iguales.

La función `vuelo_llega_mas_tarde` determina, a partir de una lista de vuelos con
sus tiempos de salida, cuál de ellos tiene el horario de salida más tardío.

Ejemplo de uso:
vuelos = [{'tiempo_salida':'08:11:45','duracion':'2:54:20'},
          {'tiempo_salida':'11:48:10','duracion':'2:11:58'},
          {'tiempo_salida':'12:00:10','duracion':'0:50:15'},
          {'tiempo_salida':'14:55:10','duracion':'3:20:00'},
          {'tiempo_salida':'17:15:20','duracion':'4:05:11'}]
print(vuelo_llega_mas_tarde(vuelos))
"""

def comparar_tiempos(tiempo_1:str, tiempo_2:str) -> int:
    partes_1 = tiempo_1.split(":")
    partes_2 = tiempo_2.split(":")
    
    hora_1 = int(partes_1[0])
    minutos_1 = int(partes_1[1])
    segundos_1 = int(partes_1[2])
    
    hora_2= int(partes_2[0])
    minutos_2 = int(partes_2[1])
    segundos_2 = int(partes_2[2])
    
    comparar = 0
    
    if hora_1 > hora_2:
        comparar = 1
    elif hora_1 < hora_2:
        comparar = -1
    else:
        if minutos_1 > minutos_2:
            comparar = 1
        elif minutos_1 < minutos_2:
            comparar = -1
        else:
            if segundos_1 > segundos_2:
                comparar = 1
            elif segundos_1 < segundos_2:
                comparar = -1
    
    return comparar

def vuelo_llega_mas_tarde(vuelos:list) -> dict:
    pos_mas_tarde = 0
    llegada_mas_tarde = vuelos[0]['tiempo_salida']
    
    for i in range(0, len(vuelos)):
        tiempo = vuelos[i]['tiempo_salida']
        
        if comparar_tiempos(tiempo, llegada_mas_tarde) == 1:
            pos_mas_tarde = i
            llegada_mas_tarde = tiempo
            
    return vuelos[pos_mas_tarde]

vuelos = [{'tiempo_salida':'08:11:45','duracion':'2:54:20'},
          {'tiempo_salida':'11:48:10','duracion':'2:11:58'},
          {'tiempo_salida':'12:00:10','duracion':'0:50:15'},
          {'tiempo_salida':'14:55:10','duracion':'3:20:00'},
          {'tiempo_salida':'17:15:20','duracion':'4:05:11'}]

print(vuelo_llega_mas_tarde(vuelos))



    
    
    
    
    


    
