# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 16:37:43 2024

@author: Ing. Leon
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def convolucion(imagen: np.ndarray, mascara: np.ndarray) -> np.ndarray:
    """Aplica la convolución entre una imagen y una máscara.

    Args:
        imagen (np.ndarray): La imagen representada como un array numpy.
        mascara (np.ndarray): La máscara representada como un array numpy.

    Returns:
        np.ndarray: La imagen resultante después de aplicar la convolución.
    """
    # Obtiene las dimensiones de la imagen y la máscara
    alto_imagen, ancho_imagen = imagen.shape[:2]
    alto_mascara, ancho_mascara = mascara.shape[:2]

    # Calcula la mitad del ancho y alto de la máscara
    mitad_alto_mascara = alto_mascara // 2
    mitad_ancho_mascara = ancho_mascara // 2

    # Inicializa la imagen resultante
    imagen_resultante = np.zeros_like(imagen)

    # Recorre cada píxel de la imagen
    for i in range(mitad_alto_mascara, alto_imagen - mitad_alto_mascara):
        for j in range(mitad_ancho_mascara, ancho_imagen - mitad_ancho_mascara):
            # Inicializa el valor de cada componente del píxel
            nuevo_valor = [0, 0, 0, 0]  # Ahora con cuatro elementos

            # Recorre cada componente del píxel (R, G, B, A si está presente)
            for k in range(imagen.shape[2]):  # Usa la dimensión de la imagen
                # Inicializa el valor acumulado para la convolución
                valor_acumulado = 0
                
                # Recorre cada píxel de la máscara
                for m in range(alto_mascara):
                    for n in range(ancho_mascara):
                        # Calcula las coordenadas del píxel correspondiente en la imagen
                        x_imagen = i + m - mitad_alto_mascara
                        y_imagen = j + n - mitad_ancho_mascara
                        
                        # Obtiene el valor del píxel de la imagen y de la máscara
                        valor_imagen = imagen[x_imagen, y_imagen, k]
                        valor_mascara = mascara[m, n]
                        
                        # Acumula el producto del valor del píxel de la imagen y de la máscara
                        valor_acumulado += valor_imagen * valor_mascara
                
                # Normaliza el valor acumulado si es necesario
                suma_valores_mascara = np.sum(mascara)
                if suma_valores_mascara != 1:
                    nuevo_valor[k] = valor_acumulado / suma_valores_mascara
                else:
                    nuevo_valor[k] = valor_acumulado

            # Asigna el nuevo valor al píxel en la imagen resultante
            imagen_resultante[i, j] = nuevo_valor

    return imagen_resultante


# Carga la imagen y la máscara
imagen = mpimg.imread("muestra.jpg")
mascara = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])

# Aplica la convolución
imagen_conv = convolucion(imagen, mascara)

# Muestra la imagen original y la imagen después de aplicar la convolución
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(imagen)
plt.title("Imagen Original")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(imagen_conv)
plt.title("Imagen Después de Convolución")
plt.axis("off")

plt.show()
