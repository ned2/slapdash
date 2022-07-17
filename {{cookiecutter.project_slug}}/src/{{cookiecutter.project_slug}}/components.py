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


@component
def make_navbar(vertical=False, **kwargs):
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
            vertical=vertical,
            pills=True,
            className="nav bg-dark navbar-dark",
        ),
        **kwargs,
    )
