from pages import character_creator
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from engine import name_provider

def test_creation():
    name = name_provider.create_spell_name()
    return str()


# Components and columns
# ----------------------

column1 = dbc.Col(
    [
        html.Div(id="div1", children=test_creation())
    ])


# Layout
layout = dbc.Row([column1])