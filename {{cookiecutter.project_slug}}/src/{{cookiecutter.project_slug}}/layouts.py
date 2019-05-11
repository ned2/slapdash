"""Contains layouts suitable for being the value of the 'layout' attribute of
Dash app instances.
"""

from flask import current_app as server
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from .components import make_header, make_sidebar


def main_layout_header():
    """Dash layout with a top-header"""
    return html.Div(
        [
            make_header(),
            dbc.Container(
                dbc.Row(dbc.Col(id=server.config["CONTENT_CONTAINER_ID"])), fluid=True
            ),
            dcc.Location(id=server.config["LOCATION_COMPONENT_ID"], refresh=False),
        ]
    )


def main_layout_sidebar():
    """Dash layout with a sidebar"""
    return html.Div(
        [
            dbc.Container(
                fluid=True,
                children=dbc.Row(
                    [
                        dbc.Col(
                            make_sidebar(className="px-2"), width=2, className="px-0"
                        ),
                        dbc.Col(id=server.config["CONTENT_CONTAINER_ID"], width=10),
                    ]
                ),
            ),
            dcc.Location(id=server.config["LOCATION_COMPONENT_ID"], refresh=False),
        ]
    )
