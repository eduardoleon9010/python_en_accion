"""

Este código utiliza la biblioteca Pandas de Python para crear una Serie a partir de datos de temperatura y 
fechas en la ciudad de Bogotá.

Esto ejecutará el código y crearía la Serie de Pandas con los datos de temperaturas en Bogotá. 
Puedes verificar la variable temperaturas en la consola de Spyder para ver los datos cargados. 
Además, podrías utilizar comandos adicionales de Pandas para realizar operaciones o visualizaciones 
específicas con estos datos.
"""

import pandas as pd

# Datos de temperaturas y fechas
datos = [19, 18, 29, 14, 20, 20, 20, 20, 19]
fechas = ["5/11/20", "6/11/20", "7/11/20", "8/11/20", "9/11/20", "10/11/20",
          "11/11/20", "12/11/20", "13/11/20"]

# Creación de la Serie de Pandas
temperaturas = pd.Series(datos, index=fechas, name="Temperaturas en Bogotá")

# Documentación:
# Este script utiliza Pandas para crear una Serie de datos de temperaturas en Bogotá.
# Se definen los datos como una lista de temperaturas y una lista de fechas.
# Estos datos se utilizan para crear una Serie de Pandas con el nombre "Temperaturas en Bogotá".

# Esta Serie tiene las fechas como índice y las temperaturas como valores.
# El parámetro 'name' especifica el nombre de la Serie.

# La Serie resultante 'temperaturas' se puede utilizar para análisis posteriores, visualización de datos o cualquier operación que se pueda realizar con Pandas Series.

# Nota: Los datos y fechas son solo ejemplos y pueden reemplazarse con datos reales.

# Por favor, asegúrate de tener la biblioteca Pandas instalada para ejecutar este script.
