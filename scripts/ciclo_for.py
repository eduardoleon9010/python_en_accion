from datetime import date

# Obtención de la fecha actual usando la librería datetime
hoy = date.today()
print("Hoy es el día:", hoy)
print()
print("TALLER 5 CICLOS ITERATIVOS CON LA SENTENCIA FOR")
print()

# Solicitar al usuario ingresar dos números enteros
num_1 = int(input("Digite el primer número: "))
num_2 = int(input("Digite el segundo número (mayor): "))

# Ciclo for para imprimir los números desde 0 hasta el primer número ingresado
print("Ciclo para el primer número")
for i in range(num_1):
    print(i)
print('Fin del ciclo')

print()

# Ciclo for para imprimir los números desde el primer número ingresado hasta el segundo número ingresado
print("Ciclo desde el primero hasta el segundo número")
for i in range(num_1, num_2):
    print(i)
print('Fin de ciclo')

print()

# Ciclo for para imprimir los números desde el primer número ingresado hasta el segundo número ingresado con incrementos de 1
print("Ciclo desde el primero hasta el segundo número con incrementos de 1")
for i in range(num_1, num_2):
    print(i)
print('Fin de ciclo')

print()

# Solicitar al usuario ingresar el nombre de una empresa, convertirlo a minúsculas
# e iterar sobre cada carácter de ese nombre, imprimiendo cada carácter en una línea independiente
empresa = input("Digite nombre de una empresa: ")
empresa = empresa.lower()
print("Caracteres de la empresa en minúsculas:")
for character in empresa:
    print(character)
print("Fin del ciclo")

print()
print("Fin")
