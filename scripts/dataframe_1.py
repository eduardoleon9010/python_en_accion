# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 21:12:05 2024

@author: USUARIO
"""

import pandas as pd

# Definir los diccionarios con la información de los récords mundiales
a1 = {'tiempo': 9.58, 'atleta': 'Usain Bolt', 'país': 'Jamaica', 'fecha': '16/08/2009', 'ciudad': 'Berlín'}
a2 = {'tiempo': 19.19, 'atleta': 'Usain Bolt', 'país': 'Jamaica', 'fecha': '20/08/2009', 'ciudad': 'Berlín'}
a3 = {'tiempo': 12.80, 'atleta': 'Kenenisa Bekele', 'país': 'Etiopía', 'fecha': '23/08/2009', 'ciudad': 'Berlín'}
a4 = {'tiempo': 47.60, 'atleta': 'Kevin Young', 'país': 'Estados Unidos', 'fecha': '06/08/1992', 'ciudad': 'Barcelona'}
a5 = {'tiempo': 121.39, 'atleta': 'Eliud Kipchoge', 'país': 'Kenia', 'fecha': '16/09/2018', 'ciudad': 'Berlín'}

# Crear una lista de diccionarios con la información de los récords
récords = [a1, a2, a3, a4, a5]

# Crear un DataFrame a partir de la lista de diccionarios
df_records1 = pd.DataFrame(récords)

print(df_records1)
