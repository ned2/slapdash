import dash
from dash import dcc, html
import dash_bootstrap_components as dbc

from .utils import component
from . import settings


def fa(className):
    """A convenience component for adding Font Awesome icons"""
    return html.I(className=className)


@component
def make_brand(**kwargs):
    return html.Header(
        className="brand",
        children=dcc.Link(
            href="/",
            children=html.H1([fa("fa-solid fa-chart-column"), settings.TITLE]),
        ),
        **kwargs,
    )


# TODO: Navbar vs Nav?

@component
def make_header(**kwargs):
    return html.Div(
        dbc.Navbar(
            id="header",
            className="sticky-top",
            color="dark",
            dark=True,
            children=[
                make_brand(),
                html.Ul(id="navbar", className="navbar-nav ml-auto"),
            ],
        )
        ** kwargs,
    )


@component
def make_sidebar(**kwargs):
    return html.Div(
        dbc.Nav(
            [
                dbc.NavLink(
                    [
                        html.Div(page["name"], className="ms-2"),
                    ],
                    href=page["path"],
                    active="exact",
                )
                for page in dash.page_registry.values()
            ],
            vertical=True,
            pills=True,
            className="nav bg-dark navbar-dark",
        ),
        **kwargs,
    )
