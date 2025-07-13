"""
Este código en Python es un conjunto de operaciones utilizando la librería NumPy, 
la cual se utiliza principalmente para operaciones con matrices y vectores. Aquí 
se están realizando diversas operaciones:

Declaración de escalares, vectores y matrices: Se definen y muestran ejemplos de 
escalares, vectores y matrices usando la librería NumPy.

Formas de las variables: Se exploran las dimensiones y formas de las variables 
(escalares, vectores y matrices) usando el método .shape y se prueba el 
redimensionamiento con .reshape().

Operaciones básicas con matrices:

Suma de matrices.
Resta de matrices.
Suma de matriz y escalar.
Operaciones adicionales:

Transpuesta de matrices y vectores utilizando .T.
Multiplicación de un escalar y un vector.
Multiplicación de vectores (producto punto) usando np.dot.
Multiplicación de matrices con np.dot.
El código muestra ejemplos de manipulación y operaciones básicas con 
escalares, vectores y matrices usando NumPy en Python.
"""

#importamos la libreria
import numpy as np
#Declaracion de escalares, vectores y matrices

##escalar
e = 5
print (e)

##vectores
v = np.array([-4, 8,5])
print (v)

##matrices
m = np.array([[1, 0, -9], [3, -6, 7]])
print (m)

##formas de las variables
m.shape
v.shape

v.reshape(1,3)
v.reshape(3,1)

e.shape

##Suma de matrices
m1 = np.array([[5, 12, 6], [-3, 0, 14]])
m2 = np.array([[9, 8, 7], [1, 3, -5]])

m1 + m2

# Resta de matrices
m3 = np.array([[5, 3], [-2, 4]])
m4 = np.array([[7, -5], [3, 8]])

m3 - m4

#Suma de matriz y escalar
print(m1)
m1 + 2

##Transpuesta de matriz
print(m1)
m1.T

print(m2)
m2.T

print(m3)
m3.T

#Transpuesta de vector
print(v)
v.T

#Multiplicacion de un escalar y un vector
x = np.array([2, 8, -4])
print(x)

10 * x

#Multiplicacion de vectores(producto punto)
print(x)
y = np.array([1, -7, 3])
print(y)

np.dot(x,y)

#Multiplicacion de matrices
print(m1)
m5 = np.array([[2, -1], [8, 0],[3, 0]])
print(m5)
np.dot(m1,m5)

