# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 18:55:03 2024

@author: USUARIO
"""

def contar_celulares_version_so(cel1: dict, cel2: dict, cel3: dict, cel4: dict, so: str, version: str) -> int:
    """
    Cuenta cuántos celulares tienen la versión del sistema operativo indicada.

    La función espera que los diccionarios de los celulares tengan una llave llamada
    'sistema' con el nombre del sistema operativo y una llave llamada 'version' con
    la versión del sistema.

    Parámetros:
    - cel1 (dict): Diccionario que representa al primer celular.
    - cel2 (dict): Diccionario que representa al segundo celular.
    - cel3 (dict): Diccionario que representa al tercer celular.
    - cel4 (dict): Diccionario que representa al cuarto celular.
    - so (str): Nombre del sistema operativo a buscar.
    - version (str): Versión del sistema operativo a buscar.

    Retorno:
    - int: La cantidad de celulares que tienen exactamente el mismo sistema operativo
      en la misma versión que se pide en los parámetros 'so' y 'version'.
    """
    cantidad_celulares = 0

    if cel1['sistema'] == so and cel1['version'] == version:
        cantidad_celulares += 1
    if cel2['sistema'] == so and cel2['version'] == version:
        cantidad_celulares += 1
    if cel3['sistema'] == so and cel3['version'] == version:
        cantidad_celulares += 1
    if cel4['sistema'] == so and cel4['version'] == version:
        cantidad_celulares += 1

    return cantidad_celulares

# Crear diccionarios que representan celulares
cel1 = {
    'procesador': 2.4,
    'memoria': 64,
    'camara': 48,
    'pantalla': 'OLED',
    'ancho': 1080,
    'alto': 2400,
    'pila': 5000,
    'sistema': 'Android',
    'version': '10'
}

cel2 = {
    'procesador': 2.2,
    'memoria': 64,
    'camara': 32,
    'pantalla': 'OLED',
    'ancho': 768,
    'alto': 1080,
    'pila': 3500,
    'sistema': 'Android',
    'version': '8.1'
}

cel3 = {
    'procesador': 2.0,
    'memoria': 32,
    'camara': 18,
    'pantalla': 'Retina',
    'ancho': 375,
    'alto': 812,
    'pila': 4200,
    'sistema': 'iOS',
    'version': '9.0'
}

cel4 = {
    'procesador': 1.8,
    'memoria': 16,
    'camara': 6,
    'pantalla': 'Retina',
    'ancho': 375,
    'alto': 667,
    'pila': 4150,
    'sistema': 'iOS',
    'version': '8.1.4'
}

# Contar celulares con sistema operativo 'iOS' y versión '9.0'
cantidad_celulares = contar_celulares_version_so(cel1, cel2, cel3, cel4, 'iOS', '9.0')

print(f"Hay {cantidad_celulares} celulares con sistema operativo 'iOS' y versión '9.0'.")
