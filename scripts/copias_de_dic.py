## Función para Agregar Definición con Copia

Este código define una función `agregar_definicion_con_copia` que agrega una nueva palabra y su definición a un diccionario existente y devuelve una copia del diccionario actualizado.

```python
def agregar_definicion_con_copia(diccionario: dict, palabra: str, definicion: str) -> dict:
    """
    Agrega una nueva palabra y su definición a un diccionario y devuelve una copia actualizada del diccionario.

    Args:
    - diccionario (dict): Diccionario original al que se le agregará la nueva palabra y definición.
    - palabra (str): Palabra a agregar al diccionario.
    - definicion (str): Definición correspondiente a la palabra a agregar.

    Returns:
    - dict: Copia actualizada del diccionario con la nueva palabra y definición.
    """
    copia = diccionario.copy()  # Se crea una copia del diccionario original
    copia[palabra] = definicion  # Se agrega la nueva palabra y definición a la copia
    return copia  # Se devuelve la copia actualizada del diccionario

# Diccionario original de palabras y definiciones
palabras = {'palabra1': 'definicion1', 'palabra2': 'definicion2'}

# Se agrega una nueva palabra y definición usando la función definida
copia_palabras = agregar_definicion_con_copia(palabras, 'p99', 'def99')

# Resultados:
# El diccionario original no se modifica
print(palabras)  # Output: {'palabra1': 'definicion1', 'palabra2': 'definicion2'}
# La copia del diccionario ahora contiene la nueva palabra y definición
print(copia_palabras)  # Output: {'palabra1': 'definicion1', 'palabra2': 'definicion2', 'p99': 'def99'}
