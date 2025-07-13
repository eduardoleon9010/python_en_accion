"""
Este código tiene como objetivo calcular el factorial de un número entero positivo ingresado por el usuario.

La función calcular_factorial toma un número entero n como argumento y calcula su factorial mediante un bucle while.
Inicialmente, se establece una bandera terminar en False y se inicializa la variable factorial en 1.
En el bucle while, se verifica si n es igual a 0. Si es así, se establece terminar en True, deteniendo el bucle.
Si n no es cero, se multiplica el valor actual de factorial por n y se reduce n en 1 en cada iteración.
Una vez que n alcanza cero, el bucle se detiene y la función devuelve el valor del factorial.
En el programa principal, se solicita al usuario ingresar un número entero positivo. Se verifica que el número sea 
positivo, y si es negativo, se le pide al usuario que ingrese un entero positivo hasta que lo haga. Luego, se llama 
a la función calcular_factorial pasando el número ingresado como argumento y se muestra el resultado del factorial 
en la pantalla.
"""

def calcular_factorial(n:int)->int:
    terminar = False
    factorial = 1
    
    while terminar == False:
        if n == 0:
            terminar = True
        else:
            factorial *= n 
            n -= 1
            
    return factorial

numero = int(input("Ingrese un numero entero positivo: "))

while numero < 0:
    print("No se puermiten numeros negativos")
    numero = int(input("Ingrese un entero positivo: "))
print(numero,"! es igual a",calcular_factorial(numero))



