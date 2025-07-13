# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 22:22:41 2024

@author: USUARIO
"""
# Ejemplo de creación de un diccionario con valores específicos
mi_diccionario = {
    'clave1': 10,      # Ejemplo de valor para 'clave1'
    'clave2': 'Hola',  # Ejemplo de valor para 'clave2'
    'clave3': [1, 2, 3] # Ejemplo de valor para 'clave3'
    # ... puedes agregar más pares llave:valor si es necesario
}

# Verificar si una clave está presente en el diccionario antes de acceder a su valor
clave_a_consultar = 'clave2'

# Uso del operador in para verificar si la clave está presente
if clave_a_consultar in mi_diccionario:
    valor_asociado = mi_diccionario[clave_a_consultar]
    print(f"El valor asociado a '{clave_a_consultar}' es: {valor_asociado}")
else:
    print(f"'{clave_a_consultar}' no existe en el diccionario.")
