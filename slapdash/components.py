import dash_core_components as dcc
import dash_html_components as html

from .utils import component, get_url
from .settings import URL_BASE_PATHNAME, TITLE


@component
def Row(*args, **kwargs):
    """A convenience component that makes a Bootstrap row"""
    return html.Div(*args, className='row', **kwargs)


@component  
def Col(*args, bp=None, size=None, **kwargs):
    """A convenience component that makes a Bootstrap column"""
    if size is None and bp is None:
        col_class = 'col'
    elif bp is None:
        col_class = f'col-{size}'
    else:        
        col_class = f'col-{bp}-{size}'

    return html.Div(*args, className=col_class, **kwargs)


@component
def Header(**kwargs):
    return html.Header(html.H1(
        children=[
            Fa('bar-chart'),
            Link(TITLE, href=URL_BASE_PATHNAME)
        ],
        **kwargs
    ))
    
    
@component
def Navbar(items, orientation='top', current_path=None,
           first_root_nav=True, **kwargs):
    nav_items = []
    
    for i, (path, text) in enumerate(items):
        href = get_url(path)
        # we are on the root url and  this is the first nav item
        is_first_root_nav = current_path == URL_BASE_PATHNAME and i == 0
        # active if we are on the path of this nav item, or if first_root_nav is
        # enabled and applies for this path
        is_active = current_path == href or (first_root_nav and is_first_root_nav) 
        className = 'nav-item active' if is_active else 'nav-item'
        nav_items.append(html.Li(
            className=className,
            children=Link(text, href=href, className='nav-link')
        ))

    return html.Nav(
        className=f'navbar {orientation}-nav',
        children=[
            html.Ul(
                className=f'nav',
                children=nav_items
            ),
        ],
        **kwargs,
    )


@component
def Link(children=None, href='', **kwargs):
    # TODO: CSS pointer-events have been set to none for the nested anchor tag
    # so that clicking the link doesn't cause a page redirect to the target
    # link. This however means we lose some useful link hover behaviour.
    # https://github.com/plotly/dash-core-components/issues/129
    return dcc.Link(
        href=href,
        className='link',
        children=html.A(children, href=href),
        **kwargs
    )


@component
def Fa(name, **kwargs):
    """A convenience component for adding Font Awesome icons"""
    return html.I(className=f"fa fa-{name}")
