# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 08:17:30 2024

@author: USUARIO
"""

def contar_estudiantes(cursos: dict, horario_consulta: tuple) -> list:
    """
    Cuenta la cantidad de estudiantes por edificio en un horario específico.

    Args:
    cursos (dict): Un diccionario donde las llaves son los nombres de los cursos y los valores son también
    diccionarios con tres llaves: 'inscritos' para indicar el número de estudiantes inscritos en el curso,
    'horario' para indicar el horario en el que se dicta el curso, y 'ubicacion' para indicar el salón donde
    se dicta el curso.
    horario_consulta (tuple): Una tupla que contiene el número de día y la franja horaria en la que se quiere
    hacer la consulta.

    Returns:
    list: Una lista de tuplas donde cada tupla contiene en la primera posición el nombre de un edificio y en
    la segunda posición la cantidad de estudiantes que deberían estar dentro del edificio en el horario
    consultado.
    """
    estudiantes_por_edificio = {}
    for curso, info_curso in cursos.items():
        horario_curso = info_curso['horario']
        ubicacion_curso = info_curso['ubicacion']
        inscritos = info_curso['inscritos']
        dia_curso, franja_curso = horario_curso
        dia_consulta, franja_consulta = horario_consulta
        if dia_curso == dia_consulta and franja_curso == franja_consulta:
            edificio, _ = ubicacion_curso
            estudiantes_por_edificio[edificio] = estudiantes_por_edificio.get(edificio, 0) + inscritos
    return list(estudiantes_por_edificio.items())

# Ejemplo de uso
cursos = {
    'Matemáticas': {'inscritos': 30, 'horario': ('lunes', '10:00 - 11:30'), 'ubicacion': ('Edificio A', 'Sala 101')},
    'Física': {'inscritos': 25, 'horario': ('lunes', '10:00 - 11:30'), 'ubicacion': ('Edificio B', 'Sala 201')},
    'Química': {'inscritos': 20, 'horario': ('lunes', '11:30 - 13:00'), 'ubicacion': ('Edificio A', 'Sala 102')},
    'Biología': {'inscritos': 35, 'horario': ('martes', '10:00 - 11:30'), 'ubicacion': ('Edificio C', 'Sala 301')}
}

horario_consulta = ('lunes', '10:00 - 11:30')
resultado = contar_estudiantes(cursos, horario_consulta)
print("Cantidad de estudiantes por edificio en el horario consultado:", resultado)
