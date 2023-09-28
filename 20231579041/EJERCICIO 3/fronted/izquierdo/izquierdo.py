import dash_bootstrap_components as dbc
from dash import html, dcc
import plotly.express as px
import pandas as pd

# Cargar el GeoJSON de los departamentos de Colombia
departamentos_geojson = r'C:\Users\KDSL\Desktop\trabajo pro\departamentos_colombia.geojson'

# Crear un mapa de Colombia con Plotly Express
fig = px.choropleth_mapbox(
    geojson=departamentos_geojson,
    locations=["Colombia"],
    featureidkey="properties.NAME_1",  # Campo que identifica los departamentos en el GeoJSON
    mapbox_style="carto-positron",
    center={"lat": 4.0, "lon": -72.0},
    zoom=4
)

fig.update_geos(projection_type="mercator")

# Diseño de la pestaña 'Izquierdo'
izquierdo = dbc.Container([
    html.H1('Mapa de Colombia'),
    html.Hr(),
    dcc.Graph(figure=fig)  # Agregar el mapa a la aplicación
])

