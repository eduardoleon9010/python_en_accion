import math

# Este programa realiza varias acciones:
# Solicita al usuario que introduzca un número entero.
# Verifica si el número ingresado es negativo.
# Si es negativo, imprime un mensaje indicando que no es válido, guarda el valor original en una variable y,
# asigna el valor 42 a la variable x y luego muestra un mensaje indicando que se decidió usar 42 en lugar del número original.
# Si no es negativo, continúa sin hacer ningún cambio en x.
# Calcula la raíz cuadrada del valor final de x utilizando la función math.sqrt() y muestra el resultado junto con
# un mensaje que indica cuál es el número del que se está calculando la raíz cuadrada.

x = int(input("Digite un numero: "))

if x < 0:
    print("El numero negativo ", x, "no es valido aqui.")
    y = x
    x = 42
    print("Decidi usar el numero 42 en lugar de ", y)

print("La raiz cuadrada de ", x, "es", math.sqrt(x))
