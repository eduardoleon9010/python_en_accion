# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 23:21:54 2024

@author: USUARIO
"""
import matplotlib.pyplot as plt

def crear_rectangulo(punto1: tuple, punto2: tuple) -> tuple:
    """
    Crea un rectángulo a partir de dos puntos dados.

    Args:
    punto1 (tuple): Coordenadas (x, y) del primer punto.
    punto2 (tuple): Coordenadas (x, y) del segundo punto.

    Returns:
    tuple: Tupla que contiene las coordenadas (x, y) del vértice superior izquierdo del rectángulo,
           el ancho del rectángulo y su altura.
    """
    # Extraer coordenadas de los puntos
    x1, y1 = punto1
    x2, y2 = punto2
    
    # Calcular el ancho y el alto del rectángulo
    ancho = abs(x1 - x2)
    alto = abs(y1 - y2)
    
    # Determinar las coordenadas del vértice superior izquierdo
    x = min(x1, x2)
    y = min(y1, y2)
    
    return (x, y, ancho, alto)

# Definir puntos para crear el rectángulo
punto1 = (2, 2)
punto2 = (5, 7)  # Cambiar la coordenada y para hacer un rectángulo en lugar de un cuadrado

# Crear el rectángulo
x, y, ancho, alto = crear_rectangulo(punto1, punto2)

# Dibujar el rectángulo en un plano cartesiano
plt.figure()
ax = plt.gca()
ax.add_patch(plt.Rectangle((x, y), ancho, alto, fill=None, edgecolor='r'))
plt.xlim(0, 10)
plt.ylim(0, 10)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()

