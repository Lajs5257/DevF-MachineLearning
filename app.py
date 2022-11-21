# Importacion de nuestras dependencias
from jupyter_dash import JupyterDash # Versión de dash para notebooks
from dash import dcc # Componentes HTML preconstruidos para dashboards
from dash import html # Componentes HTML nativos
from dash.dependencies import Input, Output # Clases Input y Output
import plotly.express as px # Generar gráficas e importar datasets con Plotly
import pandas as pd # Recolección y manipulación de datos
import requests # Hacer peticiones HTTP
import numpy as np # Operaciones matemáticas
import matplotlib.pyplot as plt # Generar gráficas
import seaborn as sns # Generar gráficas
import plotly.graph_objects as go # Generar gráficas
from sklearn.model_selection import train_test_split # Separar datos en entrenamiento y prueba
from sklearn.preprocessing import MinMaxScaler # Escalar datos
from sklearn.cluster import KMeans # Clustering
import time # Medir tiempo de ejecución
from dash import Dash # Versión de dash para servidores

# Función para obtener los datos de la API





# Le damos estilo a la aplicación
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
colors = {
    'background': '#282b2d',
    'text': '#ccd3d6',
    'titulo': '#ffffff',
}

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Proyecto Final - Machine Learning',
        style={
            'textAlign': 'center',
            'color': colors['titulo'],
            'font-weight': 'bold',
        }
    ),
    html.H2(children='Análisis de datos de la API de INEGI', style={
        'textAlign': 'center',
        'color': colors['text']}),
    html.H2(children='Alumno: Luis Alberto Jiménez Soto', style={
        'textAlign': 'center',
        'color': colors['text']}),

    html.H4(children='Este proyecto consiste en la determinar la mejor ubicación para abrir un restaurante de nuestra comida favorita.',
        style={
            'color': colors['text']
        }
        ),
    #Lista de objetivos a lograr
    html.H4(children='Objetivos:',
            style={
                'color': colors['text'],
                'font-weight': 'bold',
                'font-size': 20,}),
    html.Ul(children='1. Utilizando variables demográficas realicen un modelo supervisado donde su variable objetivo sea el número de puestos de su comida favorita.',style={'color': colors['text']}),
    html.Ul(children='2. Deberán crear sus variables independientes usando el Estado y el CP como llaves para cruzar',style={'color': colors['text']}),
    html.Ul(children='3. Usen al menos 50 variables para su tabla y con algunas de ellas realicen un modelo NO supervisado (KMedias) para perfilar a cada uno de los códigos postales de la república.',style={'color': colors['text']}),
    html.Ul(children='4. Entrenen un modelo usando el cluster y el resto de variables para predecir su Variable Objetivo. (Usar Grid Search y Cross Validation)',style={'color': colors['text']}),
    html.Ul(children='5. Determinen 10 lugares en donde colocarían su puesto de comida.',style={'color': colors['text']}),
    html.Ul(children='6. Determina las 5 variables que más influyen.',style={'color': colors['text']}),

    
])

if __name__ == '__main__':
    app.run_server(debug=True)