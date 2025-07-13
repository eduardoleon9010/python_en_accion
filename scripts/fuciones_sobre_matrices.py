# -*- coding: utf-8 -*-
'''Escriba las siguientes funciones que reciben por 
parametro una matriz de enteros y retornan:
    1. La suma de todos los valores
    2. La suma de los valores de una fila dada por parametro
    3. La suma de los valores de una colunma dada por parametro
    4. Indique verdadero o falso si en la matriz hay al menos un valor negativo
    5. La fila con el mayor numero de ceros
'''
def calcular_suma_matriz(matriz:list)->int:
    suma = 0
    
    for i in range(0, len(matriz)):
        for j  in range(0, len(matriz[0])):
            suma += matriz[i][j]
            
    return suma

def calcular_suma_fila(matriz:list, fila:int)->int:
    suma = 0
    
    for num_col in range(0, len(matriz[0])):
        suma += matriz[fila][num_col]
   
    return   suma

def calcular_suma_columna(matriz:list, columna:int)->int:
    suma = 0
    
    for num_fila in range(0, len(matriz)):
        suma += matriz[num_fila][columna]
        
    return suma

def existe_negativo(matriz:list)->bool:
    encontrado = False
    i = 0
    j = 0
    
    while i < len(matriz) and not encontrado:
        while j < len(matriz[0]) and not encontrado:
            if matriz[i][j] < 0:
                encontrado = True
            j+=1
        i+=1

    return encontrado

def fila_mas_ceros(matriz:list)->int:
    fila_mas = 0
    max_ceros = 0
    
    for i in range(0, len(matriz)):
        cant_ceros = 0
        for j in range(0, len(matriz)):
            if matriz[i][j] == 0:
                cant_ceros+=1
                
        if cant_ceros > max_ceros:
            max_ceros = cant_ceros
            fila_mas = i
            
    return fila_mas


M = []

for i in range(5):
    fila = []
    for j in range(5):
        numero = random.randint(-2,5)
        fila.append(numero)
    M.append(fila)
        
print("Matriz:")
for fila in M:
        print(fila)

print("\nResultados:\n")

print("Suma matriz:", calcular_suma_matriz(M))
print("Suma fila:", calcular_suma_fila(M,1))
print("Suma columna:", calcular_suma_columna(M,4))
print("Existe negativo:", existe_negativo(M))
print("Fila mas ceros:", fila_mas_ceros(M))
        
              