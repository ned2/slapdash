from flask import current_app as server
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from .exceptions import ValidationError
from .components import make_brand


"""Contains layouts suitable for being the value of the 'layout' attribute of
Dash app instances."""


def main_layout_header():
    """Dash layout with a top-header"""
    return html.Div([
        html.Div(
            id="header",
            children=[
                make_brand(),
                html.Div(id=server.config['NAVBAR_CONTAINER_ID']),
            ],
            className='bg-dark',

        ),
        dbc.Container(
            fluid=True,
            children=dbc.Row(
                dbc.Col(id=server.config['CONTENT_CONTAINER_ID'])
            )
        ),
        dcc.Location(id='url', refresh=False)
    ])


# NOTE: not quite working yet
def main_layout_sidebar():
    """Dash layout with a sidebar"""
    return html.Div([
        html.Div(
            className='container-fluid',
            children=dbc.Row([
                dbc.Col(
                    size=2,
                    children=[
                        dbc.Row(Col(make_brand())),
                        dbc.Row(Col(id=server.config['NAVBAR_CONTAINER_ID']))
                    ]),
                dbc.Col(
                    id=server.config['CONTENT_CONTAINER_ID'],
                    size=10,
                    className='offset-2'
                ),
            ])
        ),
        dcc.Location(id='url', refresh=False)
    ])


def main_layout_fullpage():
    """Top level Dash layout taking up entire window"""
    return html.Div([
        html.Div(
            className='container-fluid',
            children=dbc.Row(
                dbc.Col(id=server.config['CONTENT_CONTAINER_ID'])
            )
        ),
        dcc.Location(id='url', refresh=False),
    ])
