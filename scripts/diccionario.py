"""
Uso de Diccionarios para Definiciones de Palabras
Descripción
Este código utiliza un diccionario en Python para almacenar definiciones 
de palabras. Cada palabra es una clave en el diccionario, y su valor asociado es la 
definición de esa palabra.
"""

palabras = {
    'imagen': 'Figura, representación, semejanza y apariencia de algo',
    'figura': 'Forma exterior de alguien o de algo', 
    'baraja': 'Conjunto completo de cartas empleado para juegos de azar',
    'posibilidad': 'Aptitud, potencia u ocasión para ser o existir algo'
}

# Obtener definiciones de palabras específicas
definicion_imagen = palabras['imagen']
print(definicion_imagen)

definicion_figura = palabras['figura']
print(definicion_figura)

llave = 'IMAGEN'

# Verificar si la palabra está en el diccionario antes de consultar su definición
if llave in palabras:
    definicion = palabras[llave]
else:
    definicion = "La palabra '" + llave + "' no se encuentra en el diccionario"

print(definicion)


"""
Explicación
Diccionario de Palabras y Definiciones: Se crea un diccionario palabras donde las claves son 
palabras y los valores son sus definiciones.
Acceso a Definiciones: Se accede a las definiciones de palabras específicas utilizando las 
claves del diccionario.
Verificación de Existencia: Se verifica si una palabra está presente en el diccionario antes 
de consultar su definición para evitar errores.

Uso y Notas Adicionales
Este código puede servir como ejemplo para crear y acceder a definiciones de palabras almacenadas 
en un diccionario en Python. Puedes ampliarlo agregando más palabras y sus definiciones al 
diccionario para mostrar su funcionalidad y utilidad
"""
