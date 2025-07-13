# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 10:39:27 2024

@author: USUARIO
"""

import pandas as pd

# Cargar el DataFrame desde el archivo CSV
df = pd.read_csv('SECOP_II_-_Contratos_Electr_nicos.csv')

# Función para convertir pesos colombianos a dólares
def convertir_a_dolares(valor_pesos):
    tasa_cambio = 3600
    valor_dolares = valor_pesos / tasa_cambio
    return int(valor_dolares)

# Aplicar la función convertir_a_dolares a la columna 'Valor del Contrato'
df['Valor en Dólares'] = df['Valor del Contrato'].apply(convertir_a_dolares)

# Imprimir las primeras filas del DataFrame resultante
print(df.head())

