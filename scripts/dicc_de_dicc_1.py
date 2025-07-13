# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 09:00:04 2024

@author: USUARIO
"""
def crear_directorio_telefonico():
    """
    Crea un directorio telefónico vacío.

    Returns:
    dict: Un diccionario que representa el directorio telefónico.
         Las llaves son los nombres de las personas y los valores son diccionarios
         con las llaves 'telefono' y 'direccion'.
    """
    return {}

def agregar_contacto(directorio, nombre, telefono, direccion):
    """
    Agrega un contacto al directorio telefónico.

    Args:
    directorio (dict): El directorio telefónico al que se agregará el contacto.
    nombre (str): El nombre del contacto.
    telefono (str): El número de teléfono del contacto.
    direccion (str): La dirección del contacto.

    Returns:
    None
    """
    # Verifica si el nombre ya existe en el directorio
    if nombre in directorio:
        print("El contacto ya existe en el directorio.")
    else:
        # Crea un nuevo diccionario para el contacto con su información
        contacto = {'telefono': telefono, 'direccion': direccion}
        # Agrega el contacto al directorio
        directorio[nombre] = contacto
        print("Contacto agregado correctamente.")

def mostrar_directorio_telefonico(directorio):
    """
    Muestra el contenido del directorio telefónico.

    Args:
    directorio (dict): El directorio telefónico que se desea mostrar.

    Returns:
    None
    """
    print("Directorio Telefónico:")
    for nombre, info in directorio.items():
        print(f"Nombre: {nombre}, Teléfono: {info['telefono']}, Dirección: {info['direccion']}")

# Ejemplo de uso
if __name__ == "__main__":
    # Crear un directorio telefónico vacío
    directorio = crear_directorio_telefonico()

    # Solicitar datos del contacto por teclado
    nombre = input("Ingrese el nombre del contacto: ")
    telefono = input("Ingrese el número de teléfono del contacto: ")
    direccion = input("Ingrese la dirección del contacto: ")

    # Agregar el contacto al directorio
    agregar_contacto(directorio, nombre, telefono, direccion)

    # Mostrar el directorio telefónico
    mostrar_directorio_telefonico(directorio)

