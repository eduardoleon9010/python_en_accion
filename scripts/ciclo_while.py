from datetime import date

# Obtener la fecha actual utilizando la librería datetime y mostrar el día actual
hoy = date.today()
print("Hoy es el día:", hoy)
print()
print("TALLER 6 CICLOS ITERATIVOS CON LA SENTENCIA WHILE")
print()

# Solicitar al usuario ingresar un número entero
num_1 = int(input("Digite el primer número: "))

# Ciclo controlado por contador (while) desde 1 hasta el número ingresado por el usuario
print("***Ciclo controlado por contador")
i = 1
while i <= num_1:
    print(i)
    i += 1
print('Fin del ciclo')

print()

# Ciclo controlado por eventos: solicita al usuario adivinar un número secreto y muestra en cuántos intentos acertó
print("***Ciclo controlado por eventos")
intentos = 1
numero_secreto = 5  # Número secreto predefinido
numero_usuario = int(input('Adivine un número del 1 al 10: '))
while numero_usuario != numero_secreto:
    intentos += 1
    numero_usuario = int(input("Intenta adivinar el número secreto: "))
print(f"Adivinaste el número en el intento No. {intentos}")
print('Fin de ciclo')

print()

# Ciclo con la sentencia break: solicita al usuario ingresar el nombre de una amistad y muestra cada carácter del nombre en mayúsculas
print("***Ciclo abortado con la sentencia break")
nombre_amistad = input("Ingrese el nombre de una amistad: ")
nombre_amistad = nombre_amistad.upper()
for character in nombre_amistad:
    print(character)
    if character == "A":
        break
print("Fin del ciclo")

print()
print("Fin")
