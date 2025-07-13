from datetime import date

# Obtener la fecha actual utilizando la librería datetime y mostrar el día actual
hoy = date.today()
print("Hoy es el día:", hoy)

# Solicitar al usuario ingresar dos valores enteros, A y B
a = int(input("Digite el valor A: "))
b = int(input("Digite el valor B: "))

# Comparar A y B, y mostrar un mensaje según la relación entre ambos números
if a >= b:
    print("A es mayor o igual a B")
else:
    print("A es menor que B")
print()

# Definir dos variables con nombres de cursos
curso_1 = "Requerimientos"
curso_2 = "Algoritmos"
print("El curso_1 es:", curso_1)
print("El curso_2 es:", curso_2)

# Comparar los cursos definidos y mostrar un mensaje basado en la condición
if curso_1 == "Requerimientos" and curso_2 == "Algoritmos":
    print("Usted estudia programación de software")
else:
    print("Usted estudia un programa diferente a programación de software")
print()

# Mostrar un mensaje señalando el final del análisis del programa de formación SENA
print("*** Final del análisis del programa de formación SENA")
print()

# Solicitar al usuario ingresar una oración y mostrar información sobre ella
frase = input("Digite una oración: ")
print("La frase en mayúscula es:", frase.upper())
longitud = len(frase)
print("La longitud de la frase es:", len(frase), "caracteres")

# Evaluar si la longitud de la oración es mayor a 10 caracteres y mostrar un mensaje correspondiente
if longitud > 10:
    print("La frase contiene más de 10 caracteres")
else:
    print("La frase contiene 10 o menos caracteres")
print()

# Mostrar un mensaje de finalización del programa
print("Fin")
