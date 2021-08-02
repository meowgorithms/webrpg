from dash.dependencies import Output, Input
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from app import db, APP



# Components
# ----------

column1 = dbc.Col(
    dbc.Card()
)

# Layout
layout = dbc.Row([column1])
