# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 08:11:23 2024

@author: USUARIO
"""

def es_pokemon_seudolegendario(pokemon):
    """
    Determina si un Pokémon es seudolegendario basándose en la suma de sus estadísticas de combate.

    Args:
    - pokemon (dict): Un diccionario que representa un Pokémon, con las siguientes llaves:
                      "nombre": (str) el nombre del Pokémon.
                      Las llaves restantes son las estadísticas de combate del Pokémon:
                      "vida": (int), "ataque": (int), "defensa": (int),
                      "ataque_especial": (int), "defensa_especial": (int),
                      "velocidad": (int).

    Returns:
    - bool: True si el Pokémon es seudolegendario (la suma de sus estadísticas de combate es >= 600),
            False de lo contrario.
    """
    total_estadisticas = sum(valor for clave, valor in pokemon.items() if clave != 'nombre')
    return total_estadisticas >= 600


def construir_equipo_pokemon(cantidad, lista_pkmn):
    """
    Construye un equipo de Pokémones seudolegendarios para la batalla.

    Args:
    - cantidad (int): La cantidad de pokémones que se utilizarán en la batalla. Debe ser un número entre 3 y 6.
    - lista_pkmn (list): Una lista de diccionarios, donde cada diccionario representa un Pokémon. 
                         Cada diccionario tiene las siguientes llaves:
                         "nombre": (str) el nombre del Pokémon.
                         Las llaves restantes son las estadísticas de combate del Pokémon:
                         "vida": (int), "ataque": (int), "defensa": (int),
                         "ataque_especial": (int), "defensa_especial": (int),
                         "velocidad": (int).

    Returns:
    - list or None: Una lista con los nombres de los pokémones que formarán el equipo si es posible formar un equipo
                    de pokémones seudolegendarios. None si no es posible formar un equipo de pokémones seudolegendarios.
    """
    # Comprobar que la cantidad de pokémones es válida
    if cantidad < 3 or cantidad > 6:
        return None
    
    # Obtener todos los subconjuntos de la lista de pokémones
    from itertools import combinations
    for equipo_actual in combinations(lista_pkmn, cantidad):
        # Verificar si el equipo actual cumple con las condiciones
        if all(es_pokemon_seudolegendario(pokemon) for pokemon in equipo_actual):
            return [pokemon['nombre'] for pokemon in equipo_actual]
    
    # Si no se encontró ningún equipo válido, retornar None
    return None

# Ejemplo de uso
if __name__ == "__main__":
    # Lista de Pokémones
    lista_pokemon = [
        {"nombre": "Mewtwo", "vida": 106, "ataque": 110, "defensa": 90, "ataque_especial": 154, "defensa_especial": 90, "velocidad": 130},
        {"nombre": "Articuno", "vida": 90, "ataque": 85, "defensa": 100, "ataque_especial": 95, "defensa_especial": 125, "velocidad": 85},
        {"nombre": "Zapdos", "vida": 90, "ataque": 90, "defensa": 85, "ataque_especial": 125, "defensa_especial": 90, "velocidad": 100},
        {"nombre": "Raikou", "vida": 90, "ataque": 85, "defensa": 75, "ataque_especial": 115, "defensa_especial": 100, "velocidad": 115},
        {"nombre": "Latios", "vida": 80, "ataque": 90, "defensa": 80, "ataque_especial": 130, "defensa_especial": 110, "velocidad": 110},
        {"nombre": "Latias", "vida": 80, "ataque": 80, "defensa": 90, "ataque_especial": 110, "defensa_especial": 130, "velocidad": 110}
    ]

    cantidad_pokemon = 4

    equipo_pokemon = construir_equipo_pokemon(cantidad_pokemon, lista_pokemon)

    if equipo_pokemon:
        print("Ash puede formar un equipo con los siguientes Pokémones seudolegendarios:")
        print(equipo_pokemon)
    else:
        print("No es posible formar un equipo de Pokémones seudolegendarios para la batalla.")


