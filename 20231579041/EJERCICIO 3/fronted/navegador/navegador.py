import dash
import dash_bootstrap_components as dbc
from dash import html

navegador = dbc.Container([
    html.H2('COLEGIOS AFECTADOS POR INUDACIONES'),
    html.Hr(),
    html.H6('Andres Felipe Diaz-20231579057'),
    html.H6('Juan Daniel Sandoval-20231579041'),
    html.H6('Nestor Javier Florez-20231579058'),
    dbc.Row([
        dbc.Col(["visualizacion"],md=3, style={'background-colo':'grey'}),
        dbc.Col(["texto"],md=6, style={'background-colo':'gray'}),
        dbc.Col(["usuario"],md=3, style={'background-colo':'yellow'}),

    ])


])