import pandas as pd
import matplotlib.pyplot as plt

# Lectura del archivo CSV y preprocesamiento de datos
peajes = pd.read_csv('peajes.csv', sep=";")
peajes['DEP'] = peajes['DEP'].replace(to_replace="<Null>", value='Otro')
peajes['DEP'] = peajes['DEP'].replace(to_replace="ANTIQUIA", value='Antioquia')

# Selección de columnas relevantes para el análisis
tarifa_departamento = peajes[['DEP', 'CAT1', 'CAT2', 'CAT3', 'CAT4',
                              'CAT5', 'CAT6', 'CAT7']]

# Creación de diagramas de caja por categoría de tarifa y departamento
grafica = tarifa_departamento.boxplot(by="DEP", rot=90, figsize=(10, 6))

# Personalización de los gráficos generados
k = 1
for elemento in grafica:
    for i in elemento:
        i.set_title('Categoría ' + str(k))
        i.set_xlabel('Departamento')
        i.set_ylabel('Tarifa en pesos')
        k += 1

plt.show()

