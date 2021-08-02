import dash
import dash_bootstrap_components as dbc
import os
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

external_stylesheets = [
    dbc.themes.CYBORG, # Bootswatch theme
    'https://use.fontawesome.com/releases/v5.9.0/css/all.css', # for social media icons
]

meta_tags=[
    {'name': 'viewport', 'content': 'width=device-width, initial-scale=1'}
]

APP = dash.Dash(__name__, external_stylesheets=external_stylesheets, meta_tags=meta_tags)

# Load env
load_dotenv()
# Initialize server and database
server = APP.server
server.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
server.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(server)
db.init_app(server)
db.create_all()
