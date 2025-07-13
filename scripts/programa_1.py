# Este programa solicita al usuario ingresar tres valores enteros, los almacena en variables x1, x2 y x3.
# Luego, rota estos valores de manera que x2 tenga el valor inicial de x1, x3 tenga el valor inicial de x2 y 
# x1 tenga el valor inicial de x3. Finalmente, muestra los valores rotados por consola.

# Solicitar al usuario los valores
x1 = int(input("Ingrese el primer valor (x1): "))
x2 = int(input("Ingrese el segundo valor (x2): "))
x3 = int(input("Ingrese el tercer valor (x3): "))

# Rotar los valores
temp = x1
x1 = x2
x2 = x3
x3 = temp

# Mostrar los valores rotados
print("Los valores rotados son:")
print("x1:", x1)
print("x2:", x2)
print("x3:", x3)
