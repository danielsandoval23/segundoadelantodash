import dash
import dash_bootstrap_components as dbc
from dash import html
import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.dependencies import Input, Output



# Lista de departamentos de Colombia
departamentos_colombia = [
    'Amazonas', 'Antioquia', 'Arauca', 'Atlántico', 'Bolívar', 'Boyacá',
    'Caldas', 'Caquetá', 'Casanare', 'Cauca', 'Cesar', 'Chocó', 'Córdoba',
    'Cundinamarca', 'Guainía', 'Guaviare', 'Huila', 'La Guajira', 'Magdalena',
    'Meta', 'Nariño', 'Norte de Santander', 'Putumayo', 'Quindío', 'Risaralda',
    'San Andrés y Providencia', 'Santander', 'Sucre', 'Tolima', 'Valle del Cauca',
    'Vaupés', 'Vichada'
]

# Diseño de la pestaña 'Derecho'
derecho = dbc.Container([
    html.H1('Lista de Departamentos de Colombia'),
    dcc.Dropdown(
        id='departamento-dropdown',
        options=[{'label': depto, 'value': depto} for depto in departamentos_colombia],
        value=departamentos_colombia[0]
    ),
    html.Div(id='departamento-seleccionado')
])
