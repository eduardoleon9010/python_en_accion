""" 
Este código solicita al usuario ingresar la base y la altura del triángulo, calcula el área del triángulo 
utilizando la fórmula adecuada y luego muestra el resultado.

"""
def area_triangulo() -> float:
    """
    Calcula el área de un triángulo dada la medida de la base y de la altura ingresadas por el usuario.
    
    Returns:
    float: El área calculada del triángulo.
    """
    base = int(input("Ingrese la medida de la base del triángulo: "))
    altura = int(input("Ingrese la medida de la altura del triángulo: "))
    return (base * altura) / 2

# Solicitar al usuario la base y la altura del triángulo y mostrar el área
area = area_triangulo()
print("El área del triángulo es:", area)

