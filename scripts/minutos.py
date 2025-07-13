"""
Este ejercicio solicita al usuario ingresar una cantidad de días. 
Luego, realiza una serie de cálculos para convertir esa cantidad 
de días a horas, minutos y segundos.

Calcula las horas multiplicando la cantidad de días ingresados por 24 (horas en un día).
Convierte las horas a minutos multiplicando el total de horas por 60 (minutos en una hora).
Finalmente, transforma los minutos a segundos multiplicando la cantidad de minutos por 60 (segundos en un minuto).
El programa muestra cada resultado de conversión, informando las horas, minutos y segundos 
equivalentes a la cantidad de días ingresados por el usuario.
"""

print('Introduzca los dias: ')
dias = int(input())

hora = dias * 24
print('Horas: ' + str(hora))

minutos = hora * 60 

print('Minutos: ' + str(minutos))

segundos = minutos * 60
print('Segundos: ' + str(segundos))
