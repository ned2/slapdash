import dash_html_components as html
from flask import current_app as server
from dash.dependencies import Output, Input
from dash.exceptions import PreventUpdate

from .app import app
from .pages import page_not_found, character_counter, page2, page3
from .components import make_nav, fa
from .utils import get_url


#
# The router
#

# Ordered iterable of routes: tuples of (route, layout), where 'route' is a
# string corresponding to path of the route (will be prefixed with Dash's
# 'routes_pathname_prefix' and 'layout' is a Dash Component.
URLS = (
    ('',      character_counter.layout),
    ('character-counter', character_counter.layout),
    ('page2', page2.layout),
    ('page3', page3.layout),
)


ROUTES = {get_url(route): layout for route, layout in URLS}


@app.callback(Output(server.config['CONTENT_CONTAINER_ID'], 'children'),
              [Input('url', 'pathname')])
def router(pathname):
    """The router"""
    default_layout = page_not_found(pathname)
    return ROUTES.get(pathname, default_layout)


#
# The Navbar
#

# Ordered iterable of navbar items: tuples of `(route, display)`, where `route`
# is a string corresponding to path of the route (will be prefixed with
# URL_BASE_PATHNAME) and 'display' is a valid value for the `children` keyword
# argument for a Dash component (ie a Dash Component or a string).
NAV_ITEMS = (
    (
        "character-counter",
        html.Div([fa("fas fa-keyboard"), "Character Counter"])
    ),
    (
        "page2",
        html.Div([fa("fas fa-chart-area"), "Page 2"])
    ),
    (
        "page3",
        html.Div([fa("fas fa-chart-line"), "Page 3"])
    ),
)


@app.callback(Output(server.config['NAVBAR_CONTAINER_ID'], 'children'),
              [Input('url', 'pathname')])
def update_nav(pathname):
    """Create the navbar with the current page set to active"""
    if pathname is None:
        # pathname is None on the first load of the app; ignore this
        raise PreventUpdate("Ignoring first url.pathname callback")
    return make_nav(NAV_ITEMS, pathname)
