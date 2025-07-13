from datetime import date

# Obtener la fecha actual utilizando la librería datetime y mostrar el día actual
hoy = date.today()
print("Hoy es el día:", hoy)
print()
print("EJERCICIO DE LAS CLASES DE TRIÁNGULOS")
print()

# Solicitar al usuario ingresar tres valores enteros A, B y C para analizar el tipo de triángulo
a = int(input("Digite el valor A: "))
b = int(input("Digite el valor B: "))
c = int(input("Digite el valor C: "))

# Comparar los valores ingresados para determinar el tipo de triángulo
if a == b and a == c and b == c:
    print("EL TRIÁNGULO ES EQUILÁTERO")
else:
    if a == b or b == c or a == c:
        print("EL TRIÁNGULO ES ISÓSCELES")
    else:
        print("El triángulo es Escaleno")
print()

# Solicitar al usuario ingresar un animal y comparar con opciones predefinidas
animal = input("Digite un animal: ")
animal = animal.upper()
if animal == "PERRO":
    print("Este animal es el mejor amigo del hombre:", animal)
elif animal == "GATO":
    print("Este animal persigue ratones:", animal)
elif animal == "OSO":
    print("Este animal vive en el polo norte:", animal)
print()
print("Fin")

