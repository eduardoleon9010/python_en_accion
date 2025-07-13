"""
Este fragmento de código utiliza la librería Pandas para cargar datos de un archivo CSV llamado 'peajes.csv'. 
Luego, realiza algunas transformaciones en los datos cargados:

Reemplaza los valores '<Null>' en la columna 'DEP' con 'Otro'.
Reemplaza los valores 'ANTIOQUIA' (asumiendo que así se escribe) con 'Antioquia' en la columna 'DEP'.
Posteriormente, crea un gráfico de caja (boxplot) utilizando la librería Matplotlib:

Selecciona las columnas 'DEP' y 'CAT1' del DataFrame de peajes.
Crea un boxplot de la columna 'CAT1' agrupado por 'DEP'.
Define el título, etiquetas de los ejes x e y del gráfico.
Muestra el gráfico resultante.
El gráfico generado representa la distribución de la tarifa de la categoría 1 en diferentes departamentos, 
permitiendo observar la variabilidad de esta tarifa entre los departamentos presentes en los datos.
"""
import pandas as pd
import matplotlib.pyplot as plt

peajes = pd.read_csv('peajes.csv', sep=";")
peajes['DEP'] = peajes['DEP'].replace(to_replace="<Null>",
                                      value='Otro')
peajes['DEP'] = peajes['DEP'].replace(to_replace="ANTIQUIA",
                                      value='Antioquia')

#Boxplot sencillo
grafica = peajes[['DEP', 'CAT1']].boxplot(by="DEP", rot=90, figsize=(10,6))
plt.title('Tarifa Categoria 1 por Departamento')
plt.xlabel('DEPARTAMENTO')
plt.ylabel('Tarifa en pesos')
plt.show()

