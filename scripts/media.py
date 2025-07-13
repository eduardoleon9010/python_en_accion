# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 21:29:39 2024

@author: USUARIO
"""

import random

# Generar 10 valores distribuidos normalmente
mu = 10
sigma = 1.5
for _ in range(10):
    valor_generado = random.normalvariate(mu, sigma)
    print(valor_generado)
