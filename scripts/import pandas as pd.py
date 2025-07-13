# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 23:21:33 2024

@author: USUARIO
"""

import pandas as pd
import numpy as np

def depurar_partidos(partidos: pd.DataFrame) -> pd.DataFrame:
    """
    Corrige los problemas en un DataFrame de partidos de fútbol.

    Args:
    partidos (DataFrame): DataFrame con las columnas 'local', 'visitante', 'goles_local', 'goles_visitante'
                          y 'resultado'. Puede contener valores nulos en las columnas de goles.

    Returns:
    DataFrame: DataFrame corregido con las columnas 'local', 'visitante', 'goles_local', 'goles_visitante' y
               'resultado'.
    """
    # Remplazar valores nulos en las cantidades de goles por 0
    partidos['goles_local'].fillna(0, inplace=True)
    partidos['goles_visitante'].fillna(0, inplace=True)

    # Eliminar partidos en los que un equipo jugó contra sí mismo
    partidos = partidos[partidos['local'] != partidos['visitante']]

    # Corregir la columna 'resultado'
    resultado_corregido = []
    for i, fila in partidos.iterrows():
        goles_local = fila['goles_local']
        goles_visitante = fila['goles_visitante']
        if goles_local > goles_visitante:
            resultado_corregido.append(fila['local'])
        elif goles_local < goles_visitante:
            resultado_corregido.append(fila['visitante'])
        else:
            resultado_corregido.append('empate')
    partidos['resultado'] = resultado_corregido

    return partidos

# Ejemplo de uso
# Crear un DataFrame de ejemplo con datos corruptos
datos = {
    'local': ['Equipo1', 'Equipo2', 'Equipo3', 'Equipo4', 'Equipo5'],
    'visitante': ['Equipo2', 'Equipo1', 'Equipo5', 'Equipo4', 'Equipo3'],
    'goles_local': [2, np.nan, 1, 3, 0],
    'goles_visitante': [3, 1, np.nan, np.nan, 2],
    'resultado': ['Equipo2', 'empate', 'Equipo5', 'Equipo4', 'Equipo3']
}
partidos_df = pd.DataFrame(datos)

# Aplicar la función para corregir los datos
partidos_corregidos_df = depurar_partidos(partidos_df)

# Mostrar el DataFrame corregido
print("Partidos corregidos:")
print(partidos_corregidos_df)
