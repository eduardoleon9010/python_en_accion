# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 22:19:59 2024

@author: USUARIO
"""

# Crear un diccionario de información de un estudiante
estudiante = {
    'nombre': 'Juan',                    # Clave 'nombre' con valor 'Juan'
    'edad': 20,                          # Clave 'edad' con valor 20
    'carrera': 'Ingeniería',             # Clave 'carrera' con valor 'Ingeniería'
    'notas': {'matematicas': 90, 'historia': 75, 'programacion': 95}  # Clave 'notas' con un diccionario anidado
}

# Acceder a valores mediante claves
print("Nombre:", estudiante['nombre'])                 # Imprime el valor asociado a la clave 'nombre'
print("Edad:", estudiante['edad'])                     # Imprime el valor asociado a la clave 'edad'
print("Notas de Matemáticas:", estudiante['notas']['matematicas'])  # Imprime el valor asociado a la clave 'matematicas' dentro del diccionario 'notas'

# Modificar un valor
estudiante['edad'] = 21                                # Modifica el valor asociado a la clave 'edad'

# Agregar nueva información
estudiante['genero'] = 'Masculino'                     # Agrega una nueva clave 'genero' con valor 'Masculino'

# Eliminar una entrada
del estudiante['notas']['historia']                    # Elimina la clave 'historia' dentro del diccionario 'notas'

# Imprimir el diccionario actualizado
print(estudiante)                                      # Imprime el diccionario actualizado
