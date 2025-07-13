from datetime import date

# Obtener la fecha actual utilizando la librería datetime y mostrar el día actual
hoy = date.today()
print("Hoy es el día:", hoy)
print()

# Solicitar al usuario ingresar dos valores enteros A y B para comparar
a = int(input("Digite el valor A: "))
b = int(input("Digite el valor B: "))

# Comparar A y B, luego imprimir un mensaje basado en la comparación
if a >= b:
    print("A es mayor o igual a B")
else:
    print("A es menor que B")
print()

# Definir dos variables de curso y compararlas, luego mostrar el tipo de curso
curso_1 = "Requerimientos"
curso_2 = "Algoritmos"
print("El curso 1 es:", curso_1)
print("El curso 2 es:", curso_2)
if curso_1 == "Requerimientos" and curso_2 == "Algoritmos":
    print("Usted estudia programación de software")
else:
    print("Usted estudia gastronomía")
print()

# Imprimir un mensaje indicando el final del análisis del programa de formación SENA
print("*** Final del análisis del programa de formación SENA")
print()

# Solicitar al usuario ingresar una oración, mostrarla en mayúsculas y calcular su longitud
frase = input("Digite una oración: ")
print("La frase en mayúscula es:", frase.upper())
longitud = len(frase)
print("La longitud de la frase es:", len(frase), "caracteres")

# Evaluar si la longitud de la oración es mayor a 10 caracteres y mostrar un mensaje en consecuencia
if longitud > 10:
    print("La frase contiene más de 10 caracteres")
else:
    print("La frase contiene 10 o menos caracteres")
print()

# Mostrar el final del programa
print("Fin")
