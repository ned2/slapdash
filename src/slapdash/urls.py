from flask import current_app as server

from .pages import page_not_found, character_counter, page2, page3


# Ordered iterable of routes: tuples of (route, layout), where 'route' is a
# string corresponding to path of the route (will be prefixed with Dash's
# 'routes_pathname_prefix' and 'layout' is a Dash Component.
URLS = (
    ('', character_counter.layout),
    ('character-counter', character_counter.layout),
    ('page2', page2.layout),
    ('page3', page3.layout),
)
