# -*- coding: utf-8 -*-
import math

x = int(input("Digite un numero: "))

if x < 0:
    print("El numero negativo ", x, " no es valido aqui.")
    y = x
    x = 42
    print("Decidi usar el numero 42 en lugar de ", y)
    
print("La raiz cuadrada de ", x, "es", math.sqrt(x))

