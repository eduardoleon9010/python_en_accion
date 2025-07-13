# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 20:40:28 2024

@author: USUARIO
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt  # Agregamos esta línea

# Fechas de ejemplo
fechas = pd.date_range(start='2023-01-01', end='2023-03-31')

# Temperaturas simuladas en Bogotá
temperaturas = {
    '2023-01-01': 12,
    '2023-01-02': 14,
    '2023-01-03': 15,
    '2023-01-04': 13,
    '2023-01-05': 11,
    '2023-01-06': 10,
    '2023-01-07': 12,
    # Agregar más datos simulados
}

# Crear una serie de Pandas con las temperaturas y las fechas como índice
serie_temperaturas = pd.Series(temperaturas, name="Temperaturas en Bogotá")

# Graficar la serie de temperaturas
serie_temperaturas.plot(kind='line', marker='o', linestyle='-')
plt.title("Temperaturas en Bogotá")  # Corregimos el error
plt.xlabel("Fecha")
plt.ylabel("Temperatura (°C)")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
