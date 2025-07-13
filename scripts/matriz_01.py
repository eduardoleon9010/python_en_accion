"""
Este código muestra cómo acceder a elementos de una matriz e imprimir su contenido, demostrando operaciones 
básicas en una matriz de 3x3 en Python

Explicación:

La variable M representa una matriz de 3x3 (una lista de listas) donde cada sublista corresponde a una fila.
M[-1][0] y M[-1][-1] imprimen el primer y último elemento de la última fila respectivamente.
El primer bucle imprime la matriz completa por filas.
El bucle anidado imprime cada elemento individual de la matriz, fila por fila.

"""

# Definición y explicación
M = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
# El código anterior define una matriz identidad de 3x3 llamada 'M'.

# Acceso a elementos en la matriz
print(M[-1][0])  # Imprime el primer elemento en la última fila de la matriz
print(M[-1][-1])  # Imprime el último elemento en la última fila de la matriz
print("-")

# Imprimir la matriz completa por filas
for i in range(0, 3):
    print(M[i])
print("-")

# Imprimir cada elemento de la matriz
for i in range(0, 3):
    for j in range(0, 3):
        print(M[i][j])

        
        
