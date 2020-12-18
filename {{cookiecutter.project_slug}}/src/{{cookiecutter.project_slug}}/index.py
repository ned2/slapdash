import dash_html_components as html
from collections import namedtuple

from .app import app
from .utils import DashRouter, DashNavBar
from .pages import character_counter, page2, page3
from .components import fa


# Ordered iterable of routes: tuples of (route, layout), where 'route' is a
# string corresponding to path of the route (will be prefixed with Dash's
# 'routes_pathname_prefix' and 'layout' is a Dash Component.
urls = (
    ("", character_counter.get_layout),
    ("character-counter", character_counter.get_layout),
    ("page2", page2.layout),
    ("page3", page3.layout),
    ("section2/page1", page2.layout),
    ("section2/page2", page3.layout),
)

# Ordered iterable of navbar items: tuples of `(route, display)`, where `route`
# is a string or a list of tuples corresponding to path of the route (will be prefixed with
# 'routes_pathname_prefix') and 'display' is a valid value for the `children`
# keyword argument for a Dash component (ie a Dash Component or a string).
nav_item = namedtuple("nav_item", "route display")
nav_items = (
    nav_item(route="character-counter", display=html.Div([fa("fas fa-keyboard"), "Character Counter"])),
    nav_item(route="page2", display=html.Div([fa("fas fa-chart-area"), "Page 2"])),
    nav_item(route="page3", display=html.Div([fa("fas fa-chart-line"), "Page 3"])),
    (
        [
            nav_item(route="section2/page1", display="S2 P1"),
            nav_item(route="section2/page2", display="S2 P2"),
        ],
        "Section 2",
    ),
    
)

router = DashRouter(app, urls)
navbar = DashNavBar(app, nav_items)
