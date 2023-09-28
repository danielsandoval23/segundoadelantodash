import dash
import dash_bootstrap_components as dbc

#importamos el fronted
from .navegador.navegador import navegador
from .izquierdo.izquierdo import izquierdo
from .derecho.derecho import derecho

layout = dbc.Container([
    dbc.Row([
        dbc.Col(navegador,md=12, style={"background-color" : 'grey'}),
        dbc.Col(izquierdo,md=6, style={"background-color" : 'white'}),
        dbc.Col(derecho,md=6, style={"background-color" : 'white'}),
    ])

])

