import inspect
from functools import wraps

import dash
from dash.dependencies import Output, Input
from dash.exceptions import PreventUpdate
from flask import current_app as server

from .pages import page_not_found


class Router:
    """A URL Router for Dash multipage apps"""

    def __init__(self, app, urls):
        """Initialise the router.

        Params:
        app:   A Dash instance to associate the router with.
        urls:  Ordered iterable of routes: tuples of (route, layout). 'route' is a
               string corresponding to the URL path of the route (will be prefixed with Dash's
               'routes_pathname_prefix' and 'layout' is a Dash Component.
        """
        self.routes = {get_url(route): layout for route, layout in urls}

        @app.callback(
            Output(app.server.config["CONTENT_CONTAINER_ID"], "children"),
            [Input("url", "pathname")],
        )
        def router(pathname):
            """The router"""
            default_layout = page_not_found(pathname)
            return self.routes.get(pathname, default_layout)


def get_dash_args_from_flask_config(config):
    """Get a dict of Dash params that were specified """
    # all arg names less 'self'
    dash_args = set(inspect.getfullargspec(dash.Dash.__init__).args[1:])
    return {key.lower(): val for key, val in config.items() if key.lower() in dash_args}


def get_url(path):
    """Expands an internal URL to include prefix the app is mounted at"""
    return f"{server.config['ROUTES_PATHNAME_PREFIX']}{path}"


def component(func):
    """Decorator to help vanilla functions as pseudo Dash Components"""

    @wraps(func)
    def function_wrapper(*args, **kwargs):
        # remove className and style args from input kwargs so the component
        # function does not have to worry about clobbering them.
        className = kwargs.pop("className", None)
        style = kwargs.pop("className", None)

        # call the component function and get the result
        result = func(*args, **kwargs)

        # now restore the initial classes and styles by adding them
        # to any values the component introduced

        if className is not None:
            if hasattr(result, "className"):
                result.className = f"{className} {result.className}"
            else:
                result.className = className

        if style is not None:
            if hasattr(result, "style"):
                result.style = style.update(result.style)
            else:
                result.style = style

        return result

    return function_wrapper
