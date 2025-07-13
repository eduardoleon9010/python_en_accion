"""
Análisis Exploratorio de Datos con Pandas
(EDA por sus siglas en inglés: Exploratory Data Analysis)

Descripción
El siguiente código utiliza la biblioteca Pandas en Python para realizar un 
análisis exploratorio de un conjunto de datos de peajes, que se ha cargado 
desde un archivo CSV llamado "peajes.csv". Se dividen los datos en características 
categóricas y numéricas, y se realizan diversas operaciones para explorar y 
comprender la naturaleza de los datos en cada conjunto.
"""
import pandas as pd

# Carga de datos desde un archivo CSV
peajes = pd.read_csv("peajes.csv", sep=";")

# Características categóricas
categoricas = peajes[['NOMBRE', 'CONCESION','GEN',
                      'SENTIDO', 'COD_VIA', 'DEP',
                      'CONCESIONA', 'INIC_OPER',
                     'ETIQUETA']]

# Características numéricas
numericas = peajes[['CAT1', 'CAT2', 'CAT3', 'CAT4',
                    'CAT5', 'CAT6', 'CAT7',]]

# Análisis exploratorio de características categóricas
categoricas.info()
categoricas.describe()
categoricas['DEP'].unique()
categoricas['SENTIDO'].unique()
categoricas['GEN'].unique()
categoricas['DEP'].value_counts()
categoricas[['NOMBRE', 'CONCESION', 'DEP']].loc[82]

# Análisis exploratorio de características numéricas
numericas.info()
numericas.describe()
numericas.max()
numericas.idxmax()


"""
Explicación
Carga de Datos: Se importa Pandas y se carga el conjunto de datos desde un archivo CSV.
División de Datos: Se separan los datos en dos conjuntos, uno para características 
categóricas y otro para características numéricas.
Análisis Exploratorio: Se utilizan métodos de Pandas para obtener información, estadísticas 
descriptivas y valores únicos de las características categóricas. Para las numéricas, se 
calculan estadísticas descriptivas, valores máximos y sus índices.

Uso y Notas Adicionales
Estos fragmentos de código pueden servir como ejemplo para realizar un análisis exploratorio 
inicial sobre un conjunto de datos. Puedes complementar este análisis con visualizaciones, 
técnicas de limpieza de datos o cualquier otro análisis específico que sea relevante para 
tus objetivos.
"""







