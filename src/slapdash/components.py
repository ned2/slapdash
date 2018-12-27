from flask import current_app as server
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from .utils import get_url


def make_brand(**kwargs):
    return html.Header(
        html.H1(
            children=[
                fa('bar-chart'),
                dcc.Link(
                    server.config['TITLE'],
                    href=server.config['ROUTES_PATHNAME_PREFIX']
                )
            ],
        ),
        **kwargs
    )


def fa(name):
    """A convenience component for adding Font Awesome icons"""
    return html.I(className=f"fa fa-{name}")


def make_navbar(items, current_path):
    nav_items = []
    route_prefix = server.config['ROUTES_PATHNAME_PREFIX']
    for i, (path, text) in enumerate(items):
        href = get_url(path)
        active = (current_path == href) or (i == 0 and current_path ==
                                            route_prefix) 
        nav_item = dbc.NavItem(dbc.NavLink(text, href=href, active=active))
        nav_items.append(nav_item)
    return dbc.Navbar(children=nav_items, className='bg-dark')
