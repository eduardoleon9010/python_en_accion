# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 11:47:29 2024

@author: USUARIO
"""
import pandas as pd
import numpy as np

# Creamos un DataFrame de ejemplo
data = {
    'valor_pagado': np.random.randint(0, 30, 100),
    'sector': np.random.choice(['Sector A', 'Sector B', 'Sector C'], 100)
}
df = pd.DataFrame(data)

# Histograma
histograma = df['valor_pagado'].plot(kind='hist', bins=20, figsize=(10, 4), xlim=(2, 30), ylim=(0, 70), title='Histograma de valor pagado')
histograma.set_xlabel('Valor Pagado')
histograma.set_ylabel('Frecuencia')

# Diagrama de barras
diagrama_barras = df['sector'].value_counts().plot(kind='bar', fontsize=12, xlabel='Sector', ylabel='Cantidad de Contratos', title='Cantidad de Contratos por Sector')
