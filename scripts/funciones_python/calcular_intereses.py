def calcular_interes():
    """
    Este programa solicita al usuario una cantidad de dinero en pesos, una tasa de interés (un número decimal mayor a 0)
    y un número de años. Muestra por pantalla en cuánto se habrá convertido el capital inicial transcurridos esos años si 
    cada año se aplica la tasa de interés introducida. Recuerde que un capital de C pesos a un interés del x por cien durante
    n años se convierten en C×(1+x/100)^n pesos.
    
    Ejemplo:
    Si se ingresa una cantidad de 10,000 pesos al 4.5 % de interés anual durante 20 años, el programa mostrará que esa 
    cantidad se convierte en 24117.14 pesos al cabo de 20 años.
    """

    try:
        capital = float(input("Ingrese la cantidad de dinero en pesos: "))
        tasa_interes = float(input("Ingrese la tasa de interés (en decimal, por ejemplo, 0.045 para 4.5%): "))
        anos = int(input("Ingrese el número de años: "))

        capital_final = capital * (1 + tasa_interes) ** anos

        print(f"Después de {anos} años, el capital inicial de {capital} pesos con una tasa de interés del {tasa_interes * 100}%")
        print(f"se convierte en {capital_final:.2f} pesos.")

    except ValueError:
        print("Por favor, ingrese valores numéricos válidos.")

calcular_interes()
