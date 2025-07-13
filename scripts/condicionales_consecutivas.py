"""
Este código solicita tres números al usuario y luego cuenta cuántos de esos números son pares. Realiza lo siguiente:

Solicita tres números al usuario.
Verifica si cada uno de estos números es par utilizando el operador de módulo %. Si el residuo de la división entre 
el número y 2 es igual a cero, significa que es un número par.
Incrementa el contador cuantos por cada número par encontrado.
Imprime el número total de pares entre los tres números ingresados por el usuario.
"""

num1 = int (input("Digite un numero: "))
num2 = int (input("Digite un segundo numero: "))
num3 = int (input("Digite un tercer numero: "))

cuantos = 0

if (num1 % 2 == 0):
    cuantos += 1
if (num2 % 2 == 0):
    cuantos += 1
if (num3 % 2 == 0):
    cuantos += 1
print ("De los tres numeros digitados hay", cuantos, "pares" )



