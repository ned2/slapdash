import dash_core_components as dcc
import dash_html_components as html

from .exceptions import ValidationError
from .components import Col, Row, Header
from .server import server


"""Contains layouts suitable for being the value of the 'layout' attribute of
Dash app instances."""


def main_layout_header():
    """Dash layout with a top-header"""
    return html.Div([
        html.Div(
            id="header",
            children=[
                Header(),
                html.Div(id=server.config['NAVBAR_CONTAINER_ID']),
            ]
        ),
        html.Div(
            className='container-fluid',
            children=Row(
                Col(id=server.config['CONTENT_CONTAINER_ID'])
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
            children=Row([
                Col(
                    size=2,
                    children=[
                        Row(Col(Header())),
                        Row(Col(id=server.config['NAVBAR_CONTAINER_ID']))
                    ]),
                Col(
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
            children=Row(
                Col(id=server.config['CONTENT_CONTAINER_ID'])
            )
        ),
        dcc.Location(id='url', refresh=False),
    ])
