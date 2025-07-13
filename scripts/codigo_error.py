"""
Este código solicita al usuario el valor de a y b, pero tiene un error en la forma en
que se recopila la entrada del usuario y se asigna a las variables.

Se muestra en consola el mensaje "Introduzca el valor a:", pero al recopilar la entrada 
del usuario, asigna el valor ingresado a la variable valor_a.
Se imprime en consola el mensaje "Introduzca el valor b:", pero el resultado de 
print('Introduzca el valor b: ') se asigna a valor_b. Aunque muestra el mensaje, el 
valor ingresado por el usuario no se asigna a valor_b.
Se imprime el contenido de valor_a, que es el valor ingresado por el usuario en el primer paso.
Se imprime el valor de valor_b, que es None debido a la asignación incorrecta.
Finalmente, se intenta sumar valor_a y valor_b (que es None), lo cual generará un 
error porque no se pueden sumar un valor de tipo cadena con None.
Corregir el código para recopilar los valores de valor_a y valor_b de manera adecuada 
permitirá realizar la operación de suma correctamente.
"""

print('Introduzca el valor a: ')
valor_a = input()

valor_b = print('Introduzca el valor b: ')
input()

print(valor_a)
print(valor_b)

resultado = valor_a + valor_b

print(resultado)
