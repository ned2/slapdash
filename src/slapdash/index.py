from flask import current_app as server
from dash.dependencies import Output, Input
from dash.exceptions import PreventUpdate

from .app import app
from .pages import page_not_found, page1, page2, page3
from .components import Navbar
from .utils import get_url


#
# The router
#

# Ordered iterable of routes: tuples of (route, layout), where 'route' is a
# string corresponding to path of the route (will be prefixed with Dash's
# 'routes_pathname_prefix' and 'layout' is a Dash Component.
urls = (
    ('',      page1.layout),
    ('page1', page1.layout),
    ('page2', page2.layout),
    ('page3', page3.layout),
)


routes = {get_url(route): layout for route, layout in urls}


@app.callback(Output(server.config['CONTENT_CONTAINER_ID'], 'children'),
              [Input('url', 'pathname')])
def router(pathname):
    """The router"""
    default_layout = page_not_found(pathname)
    return routes.get(pathname, default_layout)


#
# The Navbar
#


if server.config['NAVBAR']:
    @app.callback(Output(server.config['NAVBAR_CONTAINER_ID'], 'children'),
                  [Input('url', 'pathname')])
    def update_nav(pathname):
        """Create the navbar with the current page set to active"""
        if pathname is None:
            # pathname is None on the first load of the app; ignore this
            raise PreventUpdate("Ignoring first url.pathname callback")
        return Navbar(items=server.config['NAV_ITEMS'], current_path=pathname)
