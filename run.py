import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import os
from flask_sqlalchemy import SQLAlchemy
from dash.dependencies import Input, Output
from pages import play, index, character_creator
from dotenv import load_dotenv

from app import APP, db

navbar = dbc.NavbarSimple(
    brand='SoftYeetus',
    brand_href='/', 
    children=[
        dbc.NavItem(dcc.Link('Home', href='/', className='nav-link')),
        dbc.NavItem(dcc.Link('Create a Character', href='/character_creator', className='nav-link')),
        dbc.NavItem(dcc.Link('Play', href='/play', className='nav-link'))
    ],
    sticky='top',
    color='#1DB954',
    light=False,
    dark=True
)

# Foot
footer = dbc.Container(
    dbc.Row(
        dbc.Col(
            html.P()
        )
    )
)

# Layout
APP.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar,
    dbc.Container(id='page-content', className='mt-4'),
    html.Hr()
])

# Callbacks
# ---------

# Pages
@APP.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return index.layout
    elif pathname == '/character_creator':
        return character_creator.layout
    elif pathname == '/play':
        return play.layout
    else:
        return dcc.Markdown('## Page not found')


if __name__ == '__main__':
    APP.run_server(debug=True)
