from dash.dependencies import Output, Input

from .server import app
from .layouts import page_not_found, page1, page2, page3
from . import settings


routes = {
    '/': page1,
    '/page1': page1,
    '/page2': page2,
    '/page3': page3,
}


# The router callback
@app.callback(Output(settings.CONTAINER_ID, 'children'),
              [Input('url', 'pathname')])
def router(pathname):
    default_layout = page_not_found(pathname)
    return routes.get(pathname, default_layout)
