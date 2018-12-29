import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from flask import current_app as server

from .utils import get_url, component


def fa(className):
    """A convenience component for adding Font Awesome icons"""
    return html.I(className=className)


@component
def make_brand(**kwargs):
    return html.Header(
        className="brand",
        children=dcc.Link(
            href=get_url(''),
            children=html.H1(
                [
                    fa('far fa-chart-bar'),
                    server.config['TITLE'],
                ]
            )
        ),
        **kwargs
    )


@component
def make_header(**kwargs):
    return html.Nav(
        id="header",
        className="navbar navbar-dark navbar-expand bg-dark sticky-top",
        children=[
            make_brand(),
            html.Ul(
                id=server.config['NAVBAR_CONTAINER_ID'],
                className="navbar-nav ml-auto"
            )
        ],
        **kwargs
    )


@component
def make_sidebar(**kwargs):
    return html.Nav(
        id=f"sidebar",
        className="nav navbar-dark bg-dark flex-column align-items-start",
        children=[
            make_brand(),
            html.Div(id=server.config['NAVBAR_CONTAINER_ID']),
        ],
        **kwargs
    )


@component
def make_nav(items, current_path, **kwargs):
    nav_items = []
    route_prefix = server.config['URL_BASE_PATHNAME']
    for i, (path, text) in enumerate(items):
        href = get_url(path)
        active = (current_path == href) or (i == 0 and current_path ==
                                            route_prefix) 
        nav_item = dbc.NavItem(dbc.NavLink(text, href=href, active=active))
        nav_items.append(nav_item)
    return html.Ul(
        nav_items,
        className="navbar-nav",
        **kwargs
    )

