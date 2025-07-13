"""
Este código define una función llamada promedio_lista que calcula el promedio de los números 
positivos presentes en una lista. 

Asi funciona:

La función promedio_lista toma una lista de números como entrada.
Inicializa dos variables, sumatoria y total, ambas a cero. sumatoria se utiliza para acumular 
la suma de los números positivos, mientras que total cuenta la cantidad de números positivos en la lista.
Itera a través de la lista de números proporcionada. Para cada número positivo en la lista, se
agrega ese número a sumatoria y se incrementa total.
Calcula el promedio dividiendo la suma total (sumatoria) por la cantidad total de números positivos presentes (total).
Devuelve el valor del promedio calculado.
El código muestra cómo utilizar esta función con una lista específica llamada lista. La lista 
contiene una serie de números, positivos y negativos. Luego, imprime el resultado de la función 
promedio_lista aplicada a esta lista
"""
def promedio_lista(numeros:list)->float:
    sumatoria = 0
    total = 0
    
    for num in numeros:
        if num > 0:
            sumatoria += num
            total += 1
    promedio = sumatoria/total
    return promedio

lista = [4,-1,-4,5,1,6,10,17,31,-14,-61]          

print(promedio_lista(lista))

