"""
Este código explora diferentes operaciones básicas con listas en Python. 
Comienza definiendo y mostrando dos listas distintas:

valor_lista: Una lista de números enteros.
lista_2: Una lista de cadenas de texto.
Luego, realiza una serie de operaciones:

Accede e imprime un elemento específico de la lista lista_2.
Agrega un nuevo elemento al final de lista_2 usando el método append().
Elimina el último elemento de lista_2 usando el método pop().
Vacía por completo la lista lista_2 usando el método clear().
Este código ilustra cómo acceder a elementos específicos de una lista, 
agregar elementos al final, eliminar elementos y vaciar una lista en Python.

Las listas son arreglos unidimensionales de cualquier tipo de dato, las listas tienen
indice de 0 hasta el numero que se defina, sin embargo, no es lo mismo que la cantidad de elementos dado que como  vemos en el siguiente ejemplo hay cinco elementos 
"""
#Indices       0, 1, 2, 3, 4 
valor_lista = [4, 7, 8, 9, 10]
print(valor_lista)
#print(valor_lista[0])

#Indices     0        1        2
lista_2 = ['Hola', 'Sara', 'Leon']
#print(lista_2)
print(lista_2[2])

#Agregar elementos a la lista
lista_2.append('Prueba')
print(lista_2)

#Sacar el ultimo elementos de la lista 
lista_2.pop()
print(lista_2)

#vaciar la lista
lista_2.clear()
print(lista_2)
