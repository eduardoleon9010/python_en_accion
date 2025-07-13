# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 12:19:15 2024

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

# Creamos una serie con la cantidad de contratos por sector
contratos_por_sector = df['sector'].value_counts()

# Creamos el diagrama de barras
diagrama_barras = contratos_por_sector.plot(kind='bar', fontsize=12, xlabel='Sector', ylabel='Cantidad de Contratos', title='Cantidad de Contratos por Sector')
