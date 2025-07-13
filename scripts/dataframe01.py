"""
Creación de un DataFrame a partir de diccionarios en Pandas
El código utiliza la biblioteca Pandas en Python para crear un DataFrame a partir de una lista de diccionarios 
que contienen datos de registros de atletismo. Cada diccionario representa un registro individual con detalles 
como el tiempo, el atleta, el país, la fecha y la ciudad.

"""
import pandas as pd

# Definición de los diccionarios que representan los registros
a1 = {"tiempo": 9.58, "atleta": "Usain Bolt", "pais": "Jamaica", "fecha": "16/08/2009", "ciudad": "Berlin"}
a2 = {"tiempo": 9.69, "atleta": "Usain Bolt", "pais": "Jamaica", "fecha": "16/09/2008", "ciudad": "Beijing"}
a3 = {"tiempo": 9.72, "atleta": "Usain Bolt", "pais": "Jamaica", "fecha": "31/05/2008", "ciudad": "New York"}
a4 = {"tiempo": 9.74, "atleta": "Asafa Powell", "pais": "Jamaica", "fecha": "9/09/2007", "ciudad": "Rieti"}
a5 = {"tiempo": 9.77, "atleta": "Asafa Powell", "pais": "Jamaica", "fecha": "18/08/2006", "ciudad": "Zurich"}

# Lista que contiene los diccionarios de registros
records = [a1, a2, a3, a4, a5]

# Creación del DataFrame a partir de la lista de diccionarios
df_records = pd.DataFrame(records)

"""
Explicación:
Se importa la biblioteca Pandas como pd.
Se definen cinco diccionarios (a1 a a5), cada uno representando un registro con detalles específicos del atleta, 
tiempo, país, fecha y ciudad.
Estos diccionarios se almacenan en una lista llamada records.
Se utiliza pd.DataFrame() para crear un DataFrame llamado df_records a partir de la lista de diccionarios. 
Cada diccionario se convierte en una fila en el DataFrame, donde las claves del diccionario se convierten en columnas.
El repositorio de GitHub podría contener este código como un ejemplo de cómo crear un DataFrame desde datos 
estructurados en diccionarios utilizando Pandas en Python. Además, podrías incluir ejemplos de operaciones 
comunes sobre este DataFrame, como filtrado, selección de columnas o cálculos estadísticos sobre los tiempos registrados.
