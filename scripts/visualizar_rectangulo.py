# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 21:21:30 2024

@author: USUARIO
"""

import pygame
import sys

# Definir las propiedades del rectángulo
propiedades_rectangulo = {
    'color_interno': (16, 116, 61),  # Color del interior del rectángulo (RGB)
    'color_linea': (135, 4, 241),     # Color de la línea del rectángulo (RGB)
    'esquina': (4, 4),                # Coordenadas de la esquina superior izquierda del rectángulo
    'grosor': 3,                      # Grosor de la línea del rectángulo
    'pos': (9, 212),                  # Posición del rectángulo en la ventana (coordenadas x, y)
    'tamaño': (279, 215)              # Tamaño del rectángulo (ancho, alto)
}

def visualizar_rectangulo(propiedades):
    """
    Visualiza un rectángulo con las propiedades definidas en un diccionario.

    Args:
        propiedades (dict): Diccionario con las propiedades del rectángulo.

    Returns:
        None
    """
    # Inicializar pygame
    pygame.init()

    # Definir las propiedades del rectángulo
    color_interno = propiedades['color_interno']
    color_linea = propiedades['color_linea']
    esquina = propiedades['esquina']
    grosor = propiedades['grosor']
    pos = propiedades['pos']
    tamaño = propiedades['tamaño']

    # Crear una ventana de pygame
    ventana = pygame.display.set_mode((400, 400))  # Crear una ventana de 400x400 píxeles
    pygame.display.set_caption('Visualización de rectángulo')  # Título de la ventana

    # Dibujar el rectángulo en la ventana
    pygame.draw.rect(ventana, color_interno, (*pos, *tamaño), grosor)  # Dibujar el interior del rectángulo
    pygame.draw.rect(ventana, color_linea, (*pos, *tamaño), grosor)    # Dibujar la línea del rectángulo

    # Actualizar la ventana
    pygame.display.update()

    # Mantener la ventana abierta hasta que se cierre
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

# Llamar a la función para visualizar el rectángulo
visualizar_rectangulo(propiedades_rectangulo)
