"""
Identificador de Estudiantes en Riesgo
Descripción
Este script en Python identifica estudiantes en riesgo basándose en su promedio académico. 
Compara los promedios de cuatro estudiantes y registra aquellos cuyo promedio sea menor a 
3.4 en un diccionario que relaciona el código del estudiante con su promedio.
"""

def quienes_en_riesgo(est1: dict, est2: dict, est3: dict, est4: dict) -> dict:
    en_riesgo = {}
    
    if est1['promedio'] < 3.4:
        en_riesgo[est1['codigo']] = est1['promedio']
    if est2['promedio'] < 3.4:
        en_riesgo[est2['codigo']] = est2['promedio']
    if est3['promedio'] < 3.4:
        en_riesgo[est3['codigo']] = est3['promedio']
    if est4['promedio'] < 3.4:
        en_riesgo[est4['codigo']] = est4['promedio']
        
    return en_riesgo

# Programa Principal
# (Aquí se definen los datos de los estudiantes)

e_1 = {'nombre':'Lina', 'codigo':'2020101234', 'genero':'femenino',
       'carrera':'Sistemas', 'promedio':4.78, 'ssc':2}
# ... (se definen e_2, e_3, e_4 de manera similar)

riesgo = quienes_en_riesgo(e_1, e_2, e_3, e_4)
        
print(riesgo)

        
"""
Función quienes_en_riesgo
Esta función recibe como parámetros los diccionarios que representan la información de cuatro estudiantes 
y retorna un diccionario que muestra los códigos de los estudiantes cuyos promedios son menores a 3.4.

Uso y Notas Adicionales
Este script es útil para identificar rápidamente los estudiantes que podrían estar en riesgo académico 
debido a un promedio bajo. Puede ser empleado por personal docente o administrativo para un seguimiento 
más cercano de estos estudiantes.
"""
