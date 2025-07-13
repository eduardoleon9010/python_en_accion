
"""
Este ejercicio utiliza la librería Pandas de Python para manipular un conjunto de datos 
(presumiblemente un archivo CSV llamado "peajes.csv"). Aquí está el desglose de lo que hace el código:

Importación y lectura de datos:

Utiliza Pandas para leer un archivo CSV llamado "peajes.csv" y lo almacena en un DataFrame llamado peajes.
Usa sep=";" para indicar que el separador en el archivo CSV es un punto y coma.
Análisis inicial de datos:

peajes.info() muestra información sobre el DataFrame peajes, como el tipo de datos en cada columna y si hay valores nulos.
Limpieza y llenado de valores nulos:

Los valores nulos en la columna COD_VIA, CAT4, y CAT5 son reemplazados por valores predeterminados 
('Sin Código' y 0 respectivamente).
Se identifican las filas donde INIC_OPER (presumiblemente la fecha de inicio de operación) es nula y 
se muestra información específica de esas filas.
Los valores nulos en INIC_OPER se reemplazan por '01/01/2019'.
Procesamiento de fechas:

Convierte la columna INIC_OPER (fecha de inicio de operación) a formato de fecha utilizando pd.to_datetime().
Se verifica nuevamente la información del DataFrame peajes con peajes.info() después de la conversión.
Visualización de los primeros valores de la nueva columna:

Se muestra una vista previa (los primeros valores) de la columna recién creada FECHA_INICIO_OP utilizando 
peajes['FECHA_INICIO_OP'].head().
Este código utiliza Pandas para cargar datos desde un archivo CSV, realiza manipulaciones 
como llenar valores nulos y conversiones de tipo de datos, y visualiza los cambios realizados en el DataFrame.
"""

import pandas as pd

peajes = pd.read_csv("peajes.csv", sep=";")

peajes.info()

peajes['COD_VIA'] = peajes['COD_VIA'].fillna('Sin Código ')
peajes['CAT4'] = peajes['CAT4'].fillna(0)
peajes['CAT5'] = peajes['CAT5'].fillna(0)

fechas_nulas = peajes[peajes['INIC_OPER'].isna()]
fechas_nulas[['NOMBRE','INIC_OPER','GEN']]
peajes['INIC_OPER'] = peajes['INIC_OPER'].fillna('01/01/2019')

peajes.info()

peajes['FECHA_INICIO_OP'] = pd.to_datetime(peajes['INIC_OPER'],
                                           infer_datetime_format=True,
                                           errors='coerce')

peajes.info()
peajes['FECHA_INICIO_OP'].head()

