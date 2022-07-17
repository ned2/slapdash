import dash
from dash import dcc, html, callback
import dash_bootstrap_components as dbc
from dash.dependencies import Input, State, Output

dash.register_page(__name__)


layout = html.Div("Page 2")
