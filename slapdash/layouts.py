import dash_core_components as dcc
import dash_html_components as html

from .exceptions import ValidationError
from .components import Col, Row
from .settings import (TITLE, CONTENT_CONTAINER_ID, URL_BASE_PATHNAME,
                       NAVBAR_CONTAINER_ID, NAV_ITEMS, NAVBAR)


def nav_items(items, active_path=None):
    li_className = 'nav-item'
    nav_items = []
    
    for path, text in items:
        href = f"{URL_BASE_PATHNAME}{path}"
        is_active = href == active_path
        className = '{li_className} active' if is_active else li_className
        li = html.Li(
            className=className,
            children=dcc.Link(text, href=href, className='nav-link')
        )
        nav_items.append(li)
    return nav_items


def navbar(orientation='top', active_path=None):
    return html.Nav(
        id='top-navbar',
        className=f'navbar {orientation}',
        children=[
            dcc.Link(TITLE, className='name'),
            html.Ul(
                className='navigation',
                children=nav_items(NAV_ITEMS, active_path=active_path)
            ),
        ]
    )


def main_layout_top_nav():
    """Top level Dash layout with a top navbar"""
    return html.Div([
        html.Div(id=NAVBAR_CONTAINER_ID),
        html.Div(
            className='container-fluid',
            children=Row(
                Col(id=CONTENT_CONTAINER_ID)
            )
        ),
        dcc.Location(id='url', refresh=False)
    ])


def main_layout_side_nav():
    """Top level Dash layout with a side navbar"""
    return html.Div([
        html.Div(
            className='container-fluid',
            children=Row([
                Col(id=NAVBAR_CONTAINER_ID, size=2),
                Col(
                    id=CONTENT_CONTAINER_ID,
                    size=10,
                    className='offset-2'
                ),
            ])
        ),
        dcc.Location(id='url', refresh=False)
    ])


def main_layout_no_nav():
    """Top level Dash layout with no navbar"""
    return html.Div([
        html.Div(
            className='container-fluid',
            id=CONTENT_CONTAINER_ID,            
        ),
        dcc.Location(id='url', refresh=False),
    ])


def main_layout():
    """Gets the main layout according to the NAVBAR setting."""    
    if NAVBAR not in ('side', 'top', None):
        msg = f"Invalid value {NAVBAR} for NAVBAR; should be 'side', 'top', or None"
        raise ValidationError(msg)
    
    if NAVBAR == 'side':
        return main_layout_side_nav()
    elif NAVBAR == 'top':
        return main_layout_top_nav()
    else:
        return main_layout_no_nav()
