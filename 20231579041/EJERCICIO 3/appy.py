import dash
import dash_bootstrap_components as dbc
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
from fronted.main import layout as main_layout
from fronted.derecho import derecho
from fronted.izquierdo import izquierdo


# Inicializar la aplicación Dash
app1 = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Diseño de la aplicación principal
app1.layout = html.Div([
    main_layout,  # Incorporar el layout de main.py aquí
])

if __name__ == '__main__':
    app1.run_server(debug=True)
# Inicializar la aplicación Dash
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Inicializar la aplicación Dash
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Diseño de la aplicación principal
app.layout = html.Div([
    derecho  # Incorpora la pestaña 'derecho' en la aplicación principal
])

if __name__ == '__main__':
    app.run_server(debug=True)


app2 = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
if __name__ == '__main__':
    app.run_server(debug=True)

# Inicializar la aplicación Dash
app3 = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Diseño de la aplicación principal
app3.layout = html.Div([
    html.Div(id='izquierdo-container', children=[izquierdo]),  # Incorporar el diseño de izquierdo.py aquí
    html.Div(id='derecho-container', children=[derecho]),  # Incorporar el diseño de derecho.py aquí
])

if __name__ == '__main__':
    app.run_server(debug=True)

