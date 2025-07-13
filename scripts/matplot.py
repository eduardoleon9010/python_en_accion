"""
Este código genera datos aleatorios de notas para un conjunto de estudiantes y luego realiza tres tipos de 
gráficos diferentes utilizando Matplotlib.
"""

import random
import matplotlib.pyplot as plt
notas = []
ids_estudiantes = []
for i in range(30):
    nota_generada = random.normalvariate(3.25,0.98)
    nota_generada = round(nota_generada, 2)
    agregado = False
    while not agregado:
        id_generado = random.randint(20202001, 20202999)
        id_generado = str(id_generado)
        if id_generado not in ids_estudiantes:
            notas.append(nota_generada)
            ids_estudiantes.append(id_generado)
            agregado = True
            
plt.plot(ids_estudiantes, notas)
plt.title("Notas del curso")
plt.ylabel("Nota")
plt.xlabel("ID estudiante")
plt.xticks(rotation=90)
plt.show()

plt.hist(notas, bins=4, color=['green'], edgecolor='black', linewidth=1)
plt.title("Cantidad de estudiantes por rango de nota")
plt.ylabel("Cantidad de estudiantes")
plt.xlabel("Rango nota")
plt.show()

plt.scatter(ids_estudiantes, notas)
plt.title("Notas del curso")
plt.ylabel("Nota")
plt.xlabel("ID estudiante")
plt.xticks(rotation=90)
plt.show()

"""
Este código genera y visualiza datos simulados de notas de estudiantes. El primer gráfico muestra la 
evolución de las notas a lo largo de los IDs de los estudiantes. El segundo gráfico es un histograma 
que representa la cantidad de estudiantes en diferentes rangos de notas. El tercer gráfico es un 
gráfico de dispersión que muestra las notas individuales de cada estudiante en función de sus IDs.
"""
