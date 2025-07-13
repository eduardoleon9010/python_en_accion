# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 21:44:07 2024

@author: USUARIO
"""

def figura_a_svg(figura):
    """
    Convierte la información de una figura en formato de diccionario a su representación SVG.

    Args:
        figura (dict): Diccionario que representa una figura con propiedades como 'pos', 'tamaño', etc.

    Returns:
        str: Cadena de texto en formato SVG que representa la figura.
    """
    # Obtener las propiedades de la figura
    posicion = figura['pos']
    tamano = figura['tamaño']
    esquinas_redondeadas = figura['esquinas_redondeadas']
    grosor_linea = figura['grosor_linea']
    color_relleno = figura['color_relleno']
    color_linea = figura['color_linea']
    rotacion = figura['rotacion']

    # Construir la cadena SVG correspondiente a la figura
    svg = f'<rect x="{posicion[0]}" y="{posicion[1]}" width="{tamano[0]}" height="{tamano[1]}"'
    svg += f' rx="5" ry="5"' if esquinas_redondeadas else ''
    svg += f' stroke-width="{grosor_linea}" stroke="rgb{color_linea}" fill="rgb{color_relleno}"'
    svg += f' transform="rotate({rotacion[0]} {rotacion[1]} {rotacion[2]})"' if any(rotacion) else ''
    svg += '/>'

    return svg

def imagen_a_svg(imagen):
    """
    Convierte la información de una imagen vectorial en formato de lista de diccionarios a su representación SVG.

    Args:
        imagen (list): Lista de diccionarios que representan figuras en la imagen.

    Returns:
        str: Cadena de texto en formato SVG que representa la imagen.
    """
    # Inicializar la cadena SVG
    svg = '<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n'
    svg += '<svg xmlns="http://www.w3.org/2000/svg" version="1.1">\n'

    # Convertir cada figura a SVG y agregarla a la cadena SVG
    for figura in imagen:
        svg += figura_a_svg(figura) + '\n'

    # Cerrar la etiqueta SVG
    svg += '</svg>'

    return svg

def guardar_svg(svg, nombre_archivo):
    with open(nombre_archivo, 'w') as archivo:
        archivo.write(svg)

# Ejemplo de uso
imagen = [
    {'pos': (100, 100), 'tamaño': (200, 150), 'esquinas_redondeadas': False,
     'grosor_linea': 3, 'color_relleno': (255, 255, 255), 'color_linea': (0, 0, 0), 'rotacion': (0, 0, 0)},
    {'pos': (300, 200), 'tamaño': (150, 100), 'esquinas_redondeadas': True,
     'grosor_linea': 2, 'color_relleno': (255, 0, 0), 'color_linea': (0, 0, 255), 'rotacion': (45, 325, 225)}
]

# Convertir la información de la imagen a SVG
svg_imagen = imagen_a_svg(imagen)

# Guardar la cadena SVG en un archivo
nombre_archivo = 'imagen.svg'
guardar_svg(svg_imagen, nombre_archivo)

# Abrir el archivo SVG con el navegador web predeterminado
import webbrowser
webbrowser.open(nombre_archivo)
