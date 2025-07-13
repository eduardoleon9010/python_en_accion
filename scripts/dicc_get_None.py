# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 08:50:33 2024

@author: USUARIO
"""

# Solicitar información del estudiante por consola
nombre = input("Ingrese el nombre del estudiante: ")
edad = int(input("Ingrese la edad del estudiante: "))
carrera = input("Ingrese la carrera del estudiante: ")

# Crear un diccionario de información de un estudiante con los datos ingresados
estudiante = {
    'nombre': nombre,
    'edad': edad,
    'carrera': carrera,
    'notas': {'matematicas': 90, 'historia': 75, 'programacion': 95}
}

# Intentar obtener la información de una llave que no existe usando get
genero = estudiante.get('genero', None)

# Verificar si la llave 'genero' estaba presente
if genero is None:
    print("La llave 'genero' no estaba presente en el diccionario.")
else:
    print(f"El valor de 'genero' es: {genero}")
