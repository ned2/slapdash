import dash_core_components as dcc
import dash_html_components as html

from .server import server, app
from .utils import component, get_url


@component
def Row(children=None, **kwargs):
    """A convenience component that makes a Bootstrap row"""
    return html.Div(children=children, className='row', **kwargs)


@component  
def Col(children=None, bp=None, size=None, **kwargs):
    """A convenience component that makes a Bootstrap column"""
    if size is None and bp is None:
        col_class = 'col'
    elif bp is None:
        col_class = f'col-{size}'
    else:        
        col_class = f'col-{bp}-{size}'
    return html.Div(children=children, className=col_class, **kwargs)


@component
def Header(children=None, **kwargs):
    return html.Header(html.H1(
        children=[
            Fa('bar-chart'), 
            dcc.Link(
                server.config['TITLE'],
                href=app.config.routes_pathname_prefix
            )
        ],
        **kwargs
    ))


def Fa(name):
    """A convenience component for adding Font Awesome icons"""
    return html.I(className=f"fa fa-{name}")


@component
def Navbar(
        children=None,
        items=None,
        current_path=None,
        first_root_nav=True,
        **kwargs):

    items = items if items is not None else []
    nav_items = []
    route_prefix = app.config.routes_pathname_prefix
    
    for i, (path, text) in enumerate(items):
        href = get_url(path)
        # bool indicating if: on the root url and this is the first nav item       
        is_first_root_nav = (current_path == route_prefix) and (i == 0)
        # active if we are on the path of this nav item, or if first_root_nav is
        # enabled and applies for this path
        is_active = (current_path == href) or (first_root_nav and is_first_root_nav) 
        className = 'nav-item active' if is_active else 'nav-item'
        nav_items.append(html.Li(
            className=className,
            children=dcc.Link(text, href=href, className='nav-link')
        ))

    return html.Nav(
        className=f'navbar',
        children=[
            html.Ul(
                className=f'nav',
                children=nav_items
            ),
        ],
        **kwargs,
    )
