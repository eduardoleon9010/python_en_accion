def saludar(nombre: str) -> str:
    """
    Genera un saludo personalizado para el usuario.
    
    Parameters:
    nombre (str): El nombre del usuario.
    
    Returns:
    str: Un mensaje de saludo personalizado.
    """
    return "¡Saludos " + nombre + "!"

nombre = input("¿Cuál es su nombre? ")
saludo = saludar(nombre)
print(saludo)
