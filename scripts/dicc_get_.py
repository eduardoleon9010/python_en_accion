# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 07:51:10 2024

@author: USUARIO
"""
# Crear un diccionario de ejemplo
mi_diccionario = {
    'clave1': 10,
    'clave2': 'Hola',
    'clave3': [1, 2, 3]
}

# Consultar el valor asociado a una llave que existe
llave_existente = 'clave2'
valor_existente = mi_diccionario.get(llave_existente, 'Valor por defecto si no existe la llave')

# Imprimir el resultado
print(f"El valor asociado a '{llave_existente}' es: {valor_existente}")

# Consultar el valor asociado a una llave que no existe
llave_no_existente = 'clave4'
valor_no_existente = mi_diccionario.get(llave_no_existente, 'Valor por defecto si no existe la llave')

# Imprimir el resultado
print(f"El valor asociado a '{llave_no_existente}' es: {valor_no_existente}")
