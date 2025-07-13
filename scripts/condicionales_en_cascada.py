"""
Este código es un menú simple que presenta al usuario varias opciones y ejecuta una función asociada a la opción elegida.

Primero, se definen cuatro funciones: funcion_a, funcion_b, funcion_c, y funcion_d. Cada una de estas funciones imprime 
un mensaje diferente indicando la opción seleccionada.

Luego, en el programa principal, se muestra un menú con cuatro opciones: a, b, c y d. El usuario debe ingresar una de 
estas letras como su elección.

El programa verifica la opción ingresada por el usuario y ejecuta la función correspondiente a esa opción. Si el usuario 
ingresa "a", se llama a funcion_a, si ingresa "b", se ejecuta funcion_b, y así sucesivamente. Si se ingresa una opción no 
válida, el programa muestra un mensaje de "Selección inválida".

El código presenta un menú al usuario, le permite elegir entre diferentes opciones y ejecuta una acción 
asociada a la opción seleccionada.
"""

def funcion_a() -> None:
    """Imprime un mensaje indicando que se seleccionó la opción 'a' del menú."""
    print("Usted ha escogido la opción a del menú")
    
def funcion_b() -> None:
    """Imprime un mensaje indicando que se seleccionó la opción 'b' del menú."""
    print("Usted ha escogido la opción b del menú")
    
def funcion_c() -> None:
    """Imprime un mensaje indicando que se seleccionó la opción 'c' del menú."""
    print("Usted ha escogido la opción c del menú")
    
def funcion_d() -> None:
    """Imprime un mensaje indicando que se seleccionó la opción 'd' del menú."""
    print("Usted ha escogido la opción d del menú")
    
# PROGRAMA PRINCIPAL

print("Menu principal")
print("Opción a")
print("Opción b")
print("Opción c")
print("Opción d")

x = input("Seleccione su opción: ")

if x == "a":
    funcion_a()
elif x == "b":
    funcion_b()
elif x == "c":
    funcion_c()
elif x == "d":
    funcion_d()
else:
    print("Selección inválida")
