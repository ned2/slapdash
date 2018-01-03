from dash.dependencies import Output, Input

from .server import app
from .pages import page_not_found, page1, page2, page3
from .settings import (CONTENT_CONTAINER_ID, NAVBAR_CONTAINER_ID,
                       URL_BASE_PATHNAME, NAVBAR, NAV_ITEMS, TITLE)
from .components import Navbar
from .utils import get_url

# Ordered iterable of routes: tuples of (route, layout), where 'route' is a
# string corresponding to path of the route (will be prefixed with
# URL_BASE_PATHNAME) and 'layout' is a Dash Component.
urls = (
    ('', page1),
    ('page1', page1),
    ('page2', page2),
    ('page3', page3),
)


routes = {get_url(route): layout for route, layout in urls}


# The router callback
@app.callback(Output(CONTENT_CONTAINER_ID, 'children'),
              [Input('url', 'pathname')])
def router(pathname):
    default_layout = page_not_found(pathname)
    return routes.get(pathname, default_layout)


if NAVBAR:
    # Callback that regenerates navbar with current page as active when the URL
    # of the app changes. Memoize 
    @app.callback(
        Output(NAVBAR_CONTAINER_ID, 'children'),
        [Input('url', 'pathname')])
    def update_nav(pathname):
        # note: pathname is None on the first load of the app for some reason
        # https://github.com/plotly/dash-core-components/issues/138
        return Navbar(
            NAV_ITEMS,
            title=TITLE,
            orientation=NAVBAR,
            current_path=pathname
        )
