from .slapdash import app, CONTAINER_ID
from .layouts import layout1, layout2, layout3


ROUTES = {
    '/page1': layout1,
    '/page2': layout2,
    '/page3': layout3,
}


# The router
@app.callback(Output(CONTAINER_ID, 'children'), [Input('url', 'pathname')])
def router(pathname):
    default_layout = html.P("No page '{}'".format(pathname))
    return ROUTES.get(pathname, default_layout)
