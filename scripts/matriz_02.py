"""
Este código en Python calcula el promedio de todos los elementos en una matriz 3x3. 
Primero, se define una matriz identidad. Luego, se realiza un bucle para sumar todos los 
elementos de la matriz. El promedio se calcula dividiendo la suma total de los elementos 
por el número total de elementos en la matriz, que en este caso es 9. El resultado se 
imprime en la consola

"""

# Matriz identidad 3x3
M = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
s = 0

# Calcular la suma de todos los elementos en la matriz
for i in range(0, 3):
    for j in range(0, 3):
        s += M[i][j]

# Calcular el promedio de los elementos en la matriz
average = s / 9  # Dividir la suma total por el número total de elementos

print(average)  # Imprimir el promedio

