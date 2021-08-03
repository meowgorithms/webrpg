import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from engine.archetypes import Quantum

def test_creation():
    character = Quantum("Fred")
    return str(character)


# Components and columns
# ----------------------

column1 = dbc.Col(
    [
        html.Div(id="div1", children=test_creation())
    ])


# Layout
layout = dbc.Row([column1])