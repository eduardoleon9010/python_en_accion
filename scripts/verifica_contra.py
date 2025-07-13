# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 10:08:05 2024

@author: USUARIO
"""
# Definición de la contraseña almacenada
contrasena_almacenada = "secreto"

# Solicitar al usuario ingresar su contraseña
contrasena_ingresada = input("Ingrese su contraseña:")

# Verificar si la contraseña ingresada coincide con la almacenada
if contrasena_almacenada == contrasena_ingresada:
    mensaje = "Su contraseña es correcta"
else:
    mensaje = "La contraseña es incorrecta"

# Imprimir el mensaje resultante
print(mensaje)
