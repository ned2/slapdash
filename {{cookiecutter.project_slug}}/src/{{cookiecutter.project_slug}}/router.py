from dash.dependencies import Output, Input
from dash.exceptions import PreventUpdate
from dash.development.base_component import Component
from werkzeug.datastructures import MultiDict

from .exceptions import InvalidLayoutError


class DashRouter:
    """A URL Router for Dash multipage apps"""

    def __init__(
        self,
        app,
        urls=None,
        content_component_id="content",
        location_component_id="location",
    ):
        """Initialise the router.
        Params:
        app:   A Dash instance to associate the router with.
        urls:  Ordered iterable of routes: tuples of (route, layout). 'route' is a
               string corresponding to the URL path of the route (will be prefixed
               with Dash's 'routes_pathname_prefix' and 'layout' is a Dash Component
               or callable that returns a Dash Component. The callable will also have
               any URL query parameters passed in as keyword arguments.
        """
        self.app = app
        self.content_component_id = content_component_id
        self.location_component_id = location_component_id
        self.routes = {}
        if urls is not None:
            self.add_urls(urls)

    def add_urls(self, urls):
        self.routes.update({self.get_url(route): layout for route, layout in urls})

    def register(self):
        @self.app.callback(
            Output(self.content_component_id, "children"),
            [
                Input(self.location_component_id, "pathname"),
                Input(self.location_component_id, "search"),
            ],
        )
        def router_callback(pathname, search):
            """The router"""
            if pathname is None:
                raise PreventUpdate("Ignoring first Location.pathname callback")

            page = self.routes.get(pathname, None)
            if page is None:
                layout = f"Page not found: {pathname}"
            elif isinstance(page, Component):
                layout = page
            elif callable(page):
                kwargs = MultiDict(parse_qs(search.lstrip("?")))
                layout = page(**kwargs)
                if not isinstance(layout, Component):
                    msg = (
                        "Layout function must return a Dash Component.\n\n"
                        f"Function {page.__name__} from module {page.__module__} "
                        f"returned value of type {type(layout)} instead."
                    )
                    raise InvalidLayoutError(msg)
            else:
                msg = (
                    "Page layouts must be a Dash Component or a callable that "
                    f"returns a Dash Component. Received value of type {type(page)}."
                )
                raise InvalidLayoutError(msg)
            return layout

    def get_url(self, path):
        """Expands an internal URL to include prefix the app is mounted at"""
        return f"{self.app.config.routes_pathname_prefix}{path}"
