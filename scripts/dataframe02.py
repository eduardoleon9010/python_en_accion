"""
Creación de un DataFrame desde Diccionarios de Listas en Pandas
Este código utiliza la biblioteca Pandas de Python para construir un DataFrame a 
partir de diccionarios que contienen listas de datos relacionados con registros 
de atletismo. Cada lista representa una columna de datos que incluye información 
sobre el tiempo, atleta, país, fecha y ciudad.
"""
import pandas as pd

# Listas de datos individuales
tiempos = [9.58, 9.69, 9.72, 9.74, 9.77]
atletas = ["Usain Bolt", "Usain Bolt", "Usain Bolt", "Asafa Powell", "Asafa Powell"]
paises = ["Jamaica", "Jamaica", "Jamaica", "Jamaica", "Jamaica"]
fechas = ["16/08/2009", "16/09/2008", "31/05/2008", "9/09/2007", "18/08/2006"]
ciudades = ["Berlin", "Beijing", "New York", "Rieti", "Zurich"]

# Creación del diccionario de datos
datos = {
    "tiempo": tiempos,
    "atleta": atletas,
    "pais": paises,
    "fecha": fechas,
    "ciudad": ciudades
}

# Creación del DataFrame a partir del diccionario de listas
df_records2 = pd.DataFrame(datos)


"""
Explicación:
Se definen cinco listas (tiempos, atletas, paises, fechas y ciudades), cada una 
representa una columna específica del DataFrame.
Estas listas se organizan en un diccionario llamado datos, donde cada clave del 
diccionario representa el nombre de una columna del DataFrame y los valores de 
las listas corresponden a los datos de esa columna.
Se utiliza pd.DataFrame() para crear un nuevo DataFrame llamado df_records2 a 
partir del diccionario de listas. Cada lista se convierte en una columna del DataFrame.

Este código podría ser útil como ejemplo para aquellos que trabajan con datos 
ya estructurados en listas, y desean convertir esos datos en un DataFrame en Pandas 
para análisis posteriores. Además, podrías incluir operaciones de indexación, filtrado 
o visualizaciones básicas sobre este DataFrame en el repositorio para mostrar cómo 
manipular y trabajar con estos datos en Pandas.
"""
