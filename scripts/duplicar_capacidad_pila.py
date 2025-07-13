# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 19:16:05 2024

@author: USUARIO
"""

def duplicar_capacidad_pila(celular1: dict, celular2: dict, celular3: dict, celular4: dict) -> None:
    """
    Modifica los diccionarios de 4 celulares para duplicar la capacidad de la pila de cada uno.

    Parámetros:
    - celular1 (dict): Diccionario que representa las especificaciones del primer celular.
    - celular2 (dict): Diccionario que representa las especificaciones del segundo celular.
    - celular3 (dict): Diccionario que representa las especificaciones del tercer celular.
    - celular4 (dict): Diccionario que representa las especificaciones del cuarto celular.

    Nota: La función modifica directamente los diccionarios, no retorna nada.

    Ejemplo:
    Si antes de llamar a la función:
    celular1 = {'modelo': 'A1', 'pila': 3000, 'precio': 400}
    celular2 = {'modelo': 'B2', 'pila': 2500, 'precio': 350}
    celular3 = {'modelo': 'C3', 'pila': 4000, 'precio': 500}
    celular4 = {'modelo': 'D4', 'pila': 2000, 'precio': 300}

    Después de llamar a la función:
    celular1 = {'modelo': 'A1', 'pila': 6000, 'precio': 400}
    celular2 = {'modelo': 'B2', 'pila': 5000, 'precio': 350}
    celular3 = {'modelo': 'C3', 'pila': 8000, 'precio': 500}
    celular4 = {'modelo': 'D4', 'pila': 4000, 'precio': 300}
    """
    # Función auxiliar para duplicar la capacidad de la pila de un celular
    def duplicar_pila(celular):
        celular['pila'] *= 2

    # Duplicar la capacidad de la pila de cada celular
    duplicar_pila(celular1)
    duplicar_pila(celular2)
    duplicar_pila(celular3)
    duplicar_pila(celular4)

# Ejemplo de uso
celular1 = {'modelo': 'A1', 'pila': 3000, 'precio': 400}
celular2 = {'modelo': 'B2', 'pila': 2500, 'precio': 350}
celular3 = {'modelo': 'C3', 'pila': 4000, 'precio': 500}
celular4 = {'modelo': 'D4', 'pila': 2000, 'precio': 300}

# Llamar a la función para duplicar la capacidad de la pila
duplicar_capacidad_pila(celular1, celular2, celular3, celular4)

# Imprimir los resultados después de la modificación
print(celular1)
print(celular2)
print(celular3)
print(celular4)
