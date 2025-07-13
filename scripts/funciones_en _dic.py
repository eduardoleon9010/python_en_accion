"""
Este código muestra ejemplos de funciones que operan sobre un diccionario de 
palabras y sus definiciones. Aquí está el resumen:

Función agregar_definicion:

Añade una palabra y su definición al diccionario.
Si la palabra ya existe, no agrega una nueva definición.
Devuelve un valor booleano indicando si la definición se agregó con éxito.
Permite múltiples definiciones para una misma palabra, separadas por saltos de línea.
Función eliminar_palabra:

Elimina una palabra y su definición asociada del diccionario.
Devuelve un valor booleano indicando si la palabra se eliminó con éxito.
Si la palabra no existe en el diccionario, no realiza ninguna acción.
Ejemplos de uso de las funciones:

Agrega definiciones a un diccionario y comprueba si las definiciones se agregaron correctamente.
Elimina palabras del diccionario y verifica si fueron eliminadas con éxito.
Este código presenta operaciones básicas como agregar y eliminar palabras con sus 
respectivas definiciones en un diccionario, permitiendo múltiples definiciones para una misma palabra.
"""

def agregar_definicion(diccionario: dict, palabra: str, definicion: str)-> None:
  diccionario[palabra] = definicion
palabras = {}
agregar_definicion(palabras, 'imagen', 'Figura, representación, semejanza y apariencia de algo')
agregar_definicion(palabras, 'figura', 'Forma exterior de alguien o de algo')

def agregar_definicion(diccionario: dict, palabra: str, definicion: str)-> bool:
  definicion_agregada = False
  if palabra not in diccionario:
      diccionario[palabra] = definicion
      definicion_agregada = True
  return definicion_agregada

palabras = {}
res1 = agregar_definicion(palabras, 'imagen', 'Figura, representación, semejanza y apariencia de algo')
res2 = agregar_definicion(palabras, 'figura', 'Forma exterior de alguien o de algo')
res3 = agregar_definicion(palabras, 'imagen', 'Figura, representación, semejanza y apariencia de algo')
print(res1, res2, res3)

def agregar_definicion(diccionario: dict, palabra: str, definicion: str)-> bool:
  definicion_agregada = False
  # La palabra es nueva en el diccionario
  if palabra not in diccionario:
      diccionario[palabra] = definicion
      definicion_agregada = True
  # La palabra no es nueva pero la definición sí es nueva
  elif definicion not in diccionario[palabra]:
      diccionario[palabra] += '\n' + definicion
      definicion_agregada = True
  return definicion_agregada

palabras = {}
res1 = agregar_definicion(palabras, 'imagen', 'Figura, representación, semejanza y apariencia de algo')
res2 = agregar_definicion(palabras, 'imagen', 'Estatua, efigie o pintura de una divinidad o de un personaje sagrado.')
res3 = agregar_definicion(palabras, 'imagen', 'Figura, representación, semejanza y apariencia de algo')
print(res1, res2, res3)

def eliminar_palabra(diccionario: dict, palabra: str)-> bool:
    palabra_eliminada = False
    if palabra in diccionario:
        del diccionario[palabra]
        palabra_eliminada = True
    return palabra_eliminada

palabras = {}
agregar_definicion(palabras, 'imagen', 'Figura, representación, semejanza y apariencia de algo')
agregar_definicion(palabras, 'toballa', 'Toalla')
agregar_definicion(palabras, 'toballa', 'Pieza de felpa')
res1 = eliminar_palabra(palabras, 'caracter')
res2 = eliminar_palabra(palabras, 'toballa')
print(res1, res2)

def eliminar_palabra(diccionario: dict, palabra: str)-> bool:
    palabra_eliminada = False
    if palabra in diccionario:
        diccionario.pop(palabra)
        palabra_eliminada = True
    return palabra_eliminada

def eliminar_palabra(diccionario: dict, palabra: str)-> bool:
    palabra_eliminada = False
    if palabra in diccionario:
        diccionario.pop(palabra)
        palabra_eliminada = True
    return palabra_eliminada

def eliminar_palabra(diccionario: dict, palabra: str)-> bool:
    palabra_eliminada = False
    if palabra in diccionario:
        definicion_eliminada = diccionario.pop(palabra)
        print("Se eliminó la llave", palabra, "que tenía la definición", definicion_eliminada)
        palabra_eliminada = True
    return palabra_eliminada

def agregar_definicion(diccionario: dict, palabra: str, definicion: str)-> None:
  diccionario[palabra] = definicion


palabras = {}
print(palabras)
{'palabra1': 'definicion1'}
agregar_definicion(palabras, 'palabra2', 'definicion2')
print(palabras)
{'palabra1': 'definicion1', 'palabra2': 'definicion2'}
