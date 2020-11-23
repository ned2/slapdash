from dash.dependencies import Output, Input
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc
import dash_html_components as html

from .utils import component


class DashNavBar:
    """A Dash navbar for multipage apps"""

    def __init__(self, app, router, nav_items=None, navbar_component_id="navbar-items"):
        """Initialise the navbar.

        Params:
        app:        A Dash instance to associate the router with.

        nav_items:  Ordered iterable of navbar items: tuples of `(route, display)`,
                    where `route` is a string corresponding to path of the route
                    (will be prefixed with Dash's 'routes_pathname_prefix') and
                    'display' is a valid value for the `children` keyword argument
                    for a Dash component (ie a Dash Component or a string).
        """
        self.app = app
        self.router = router
        self.navbar_component_id = navbar_component_id 
        self.nav_items = []
        if nav_items is not None:
            self.add_nav_items(nav_items)

    def add_nav_items(self, nav_items):
        self.nav_items.extend(nav_items)

    def register(self):
        @self.app.callback(
            Output(self.navbar_component_id, "children"),
            [Input(self.router.location_component_id, "pathname")],
        )
        def update_nav_callback(pathname):
            """Create the navbar with the current page set to active"""
            if pathname is None:
                # pathname is None on the first load of the app; ignore this
                raise PreventUpdate("Ignoring first Location.pathname callback")
            return self.make_nav(pathname)

    @component
    def make_nav(self, current_path, **kwargs):
        nav_items = []
        for i, (path, text) in enumerate(self.nav_items):
            href = get_url(path)
            active = (current_path == href) or (
                i == 0 and current_path == self.app.config.routes_pathname_prefix
            )
            nav_item = dbc.NavItem(dbc.NavLink(text, href=href, active=active))
            nav_items.append(nav_item)
        return html.Ul(nav_items, className="navbar-nav", **kwargs)
