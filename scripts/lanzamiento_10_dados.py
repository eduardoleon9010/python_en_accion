# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 19:17:19 2024

@author: USUARIO
"""

import random
from collections import Counter
import matplotlib.pyplot as plt

def lanzar_dados(n_lanzamientos):
    """
    Simula lanzamientos de 6 dados.

    Parámetros:
    - n_lanzamientos (int): El número de lanzamientos a simular.

    Retorno:
    - list: Una lista con los resultados de cada lanzamiento.
    """
    resultados = [random.randint(1, 10) for _ in range(n_lanzamientos)]
    return resultados

def calcular_histograma(resultados):
    """
    Calcula un histograma de los resultados.

    Parámetros:
    - resultados (list): Una lista con los resultados de los lanzamientos.

    Retorno:
    - dict: Un diccionario donde las llaves son los números del dado y los valores son la frecuencia de cada número.
    """
    histograma = dict(Counter(resultados))
    return histograma

def plot_histograma(histograma):
    """
    Crea y muestra un plot de barras (histograma) a partir de un diccionario de frecuencias.

    Parámetros:
    - histograma (dict): Un diccionario donde las llaves son los números y los valores son las frecuencias.

    Retorno:
    - None
    """
    numeros = list(histograma.keys())
    frecuencias = list(histograma.values())

    plt.bar(numeros, frecuencias, color='blue')
    plt.xlabel('Número en el dado')
    plt.ylabel('Frecuencia')
    plt.title('Histograma de resultados de lanzamientos de dados')
    plt.show()

# Solicitar al usuario el número de lanzamientos por consola
try:
    n_lanzamientos_simulados = int(input("Ingrese el número de lanzamientos a simular: "))
except ValueError:
    print("Error: Ingrese un número entero válido.")
    exit()

# Simular lanzamientos de 6 dados
resultados_lanzamientos = lanzar_dados(n_lanzamientos_simulados)

# Calcular el histograma de los resultados
histograma_resultados = calcular_histograma(resultados_lanzamientos)

# Imprimir el histograma
print("Histograma de resultados:")
for numero, frecuencia in sorted(histograma_resultados.items()):
    print(f"Número {numero}: {frecuencia} veces")

# Plot del histograma
plot_histograma(histograma_resultados)
