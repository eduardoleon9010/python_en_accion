# -*- coding: utf-8 -*-
def calcular_hora_llegada(hora_salida:int, minutos_salida:int,
                          seg_salida:int, horas_duracion:int,
                          minutos_duracion:int, seg_duracion:int)->str:
    
    hora = 0
    minutos = 0
    segundos = 0
    
    segundos = seg_salida+seg_duracion
    
    if segundos >= 60:
        segundos -= 60
        minutos += 1
        
    suma_minutos = minutos_salida + minutos_duracion
    
    minutos += suma_minutos 
    
    if minutos >= 60:
        minutos -= 60
        hora += 1
        
    suma_horas = hora_salida + horas_duracion
    hora += suma_horas
    
    return '{0:0>2d}:{1:0>2d}:{2:>02d}'.format(hora, minutos, segundos)

#print(calcular_hora_llegada(11,48,10,2,11,58))
    
def hora_llegada_vuelos(info_vuelos:list)->list:
     llegadas = []
    
     for vuelo in info_vuelos:
        salida = vuelo['tiempo_salida']
        duracion = vuelo['duracion']
        
        partes_salida = salida.split(":")
        partes_duracion = duracion.split(":")
        
        partes_salida = salida.split(":")
        hora_salida = int(partes_salida[0])
        minutos_salida = int(partes_salida[1])
        segundos_salida = int(partes_salida[2])
        partes_duracion = duracion.split(":")
        hora_duracion = int(partes_duracion[0])
        minutos_duracion = int(partes_duracion[1])
        segundos_duracion = int(partes_duracion[2])
        
        tiempo_llegada = calcular_hora_llegada(hora_salida, minutos_salida, segundos_salida, 
                                               hora_duracion, minutos_duracion, segundos_duracion)
        
        dic_llegada = {"tiempo_llegada":tiempo_llegada}
        llegadas.append(dic_llegada)
        
        
     return llegadas
        
vuelos = [{'tiempo_salida':'08:11:45','duracion':'2:54:20'},
          {'tiempo_salida':'11:48:10','duracion':'2:11:58'},
          {'tiempo_salida':'12:00:10','duracion':'0:50:15'},
          {'tiempo_salida':'14:55:10','duracion':'3:20:00'},
          {'tiempo_salida':'17:15:20','duracion':'4:05:11'}]

print(hora_llegada_vuelos(vuelos))
    
    
    
    
    