# Análisis Exploratorio de Datos (EDA) en inmubles
Autor: **Ing. Leon**


## Introducción

El análisis exploratorio de datos (EDA) es una herramienta fundamental en el análisis de datos que se basa en el uso de gráficos para la visualización de conjuntos de datos. Su objetivo principal es investigar y comprender los datos, más que confirmar hipótesis estadísticas. Aunque el EDA está basado en análisis planeados, también puede implicar la limpieza de datos para analizar subgrupos o obtener una comprensión más profunda de los datos.

EDA, por sus siglas en inglés, se refiere al proceso de exploración de datos mediante resúmenes numéricos y visualización, buscando corroborar posibles relaciones entre variables y detectar anomalías. Es un proceso investigativo basado en estadísticas descriptivas y gráficos, que permite obtener un conocimiento intrínseco de los datos.

### Caso

La empresa A&A Ltda ha comenzado un proceso de implementación de Machine Learning. Usted ha sido designado para una tarea crucial dentro del proyecto: realizar el análisis exploratorio de los datos y documentar los resultados en un informe. El archivo que se analizará contiene información sobre precios de viviendas y locales para la venta, con variables relacionadas con estos valores.
"""

# Librerías necesarias para el análisis y visualización de datos

# pandas: Manipulación y análisis de datos
import pandas as pd

# numpy: Operaciones numéricas y manipulación de arrays
import numpy as np

# matplotlib.pyplot: Creación de gráficos estáticos
import matplotlib.pyplot as plt

# seaborn: Visualización de datos estadísticos con gráficos estilizados
import seaborn as sns

# plotly.express: Creación de gráficos interactivos sencillos
import plotly.express as px

# plotly.graph_objects: Personalización avanzada de gráficos interactivos
import plotly.graph_objects as go

# plotly.subplots: Creación de figuras con múltiples subgráficos
import plotly.subplots as sp

# plotly.figure_factory: Creación de gráficos avanzados, como mapas de calor
import plotly.figure_factory as ff

import plotly.io as pio

# Carga del dataset
df = pd.read_csv('/content/Data_Caso_Propuesto.csv')

# Información general del DataFrame
print("Total de registros:", df.shape[0])
print("Total de columnas:", df.shape[1])

# Mostrar nombres de columnas
print("Nombres de columnas en el DataFrame:")
print(df.columns)

# Tipos de columnas y valores nulos
print("\nDetalle de las columnas:")
print(df.info())

# Verificar valores nulos
valores_nulos = df.isnull().sum()
print("\nValores nulos por columna:")
print(valores_nulos)

# Columnas más afectadas por valores nulos
print("\nColumnas más afectadas por valores nulos:")
print(valores_nulos[valores_nulos > 0])

# Comprobación de valores duplicados
duplicados = df.duplicated().sum()
print("\nRegistros duplicados:", duplicados)

# Crear una función para clasificar el rango de precios
def clasificar_rango_precio(precio):
    if 1.534802e+07 <= precio <= 2.060800e+07:
        return 'A'
    elif 2.070134e+07 <= precio <= 2.960534e+07:
        return 'B'
    elif 4.916800e+07 <= precio <= 1.253700e+08:
        return 'C'
    else:
        return 'Fuera de Rango'

# Aplicar la función para crear la nueva columna 'Rango_precios'
df['Rango_precios'] = df['Precio'].apply(clasificar_rango_precio)

# Mostrar las primeras filas del DataFrame para verificar
print(df.head())

# Calcular los cuartiles y el IQR para identificar valores atípicos en 'Precio'
Q1 = df['Precio'].quantile(0.25)
Q3 = df['Precio'].quantile(0.75)
IQR = Q3 - Q1

# Definir los límites para los valores atípicos
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Identificar los valores atípicos en 'Precio'
outliers_precio = df[(df['Precio'] < lower_bound) | (df['Precio'] > upper_bound)]

# Mostrar los valores atípicos
print(f"Valores atípicos en 'Precio':")
print(outliers_precio[['Precio']])

# Contar los valores atípicos
print(f"Total de valores atípicos en 'Precio': {len(outliers_precio)}")

# Gráfico boxplot de los precios
fig = px.box(
    df,
    y='Precio',
    title='Boxplot de Precios con Valores Atípicos',
    labels={'Precio': 'Precio'},
    height=600
)

# Encontrar valores atípicos
q1 = df['Precio'].quantile(0.25)
q3 = df['Precio'].quantile(0.75)
iqr = q3 - q1
outliers = df[(df['Precio'] < (q1 - 1.5 * iqr)) | (df['Precio'] > (q3 + 1.5 * iqr))]

# Agregar trazas para los valores atípicos con anotaciones
fig.add_trace(
    go.Scatter(
        x=[None] * len(outliers),  # Coordenada X no está especificada para Scatter
        y=outliers['Precio'],      # Valores atípicos en el eje Y
        mode='markers+text',       # Mostrar como marcadores y texto
        text=outliers['Precio'].apply(lambda x: f'${x:,.0f}'),  # Formato de texto para los precios
        textposition='top center',
        marker=dict(color='red', size=10),  # Color rojo para resaltar los valores atípicos
        name='Valores Atípicos'
    )
)

# Actualizar diseño del gráfico
fig.update_layout(
    yaxis_title='Precio',
    boxmode='overlay',  # Superponer las cajas
    title='Boxplot de Precios con Valores Atípicos',
    showlegend=False
)

# Mostrar el gráfico
fig.show()

# Filtrar las columnas relevantes para el análisis
df_filtered = df[['Ciudad', 'Precio', 'Tipo de Inmueble', 'Estrato']].dropna()

# Convertir la columna 'Estrato' a tipo string para evitar problemas con categorías mixtas
df_filtered['Estrato'] = df_filtered['Estrato'].astype(str)

# Gráfico de cajas de precios por ciudad
fig_ciudad = px.box(
    df_filtered,
    x='Ciudad',
    y='Precio',
    title='Distribución de Precios por Ciudad',
    labels={'Precio': 'Precio', 'Ciudad': 'Ciudad'},
    height=600
)
fig_ciudad.show()

# Gráfico de cajas de precios por tipo de inmueble
fig_tipo_inmueble = px.box(
    df_filtered,
    x='Tipo de Inmueble',
    y='Precio',
    title='Distribución de Precios por Tipo de Inmueble',
    labels={'Precio': 'Precio', 'Tipo de Inmueble': 'Tipo de Inmueble'},
    height=600
)
fig_tipo_inmueble.show()

# Gráfico de cajas de precios por estrato
fig_estrato = px.box(
    df_filtered,
    x='Estrato',
    y='Precio',
    title='Distribución de Precios por Estrato',
    labels={'Precio': 'Precio', 'Estrato': 'Estrato'},
    height=600
)
fig_estrato.show()

# Visualización de Número de Inmuebles por Ciudad, Número de Inmuebles por Tipo de Inmueble
# Contar el número de inmuebles por ciudad
inmuebles_por_ciudad = df['Ciudad'].value_counts().reset_index()
inmuebles_por_ciudad.columns = ['Ciudad', 'Número de Inmuebles']

# Contar el número de inmuebles por tipo de inmueble
inmuebles_por_tipo = df['Tipo de Inmueble'].value_counts().reset_index()
inmuebles_por_tipo.columns = ['Tipo de Inmueble', 'Número de Inmuebles']

# Crear subplots
fig = sp.make_subplots(rows=1, cols=2, subplot_titles=('Número de Inmuebles por Ciudad', 'Número de Inmuebles por Tipo'))

# Gráfico de barras para el número de inmuebles por ciudad
fig.add_trace(
    go.Bar(x=inmuebles_por_ciudad['Ciudad'], y=inmuebles_por_ciudad['Número de Inmuebles'], name='Inmuebles por Ciudad'),
    row=1, col=1
)

# Gráfico de barras para el número de inmuebles por tipo de inmueble
fig.add_trace(
    go.Bar(x=inmuebles_por_tipo['Tipo de Inmueble'], y=inmuebles_por_tipo['Número de Inmuebles'], name='Inmuebles por Tipo de Inmueble'),
    row=1, col=2
)

# Actualizar diseño
fig.update_layout(
    title_text='Distribución de Inmuebles por Ciudad y por Tipo',
    height=600,
    width=1200,
    xaxis_title='Ciudad',
    yaxis_title='Número de Inmuebles',
    xaxis2_title='Tipo de Inmueble',
    yaxis2_title='Número de Inmuebles',
    showlegend=False,
    xaxis=dict(tickangle=-45),  # Rotar etiquetas del eje x para mejor visualización
    xaxis2=dict(tickangle=-45)  # Rotar etiquetas del eje x para mejor visualización
)

# Mostrar los gráficoS
fig.show()

# Histograma para el número de inmuebles por ciudad
ciudad_counts = df['Ciudad'].value_counts()

# Creación del histograma con colores más vivos
fig_ciudad = go.Figure(data=[go.Histogram(x=df['Ciudad'], histfunc='count', name='Número de Inmuebles')])
fig_ciudad.update_traces(marker=dict(color='rgb(0, 204, 150)', line=dict(width=1, color='rgb(0, 0, 0)')))

# Actualización del diseño del histograma
fig_ciudad.update_layout(
    title='Número de Inmuebles por Ciudad',
    xaxis_title='Ciudad',
    yaxis_title='Número de Inmuebles',
    height=400,
    xaxis=dict(
        title='Ciudad',
        tickangle=-45  # Rotar etiquetas del eje x para mejor visualización
    ),
    yaxis=dict(
        title='Número de Inmuebles'
    )
)

# Mostrar el gráfico
fig_ciudad.show()

# Histograma para el número de inmuebles por tipo de inmueble
tipo_counts = df['Tipo de Inmueble'].value_counts()

# Creación del histograma con colores más vivos
fig_tipo = go.Figure(data=[go.Histogram(x=df['Tipo de Inmueble'], histfunc='count', name='Número de Inmuebles')])
fig_tipo.update_traces(marker=dict(color='rgb(255, 100, 100)', line=dict(width=1, color='rgb(0, 0, 0)')))

# Actualización del diseño del histograma
fig_tipo.update_layout(
    title='Número de Inmuebles por Tipo de Inmueble',
    xaxis_title='Tipo de Inmueble',
    yaxis_title='Número de Inmuebles',
    height=400,
    xaxis=dict(
        title='Tipo de Inmueble',
        tickangle=-45  # Rotar etiquetas del eje x para mejor visualización
    ),
    yaxis=dict(
        title='Número de Inmuebles'
    )
)

# Mostrar el gráfico
fig_tipo.show()

# Grafico de barras interactivo.
# Agrupamiento de los datos
conteo_inmuebles = df.groupby(["Ciudad", "Tipo de Inmueble"]).size().reset_index(name='Cantidad')

# Crear el gráfico interactivo
fig = px.bar(conteo_inmuebles,
             x='Ciudad',
             y='Cantidad',
             color='Tipo de Inmueble',
             title='Cantidad de Inmuebles por Ciudad y Tipo de Inmueble',
             labels={'Cantidad': 'Número de Inmuebles'},
             height=600)

# Ajuste del diseño para una mejor visualización
fig.update_layout(
    xaxis_title='Ciudad',
    yaxis_title='Número de Inmuebles',
    coloraxis_colorbar_title='Tipo de Inmueble'
)

# Mostrar el gráfico
fig.show()

# Gráfico de dispersion
df['Area Construida'] = pd.to_numeric(df['Area Construida'], errors='coerce')
df['Precio'] = pd.to_numeric(df['Precio'], errors='coerce')

# Agrupamiento por ciudad y tipo de inmueble y contar el número de inmuebles
df_grouped = df.groupby(['Ciudad', 'Tipo de Inmueble']).size().reset_index(name='Número de Inmuebles')

# Gráfico de dispersión interactivo
fig = px.scatter(df_grouped,
                 x='Ciudad',
                 y='Tipo de Inmueble',
                 size='Número de Inmuebles',  # Tamaño de los puntos basado en la cantidad de inmuebles
                 color='Tipo de Inmueble',    # Diferenciar los tipos de inmueble por color
                 title='Número de Inmuebles por Ciudad y Tipo de Inmueble',
                 labels={'Ciudad': 'Ciudad', 'Tipo de Inmueble': 'Tipo de Inmueble', 'Número de Inmuebles': 'Número de Inmuebles'},
                 height=600,
                 size_max=30)  # Ajustar tamaño máximo para mejor visualización

# Mostrar el gráfico
fig.show()

# Scatter plot: Precio vs. Área Construida (en lugar de metros_cuadrados)
# Gráfico de dispersión interactivo
fig = px.scatter(df,
                 x='Area Construida',
                 y='Precio',
                 color='Tipo de Inmueble',
                 title='Precio vs Área Construida',
                 labels={'Area Construida': 'Área Construida', 'Precio': 'Precio'},
                 height=600)

# Mostrar el gráfico
fig.show()

# Contar la cantidad de inmuebles por tipo y ciudad
df_counts = df.groupby(['Ciudad', 'Tipo de Inmueble']).size().reset_index(name='Cantidad')

# Gráfico de dispersión
fig = px.scatter(
    df_counts,
    x='Ciudad',
    y='Cantidad',
    color='Tipo de Inmueble',
    size='Cantidad',
    title='Cantidad de Inmuebles por Tipo en Cada Ciudad',
    labels={'Cantidad': 'Número de Inmuebles', 'Ciudad': 'Ciudad'},
    height=600
)

# Actualizacion diseño del gráfico
fig.update_layout(
    xaxis_title='Ciudad',
    yaxis_title='Número de Inmuebles',
    legend_title='Tipo de Inmueble',
    xaxis=dict(tickangle=-45)  # Rotar etiquetas del eje x para mejor visualización
)

# Mostrar el gráfico
fig.show()

# Tabla de contingencia de número de inmuebles por ciudad y tipo de inmueble
contingency_table = pd.crosstab(df['Ciudad'], df['Tipo de Inmueble'])

# Matriz de correlación
corr_matrix = contingency_table.corr()

# Mapa de calor usando Plotly con la escala de colores 'Electric' para un estilo fluorescente
fig = go.Figure(data=go.Heatmap(
    z=corr_matrix.values,
    x=corr_matrix.columns.tolist(),
    y=corr_matrix.columns.tolist(),
    colorscale='Electric',  # Escala de colores fluorescente 'Electric'
    zmin=-1,
    zmax=1,
    colorbar=dict(title='Correlación'),
    text=corr_matrix.round(2).values,  # Usar valores redondeados para las anotaciones
    hoverinfo='text'  # Mostrar solo las anotaciones en hover
))

# Actualización del diseño del gráfico
fig.update_layout(
    title='Mapa de Calor de Correlaciones entre Tipos de Inmuebles y Ciudades',
    xaxis_title='Tipos de Inmuebles',
    yaxis_title='Ciudades',
    xaxis=dict(tickangle=-45),
    yaxis=dict(tickangle=0),
    height=600
)

# Mostrar el gráfico
fig.show()

# Número total de inmuebles por ciudad
inmuebles_por_ciudad = df['Ciudad'].value_counts().reset_index()
inmuebles_por_ciudad.columns = ['Ciudad', 'Número de Inmuebles']

# Mostrar resultados en la consola
print("Número total de inmuebles por ciudad:")
print(inmuebles_por_ciudad)

# Número de inmuebles por tipo en cada ciudad
inmuebles_por_tipo_ciudad = df.groupby(['Ciudad', 'Tipo de Inmueble']).size().reset_index(name='Número de Inmuebles')

# Mostrar resultados en la consola
print("\nNúmero de inmuebles por tipo en cada ciudad:")
print(inmuebles_por_tipo_ciudad)

# Número total de inmuebles por tipo
inmuebles_por_tipo = df['Tipo de Inmueble'].value_counts().reset_index()
inmuebles_por_tipo.columns = ['Tipo de Inmueble', 'Número de Inmuebles']

# Mostrar resultados en la consola
print("\nNúmero total de inmuebles por tipo:")
print(inmuebles_por_tipo)

# Opcional: Guardar los resultados en archivos CSV
inmuebles_por_ciudad.to_csv('inmuebles_por_ciudad.csv', index=False)
inmuebles_por_tipo_ciudad.to_csv('inmuebles_por_tipo_ciudad.csv', index=False)
inmuebles_por_tipo.to_csv('inmuebles_por_tipo.csv', index=False)

# Conclusiones

El análisis exploratorio de datos revela una alta variabilidad en los precios y tamaños de los inmuebles, con una notable concentración en ciertas ciudades. Se identificaron un total de 463 inmuebles en el dataset, clasificados en siete tipos distintos. El tipo "LOCAL" es el más prevalente, con 305 inmuebles, mientras que otros tipos como "LOTE VIVIENDA" y "BODEGA" tienen menos representación.

En términos de distribución por ciudad, VILLAVICENCIO destaca con 290 inmuebles, lo que sugiere una mayor actividad en esa área. En Calima del Darien, el tipo "LOTE CON VIVIENDA" es el más frecuente, con nueve inmuebles. Cali también presenta una cantidad significativa de inmuebles, especialmente del tipo "LOCAL".

Las visualizaciones han proporcionado una comprensión clara de las distribuciones y relaciones entre las variables del dataset, permitiendo una evaluación exhaustiva del mercado inmobiliario.
