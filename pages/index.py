from pages import character_creator
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from engine.archetypes import Quantum

def test_creation():
    character = Quantum("Fred")
    character2 = Quantum("Fred")
    character2.magic_defense = 10

    print(f"Fred1 has {character.current_health} health, and {character.magic_defense} magic defense")
    print(f"Fred2 has {character2.current_health} health, and {character2.magic_defense} magic defense")
    character.abilities["Tunnel"].use_ability(character2)
    print(f"Fred1 has {character.current_health} health, and {character.magic_defense} magic defense")
    print(f"Fred2 has {character2.current_health} health, and {character2.magic_defense} magic defense")
    return str(character)


# Components and columns
# ----------------------

column1 = dbc.Col(
    [
        html.Div(id="div1", children=test_creation())
    ])


# Layout
layout = dbc.Row([column1])