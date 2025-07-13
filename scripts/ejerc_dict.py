"""
Acceso a Valores de un Diccionario usando Llaves Variables
Descripción
Este código en Python ilustra cómo acceder a los valores de un diccionario utilizando variables como llaves. 
Comienza definiendo un diccionario con pares de llaves y valores. Luego, accede a los valores del diccionario 
utilizando variables que contienen nombres de llaves y los imprime en la consola.

Código de Ejemplo
"""
diccionario = {"llave": "valor", "palabra": "definición"}
llave = "llave"
print("1.", diccionario["llave"])
print("2.", diccionario[llave])
llave = "palabra"
print("3.", diccionario[llave])
print("4.", diccionario["palabra"])

# Salida esperada

1. valor
2. valor
3. definición
4. definición

"""
Funcionamiento del Código
Define un diccionario con pares de llaves y valores.
Accede a los valores del diccionario utilizando variables que almacenan nombres de llaves.
Imprime los valores correspondientes en la consola.
Uso y Notas Adicionales
Este fragmento de código demuestra cómo acceder a los valores de un diccionario utilizando 
variables que contienen nombres de llaves. Puede ser útil para dinamizar la obtención de 
valores de un diccionario según las necesidades del programa.
"""
