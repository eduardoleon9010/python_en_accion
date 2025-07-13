"""
La función insertar_ordenado en tu código está diseñada para mantener una lista ordenada mientras se agregan elementos. 
Cada vez que ingresas una cadena, se usa esta función para insertarla en la lista, manteniendo el orden. Al ingresar 
'terminar', el bucle se detiene y la lista resultante se imprime.

La salida muestra que las cadenas se han insertado de manera que la lista se mantiene ordenada alfabéticamente. 
Por ejemplo, "carro" viene antes que "gf", y "jose" viene antes que "rrope". Si se inserta 'terminar', se detiene 
el proceso y se imprime la lista ordenada hasta ese momento.

Esta función puede ser útil cuando necesitas mantener una lista ordenada y agregar elementos a ella mientras se 
mantiene este orden
"""

def insertar_ordenado(lista_ordenada: list, cadena: str) -> list:
    i = 0
    
    while i < len(lista_ordenada) and cadena > lista_ordenada[i]:
        i += 1
        
    lista_ordenada.insert(i, cadena)
    
    return lista_ordenada

# Lista vacía para almacenar las cadenas
lista = []

# Ingresar cadenas hasta que se escriba 'terminar'
palabra = input("Ingrese una cadena, o 'terminar' para cerrar: ")
        
while palabra != 'terminar':
    insertar_ordenado(lista, palabra)
    palabra = input("Ingrese una cadena, o 'terminar' para cerrar: ")                  
                      
print(lista)

