from dash import Dash
from flask import Flask
import dash_bootstrap_components as dbc
from .layouts import main_layout_header, main_layout_sidebar
from . import settings


server = Flask(__package__)

app = Dash(
    __package__,
    use_pages=True,
    title=settings.TITLE,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
)

app.layout = main_layout_sidebar
