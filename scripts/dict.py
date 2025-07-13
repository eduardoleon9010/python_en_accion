"""
Avance de Semestre para Estudiantes
Descripción
Este script en Python realiza el avance de semestre para cuatro estudiantes específicos. Aumenta el número 
de semestre actual (ssc) en uno para cada estudiante, lo que simula el avance de un período académico.

Código de Ejemplo
"""

def avanzar_semestre(est1: dict, est2: dict, est3: dict, est4: dict) -> None:
    est1['ssc'] += 1
    est2['ssc'] += 1
    est3['ssc'] += 1
    est4['ssc'] += 1
    
# Programa Principal
# (Aquí se definen los datos de los estudiantes)

e_1 = {'nombre':'Lina', 'codigo':'2020101234', 'genero':'femenino',
       'carrera':'Sistemas', 'promedio':4.78, 'ssc':4}
# ... (se definen e_2, e_3, e_4 de manera similar)

print("Semestre estudiante 1:", e_1['ssc'])
print("Semestre estudiante 2:", e_2['ssc'])
print("Semestre estudiante 3:", e_3['ssc'])
print("Semestre estudiante 4:", e_4['ssc'])

avanzar_semestre(e_1, e_2, e_3, e_4)

print("Nuevo semestre estudiante 1:", e_1['ssc'])
print("Nuevo semestre estudiante 2:", e_2['ssc'])
print("Nuevo semestre estudiante 3:", e_3['ssc'])
print("Nuevo semestre estudiante 4:", e_4['ssc'])


"""
Función avanzar_semestre
La función avanzar_semestre toma cuatro diccionarios que representan la información de los estudiantes y
aumenta el número de semestre actual en uno para cada estudiante.

Uso y Notas Adicionales
Este script es útil para simular el avance de semestre de los estudiantes. Puede ser empleado en sistemas 
de seguimiento académico o administrativo para actualizar la 
información académica de los estudiantes al finalizar un período.
"""
