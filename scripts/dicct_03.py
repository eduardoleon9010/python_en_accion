"""
Gestor de Información de Celulares
Descripción
Este conjunto de funciones en Python permite crear, gestionar y comparar información de celulares. 
Incluye funciones para crear diccionarios que representan celulares con sus especificaciones técnicas, 
comparar las cámaras de dos celulares, verificar la existencia de ciertas versiones de sistemas 
operativos en los celulares, y obtener información sobre los celulares mediante sus nombres
"""
def crear_celular(procesador: float, memoria: float, camara: float, 
                  pantalla: str, ancho: int, alto: int, pila: float, 
                  sistema: str, version: str)->dict:
  nuevo_celular = {}
  nuevo_celular['procesador'] = procesador
  nuevo_celular['memoria'] = memoria
  nuevo_celular['camara'] = camara
  nuevo_celular['pantalla'] = pantalla
  nuevo_celular['ancho'] = ancho
  nuevo_celular['alto'] = alto
  nuevo_celular['pila'] = pila
  nuevo_celular['sistema'] = sistema
  nuevo_celular['version'] = version
  return nuevo_celular


cel1 = crear_celular(2.4, 64, 48, 'OLED', 1080, 2400, 5000, 'Android', '10')
cel2 = crear_celular(2.2, 64, 32, 'OLED', 768, 1080, 3500, 'Android', '8.1')
cel3 = crear_celular(2.0, 32, 18, 'Retina', 375, 812, 4200, 'iOS', '9.0')
cel4 = crear_celular(1.8, 16, 6, 'Retina', 375, 667, 4150, 'iOS', '8.1.4')

def mejor_camara(celular1: dict, celular2: dict)-> int:
    """ Busca cuál de los dos celulares tiene la mejor cámara (más mega-pixeles).
    Para que se pueda usar la función, los celulares deben representarse con 
    diccionarios que tengan una llave llamada 'camara' que indique la cantidad
    de mega-pixeles de la cámara del celular.    
    Parámetros:
      celular1 (dict): Es un diccionario que representa al primer celular. 
      celular2 (dict): Es un diccionario que representa al segundo celular.
    Retorno:
      (int): Retorna 1 si el primer celular tiene la mejor cámara.
             Retorna 2 si el segundo celular tiene la mejor cámara.
             Retorna 0 si las cámaras de los dos celulares son iguales.
    """
    mejor = 0
    camara1 = celular1['camara']
    camara2 = celular2['camara']    
    if camara1 > camara2:
        mejor = 1
    elif camara1 < camara2:
        mejor = 2
    return mejor

mejor_camara(cel1, cel2)
1
mejor_camara(cel1, cel1)
0
mejor_camara(cel3, cel2)
2

def hay_celular_version_so(cel1: dict, cel2: dict, cel3: dict, cel4: dict, so: str, version: str) -> bool:
    """ Esta función indica si hay algún celular con la versión del sistema operativo
        indicada en los parámetros 'so' y 'version'.
        La función espera que los diccionarios de los celulares tengan una llave llamada
        'sistema' con el nombre del sistema operativo y una llave llamada 'version' con
        la versión del sistema.
    Parámetros:
      cel1 (dict): El diccionario que representa el primer celular
      cel2 (dict): El diccionario que representa el segundo celular
      cel3 (dict): El diccionario que representa el tercer celular
      cel4 (dict): El diccionario que representa el cuarto celular
    Retorno:
      (bool) : Retorna True si algún celular tiene exactamente el mismo sistema operativo
               en la misma versión que se pide en los parámetros 'so' y 'version'.
               Retorna False de lo contrario.
    """
    hay_celular_buscado = False
    if cel1['sistema'] == so and cel1['version'] == version:
        hay_celular_buscado = True
    elif cel2['sistema'] == so and cel2['version'] == version:
        hay_celular_buscado = True
    elif cel3['sistema'] == so and cel3['version'] == version:
        hay_celular_buscado = True
    elif cel4['sistema'] == so and cel4['version'] == version:
        hay_celular_buscado = True    
    return hay_celular_buscado

def contar_celulares_version_so(cel1: dict, cel2: dict, cel3: dict, cel4: dict, so: str, version: str) -> int:
    """ Esta función cuenta cuántos celulares tienen la versión del sistema operativo
        indicada en los parámetros 'so' y 'version'.
        La función espera que los diccionarios de los celulares tengan una llave llamada
        'sistema' con el nombre del sistema operativo y una llave llamada 'version' con
        la versión del sistema.
    Parámetros:
      cel1 (dict): El diccionario que representa el primer celular
      cel2 (dict): El diccionario que representa el segundo celular
      cel3 (dict): El diccionario que representa el tercer celular
      cel4 (dict): El diccionario que representa el cuarto celular
    Retorno:
      (bool) : Retorna la cantidad de celulares que tienen exactamente el mismo 
               sistema operativo en la misma versión que se pide en los 
               parámetros 'so' y 'version'.
    """
    cantidad_celulares = 0
    if cel1['sistema'] == so and cel1['version'] == version:
        cantidad_celulares += 1
    if cel2['sistema'] == so and cel2['version'] == version:
        cantidad_celulares += 1
    if cel3['sistema'] == so and cel3['version'] == version:
        cantidad_celulares += 1
    if cel4['sistema'] == so and cel4['version'] == version:
        cantidad_celulares += 1
    return cantidad_celulares
celulares = {}
celulares['AmazingCel'] = cel1
celulares['BoringCel'] = cel2
celulares['CheapCel'] = cel3
celulares['DumbCel'] = cel4


print(celulares['AmazingCel'])

print(celulares['AmazingCel']['procesador'])

def mejor_camara_con_nombres(celulares: dict, nombre1: str, nombre2: dict)-> str:
    """ Busca cuál de los dos celulares tiene la mejor cámara
    Parámetros:
      celulares (dict): Un diccionario donde las llaves son los nombres de los celulares
                        y los valores son diccionarios que representan celulares
      nombre1 (str): El nombre del primer celular que se quiere comparar
      nombre2 (str): El nombre del segundo celular que se quiere comparar
    Retorno:
      (str): Retorna el nombre del celular que tiene la mejor cámara o "Empate" si
             las cámaras de los dos celulares son iguales.
             Si sólo uno de los nombres corresponde al de un celular, retorna ese nombre.
             Si ningún nombre corresponde al de un celular, retorna "Nombres inválidos".
    """
    # Extraer los celulares del diccionario usando su nombre
    celular1 = celulares.get(nombre1, None)
    celular2 = celulares.get(nombre2, None)
    # Ninguno de los dos nombres era correcto
    if celular1 is None and celular2 is None:
        nombre_mejor = "Nombres inválidos"
    # Sólo el segundo nombre era correcto
    elif celular1 is None and celular2 is not None:
        nombre_mejor = nombre2
    # Sólo el primer nombre era correcto
    elif celular1 is not None and celular2 is None:
        nombre_mejor = nombre1
    # Los dos nombres eran correctos así que hay que comparar los celulares
    else:
        nombre_mejor = "Empate"
        numero_mejor = mejor_camara(celular1, celular2)
        if numero_mejor == 1:
            nombre_mejor = nombre1
        elif numero_mejor == 2:
            nombre_mejor = nombre2
    return nombre_mejor

# Ejemplos de uso de las funciones
print(mejor_camara_con_nombres(celulares, 'DumbCel', 'BoringCel'))
print(mejor_camara_con_nombres(celulares, 'DumbCel', 'FalseCel'))
print(mejor_camara_con_nombres(celulares, 'FalsestCel', 'FalseCel'))
print(mejor_camara_con_nombres(celulares, 'CheapCel', 'CheapCel'))



"""
Funciones Principales
crear_celular: Crea un diccionario que representa un celular con sus especificaciones técnicas.
mejor_camara: Compara las cámaras de dos celulares y devuelve cuál tiene la mejor cámara.
hay_celular_version_so: Verifica si hay algún celular con una versión específica de sistema operativo.
contar_celulares_version_so: Cuenta cuántos celulares tienen una versión específica de sistema operativo.
mejor_camara_con_nombres: Compara las cámaras de dos celulares mediante sus nombres.

Uso y Notas Adicionales
Este código puede ser utilizado para gestionar información sobre celulares. Las funciones permiten comparar 
características específicas de los celulares, verificar la existencia de ciertas versiones de sistemas 
operativos y obtener información detallada mediante los nombres de los celulares.
"""






































