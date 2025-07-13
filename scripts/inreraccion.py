from datetime import date

# Obtener la fecha actual utilizando la librería datetime y mostrar el día actual
hoy = date.today()
print("Hoy es el día:", hoy)

# Solicitar al usuario ingresar dos números enteros
n1 = int(input("Digite el primer número: "))
n2 = int(input("Digite el segundo número: "))

# Realizar operaciones matemáticas básicas con los números ingresados: suma, resta, multiplicación y división
suma = n1 + n2
resta = n1 - n2
producto = n1 * n2
division = n1 / n2

# Mostrar los resultados de estas operaciones
print("La suma es =", suma)
print("La resta es =", resta)
print("La multiplicación es =", producto)
print("La división es =", division)
print("Fin")

