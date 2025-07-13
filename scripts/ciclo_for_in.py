"""
Esta función comprueba si un número es primo o no.

Recibe un número numero como argumento.
Comienza asumiendo que el número es primo, estableciendo la variable primo en True.
Luego, realiza un bucle for que itera desde 2 hasta numero - 1 (exclusivo).
En cada iteración del bucle, verifica si numero es divisible por i (resto de la división igual a cero). 
Si lo es, actualiza primo a False, indicando que el número no es primo.
Retorna el valor de primo después de completar el bucle.
Por lo tanto, para que la función verifique correctamente si un número es primo, debería tener un 
condicional que interrumpa la iteración y devuelva False en el momento en que se encuentre un divisor 
válido, es decir, cuando numero % i == 0. Si el bucle termina sin encontrar ningún divisor, entonces el 
número es primo y se devuelve True
"""

def es_numero_primo(numero: int) -> bool:
    if numero <= 1:
        return False  # 0 y 1 no son primos

    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False  # Encontró un divisor, no es primo

    return True  # No se encontraron divisores, es primo

"""Esta versión utiliza la optimización de buscar divisores solo hasta la raíz cuadrada del número, 
lo cual es suficiente para verificar si un número es primo """
