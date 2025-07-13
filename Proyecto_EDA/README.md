# Análisis Exploratorio de Datos de Inmuebles

## Descripción del Proyecto

Este proyecto tiene como objetivo llevar a cabo un análisis exploratorio de datos 
(EDA) para comprender las características y distribuciones de los inmuebles en el 
dataset proporcionado. El análisis incluye la carga y preparación de datos, 
limpieza, visualización y el estudio de las relaciones entre variables para obtener 
conclusiones significativas.

## Metodología

1. **Carga y preparación de datos**
   - Importación del dataset.
   - Conversión y limpieza de datos para asegurar su correcta utilización en el análisis.

2. **Proceso de análisis**
   - Realización de análisis descriptivos para identificar rangos, medias y desviaciones estándar.
   - Agrupamiento de datos por ciudades y tipos de inmuebles.
   - Identificación de valores atípicos.
   - Generación de visualizaciones para representar las distribuciones y relaciones entre las variables.

## Resultados

### Visualizaciones

- **Cantidad de Inmuebles por Ciudad y Tipo de Inmueble**: Muestra la distribución 
de inmuebles en diferentes ciudades y sus tipos correspondientes.
- **Número de Inmuebles por Tipo y Ciudad**: Representa el número de inmuebles 
agrupados por ciudad y tipo.
- **Mapa de Calor de Correlaciones**: Visualiza las correlaciones entre diferentes 
tipos de inmuebles y ciudades.

### Descripción de los hallazgos

- Se han identificado y documentado las características principales de los inmuebles, 
como los precios y áreas.
- Se observó una alta variabilidad en los precios y tamaños de los inmuebles.
- Se ha encontrado una concentración significativa de inmuebles en ciertas ciudades, 
con una predominancia de ciertos tipos de inmuebles.

## Instalación de librerías

Para ejecutar el análisis, asegúrate de tener instaladas las siguientes librerías:

```bash
pip install pandas plotly numpy
