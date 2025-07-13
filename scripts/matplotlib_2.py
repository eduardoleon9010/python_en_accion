# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 19:44:31 2024

@author: USUARIO
"""
import matplotlib.pyplot as plt
import random

# Generación de datos aleatorios para 30 estudiantes
ids_estudiantes = list(range(1, 31))  # Lista de identificadores de estudiantes
notas = [random.gauss(70, 10) for _ in range(30)]  # Lista de notas aleatorias

# Gráfico de línea
plt.figure(figsize=(8, 6))  # Tamaño de la figura
plt.plot(ids_estudiantes, notas)  # Crear el gráfico de línea
plt.title('Notas del curso')  # Título del gráfico
plt.ylabel('Nota')  # Etiqueta del eje Y
plt.xlabel('ID de Estudiante')  # Etiqueta del eje X
plt.xticks(rotation=90)  # Rotar etiquetas del eje X
plt.show()  # Mostrar el gráfico

# Histograma
plt.figure(figsize=(8, 6))  # Tamaño de la figura
plt.hist(notas, bins=4, color='green', edgecolor='black', linewidth=1)  # Crear el histograma
plt.title('Cantidad de estudiantes por rango de nota')  # Título del gráfico
plt.ylabel('Cantidad de estudiantes')  # Etiqueta del eje Y
plt.xlabel('Rango nota')  # Etiqueta del eje X
plt.show()  # Mostrar el histograma

# Gráfico de dispersión
plt.figure(figsize=(8, 6))  # Tamaño de la figura
plt.scatter(ids_estudiantes, notas)  # Crear el gráfico de dispersión
plt.title('Notas del curso')  # Título del gráfico
plt.ylabel('Nota')  # Etiqueta del eje Y
plt.xlabel('ID de Estudiante')  # Etiqueta del eje X
plt.xticks(rotation=90)  # Rotar etiquetas del eje X
plt.show()  # Mostrar el gráfico de dispersión
