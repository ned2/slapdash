import inspect
from functools import wraps

import dash
import dash_html_components as html
from flask import has_request_context
from flask import current_app as server


def get_dash_args_from_flask_config(config):
    """Get a dict of Dash params that were specified """
    # all arg names less 'self'
    dash_args = set(inspect.getfullargspec(dash.Dash.__init__).args[1:])
    return {key.lower(): val for key, val in config.items() if key.lower() in dash_args}


def get_url(path):
    """Expands an internal URL to include prefix the app is mounted at"""
    return f"{server.config['ROUTES_PATHNAME_PREFIX']}{path}"


def validate_layout(func):
    """Decorator that allows callback validation for dynamic layout functions"""

    @wraps(func)
    def function_wrapper(*args, **kwargs):
        requested_layout = func(*args, **kwargs)
        if has_request_context():
            # This is a normal page request, return the layout
            return requested_layout
        # Not handling a request, return a layout with every page
        # layout concatenated together for validation
        layouts = [requested_layout] + [url[1] for url in server.config["URLS"]]
        return html.Div(layouts)

    return function_wrapper


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
