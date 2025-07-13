# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 19:18:46 2024

@author: USUARIO
"""

import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Cargar el dataset iris
iris_df = px.data.iris()

# Inicializar la aplicación Dash
app = dash.Dash(__name__)

# Layout de la aplicación
app.layout = html.Div([
    # Título del dashboard
    html.H1("Dashboard Iris"),
    # Menú desplegable para seleccionar la especie
    dcc.Dropdown(
        id='dropdown-species',
        options=[{'label': i, 'value': i} for i in iris_df['species'].unique()],  # Opciones del menú desplegable
        value='setosa',  # Valor predeterminado del menú desplegable
        style={'width': '50%'}  # Estilo del menú desplegable
    ),
    # Gráfico de dispersión para mostrar los datos
    dcc.Graph(id='scatter-plot')
])

# Callback para actualizar el gráfico de dispersión según la especie seleccionada
@app.callback(
    Output('scatter-plot', 'figure'),  # Actualiza la figura del gráfico de dispersión
    [Input('dropdown-species', 'value')]  # Recibe el valor seleccionado del menú desplegable
)
def update_scatter_plot(selected_species):
    # Filtrar el dataframe según la especie seleccionada
    filtered_df = iris_df[iris_df['species'] == selected_species]
    # Crear un gráfico de dispersión con Plotly Express
    fig = px.scatter(filtered_df, x='sepal_width', y='sepal_length', color='species',
                     title=f'Sepal Length vs Width ({selected_species})')
    return fig

# Ejecutar la aplicación Dash
if __name__ == '__main__':
    app.run_server(debug=True)


# Abre el navegador web en la dirección http://127.0.0.1:8050/ para ver el dashboard interactivo.