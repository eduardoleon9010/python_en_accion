"""
Este código crea una matriz identidad de tamaño n ingresado por el usuario. Asi funciona:

El programa solicita al usuario que ingrese el tamaño deseado para la matriz identidad (n).
Inicializa una lista vacía M que representará la matriz identidad.
Utiliza un bucle while que se ejecuta n veces para construir la matriz:
Para cada fila de la matriz, inicializa una nueva lista fila_nueva de longitud n, llena de ceros.
En la posición i de cada fila (donde i es el índice de la fila actual), coloca un 1, creando así la 
estructura de una matriz identidad.
Agrega la fila recién creada a la matriz M.
Incrementa el contador i para avanzar a la siguiente fila.
En el programa principal, utiliza un bucle for para imprimir cada fila de la matriz identidad M.
Este código genera una matriz cuadrada (el mismo número de filas y columnas) donde todos 
los elementos de la diagonal principal son 1 y los demás elementos son 0. La matriz resultante se 
muestra como una lista de listas, cada lista interior representando una fila de la matriz identidad.
"""
n = int(input("Ingrese el tamaño de la matriz identidad: "))

M = []
i = 0

while i < n:
    fila_nueva = [0] * n
    fila_nueva[i] = 1
    M.append(fila_nueva)
    i+=1
             #PROGRAMA PRINCIPAL
for fila in M:
     print(fila)
