"""
Este código en Python realiza lo siguiente:

Función buscar_estudiante:

Recibe cuatro diccionarios que representan información de diferentes estudiantes y el nombre de un estudiante a buscar.
Comprueba si el nombre buscado está presente en alguno de los diccionarios proporcionados y retorna el diccionario 
completo del estudiante si lo encuentra. Si no lo encuentra, retorna None.
Programa principal:

Define cuatro diccionarios, cada uno representando la información de un estudiante (nombre, código, género, carrera, 
promedio, etc.).
Solicita al usuario ingresar el nombre de un estudiante.
Utiliza la función buscar_estudiante con los diccionarios de los estudiantes y el nombre ingresado para buscar al estudiante.
Si el estudiante existe, muestra su código; si no existe, imprime un mensaje indicando que el estudiante no está en 
el sistema.
Este código permite buscar información de un estudiante en particular a partir de su nombre, usando 
diccionarios que contienen los detalles de varios estudiantes.
"""

# -*- coding: utf-8 -*-
def buscar_estudiante(est1:dict,est2:dict,est3:dict,est4:dict,nom:str)->dict:
    buscado = None
    
    if est1['nombre'] == nom:
        buscado = est1
    elif  est2['nombre'] == nom:
        buscado = est2
    elif  est3['nombre'] == nom:
            buscado = est3
    elif  est4['nombre'] == nom:
            buscado = est4
            
    return buscado

#PROGRAMA PRINCIPAL 
e_1 = {'nombre':'Lina', 'codigo':'2020101234', 'genero':'femenino',
               'carrera':'Sistemas', 'promedio':4.78, 'ssc':2}
e_2 = {'nombre':'Laura', 'codigo':'2020105678', 'genero':'femenino',
               'carrera':'Civil', 'promedio':4.21, 'ssc':2}
e_3 = {'nombre':'Felipe', 'codigo':'2020109012', 'genero':'masculino',
               'carrera':'Sistemas', 'promedio':4.9, 'ssc':2}
e_4 = {'nombre':'Carlos', 'codigo':'2020103456', 'genero':'masculino',
               'carrera':'Economia', 'promedio':3.89, 'ssc':2}

nombre = input("Ingrese el nombre del estudiante a buscar: ")

est_buscado = buscar_estudiante(e_1,e_2,e_3,e_4,nombre)

if est_buscado is None:
    print("El estudiante No existe")
else:
    print("El estudiante existe y su codigo es "+est_buscado['codigo'])
