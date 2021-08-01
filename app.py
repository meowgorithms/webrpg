import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from flask_sqlalchemy import SQLAlchemy
from dash.dependencies import Input, Output
from pages import play, index, character_creator

external_stylesheets = [
    dbc.themes.CYBORG, # Bootswatch theme
    'https://use.fontawesome.com/releases/v5.9.0/css/all.css', # for social media icons
]

meta_tags=[
    {'name': 'viewport', 'content': 'width=device-width, initial-scale=1'}
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets, meta_tags=meta_tags)

# Components
# ----------

# Nav / header
navbar = dbc.NavbarSimple(
    brand='SoftYeetus',
    brand_href='/', 
    children=[
        dbc.NavItem(dcc.Link('Home', href='/index', className='nav-link')),
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
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar,
    dbc.Container(id='page-content', className='mt-4'),
    html.Hr()
])

# Callbacks
# ---------

# Pages
@app.callback(Output('page-content', 'children'),
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

# Initialize server and database
server = app.server
server.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///webrpg.sqlite3"
server.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(server)
db.init_app(server)
db.create_all()

if __name__ == '__main__':
    app.run_server(debug=True)
