# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 15:39:55 2024

@author: USUARIO
"""

def contar_estudiantes(cursos: dict, horario_consultado: tuple) -> list:
    """
    Recibe información sobre los cursos y un horario consultado y devuelve la cantidad de estudiantes por edificio
    en el horario consultado.

    Args:
        cursos (dict): Un diccionario donde las llaves son los nombres de los cursos y los valores son diccionarios
        con las llaves 'inscritos', 'horario' y 'ubicacion'.
        horario_consultado (tuple): Una tupla que representa el horario consultado, con el día de la semana en la primera posición
        y la franja horaria en la segunda posición.

    Returns:
        list: Una lista de tuplas donde cada tupla contiene el nombre de un edificio y la cantidad de estudiantes que deberían
        estar dentro del edificio en el horario consultado.
    """
    estudiantes_por_edificio = {}

    # Iterar sobre cada curso
    for curso, info_curso in cursos.items():
        horario_curso = info_curso['horario']
        ubicacion_curso = info_curso['ubicacion']
        estudiantes_inscritos = info_curso['inscritos']

        # Verificar si el horario del curso coincide con el horario consultado
        if horario_curso == horario_consultado:
            edificio, _ = ubicacion_curso

            # Sumar la cantidad de estudiantes al total del edificio
            estudiantes_por_edificio[edificio] = estudiantes_por_edificio.get(edificio, 0) + estudiantes_inscritos

    # Convertir el diccionario en una lista de tuplas
    resultado = list(estudiantes_por_edificio.items())

    return resultado


# Ejemplo de uso de la función contar_estudiantes
cursos = {
    'Matemáticas': {'inscritos': 50, 'horario': ('lunes', '10:00 - 11:30'), 'ubicacion': ('Edificio A', 'Salón 101')},
    'Física': {'inscritos': 40, 'horario': ('martes', '10:00 - 11:30'), 'ubicacion': ('Edificio B', 'Salón 201')},
    'Química': {'inscritos': 30, 'horario': ('lunes', '10:00 - 11:30'), 'ubicacion': ('Edificio A', 'Salón 102')}
}

horario_consultado = ('lunes', '10:00 - 11:30')
resultado = contar_estudiantes(cursos, horario_consultado)
print("Cantidad de estudiantes por edificio en el horario consultado:", resultado)
