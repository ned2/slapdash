"""Contains layouts suitable for being the value of the 'layout' attribute of
Dash app instances.
"""

import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from .app import router
from .components import make_header, make_sidebar


def main_layout_header():
    """Dash layout with a top-header"""
    return html.Div(
        [
            make_header(),
            dbc.Container(dbc.Row(dbc.Col(id=router.content_component_id)), fluid=True),
            dcc.Location(id=router.location_component_id, refresh=False),
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
                        dbc.Col(id=router.content_component_id, width=10),
                    ]
                ),
            ),
            dcc.Location(id=router.location_component_id, refresh=False),
        ]
    )
