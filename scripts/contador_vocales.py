"""
Contador de Vocales en un Texto
Descripción
Este fragmento de código en Python cuenta la cantidad de veces que aparece cada vocal (a, e, i, o, u) 
dentro de un texto proporcionado. Utiliza un diccionario para almacenar estas frecuencias y devuelve 
este histograma de ocurrencias como resultado.
"""
def contar_vocales(texto: str) -> dict:
    """Cuenta la cantidad de veces que aparece cada vocal dentro de un texto.
    
    Parámetros:
      texto (str): El texto en el que se contarán las vocales.
    
    Retorno:
      (dict): Un diccionario donde las llaves son las vocales minúsculas y los valores
              son la cantidad de veces que aparece la vocal dentro del texto.
    """
    histograma = {}
    histograma['a'] = texto.lower().count('a')
    histograma['e'] = texto.lower().count('e')
    histograma['i'] = texto.lower().count('i')
    histograma['o'] = texto.lower().count('o')
    histograma['u'] = texto.lower().count('u')
    return histograma

pangrama = 'Jovencillo emponzoñado de whisky, ¡qué figurota exhibe!'
vocales = contar_vocales(pangrama)
print(vocales)

"""
Función contar_vocales
Esta función cuenta la frecuencia de aparición de las vocales (a, e, i, o, u) en un texto dado. Utiliza un 
enfoque simple de búsqueda y recuento individual para cada vocal, y devuelve un diccionario donde las llaves 
son las vocales y los valores son sus frecuencias en el texto.

Uso y Notas Adicionales
Esta función es útil para analizar la distribución de las vocales en un texto. Puedes usarla para medir la 
presencia y frecuencia de las vocales en diferentes contextos textuales.
"""
