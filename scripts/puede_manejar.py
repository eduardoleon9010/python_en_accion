# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 02:10:39 2024

@author: USUARIO
"""
def evaluar_salud(altura: float, peso: float) -> str:
    """
    Evalúa la salud de un adulto según su altura y peso utilizando el Índice de Masa Corporal (IMC).
    
    Parámetros:
    altura (float): Altura en metros.
    peso (float): Peso en kilogramos.
    
    Retorno:
    (str): Mensaje que indica la categoría de salud del adulto.
    """
    # Calcular el Índice de Masa Corporal (IMC)
    imc = peso / (altura ** 2)
    
    # Determinar la categoría de salud
    if imc >= 25:
        return "Tiene sobrepeso."
    elif imc < 18.5:
        return "Está bajo de peso."
    else:
        return "Está dentro del rango saludable."

# Ejemplo de uso de la función
altura_usuario = float(input("Ingrese la altura en metros: "))
peso_usuario = float(input("Ingrese el peso en kilogramos: "))

resultado_salud = evaluar_salud(altura_usuario, peso_usuario)
print(resultado_salud)
