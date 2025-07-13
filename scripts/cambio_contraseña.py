# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 08:58:16 2024

@author: USUARIO
"""

import random

def longitud(cadena):
    """Calcula la longitud de una cadena."""
    return len(cadena)

def tiene_numeros(cadena):
    """Verifica si una cadena contiene al menos un número."""
    return any(char.isdigit() for char in cadena)

def tiene_mayusculas(cadena):
    """Verifica si una cadena contiene al menos una letra mayúscula."""
    return any(char.isupper() for char in cadena)

def tiene_minusculas(cadena):
    """Verifica si una cadena contiene al menos una letra minúscula."""
    return any(char.islower() for char in cadena)

def cambiar_contrasena(nueva_contrasena):
    """Simula el cambio de contraseña."""
    print(f"La contraseña se cambió a: {nueva_contrasena}")

# Define la contraseña anterior (reemplázala con el valor real)
contrasena_anterior = "Morty"

# Solicita al usuario ingresar una nueva contraseña
nueva = input("Introduzca su nueva contraseña:")

# Inicializa variables para verificar la validez de la nueva contraseña y almacenar mensajes de error
contrasena_correcta = True
mensaje = ""

# Verifica la longitud de la nueva contraseña
if longitud(nueva) < 8:
    contrasena_correcta = False
    mensaje += "La nueva contraseña debe tener al menos 8 caracteres" + "\n"

# Verifica si la nueva contraseña es igual a la contraseña anterior
if nueva == contrasena_anterior:
    contrasena_correcta = False
    mensaje += "La nueva contraseña no puede ser igual a la anterior" + "\n"

# Resto del código...

# Si la nueva contraseña es válida, realiza el cambio de contraseña
if contrasena_correcta:
    cambiar_contrasena(nueva)
    mensaje = "La contraseña se cambió exitosamente"

# Imprime el mensaje resultante
print(mensaje)
