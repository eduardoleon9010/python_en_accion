# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 18:23:18 2024

@author: USUARIO
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargamos el conjunto de datos Iris desde Seaborn
iris = sns.load_dataset('iris')

# Creamos la matriz de dispersión
sns.pairplot(iris, diag_kind='kde', hue='species', palette='Set2')

# Añadimos un título
plt.suptitle('Matriz de Dispersión del Conjunto de Datos Iris', y=1.02)

# Mostramos la matriz de dispersión
plt.show()
