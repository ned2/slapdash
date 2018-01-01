import dash_core_components as dcc
import dash_html_components as html

from .utils import component, get_url


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
def Navbar(items, title=None, orientation='top', active_path=None, **kwargs):
    nav_items = []
    
    for path, text in items:
        href = get_url(path)
        is_active = href == active_path
        className = 'nav-item active' if is_active else 'nav-item'
        nav_items.append(html.Li(
            className=className,
            children=Link(text, href=href, className='nav-link')
        ))

    return html.Nav(
        className=f'navbar {orientation}-nav',
        children=[
            Link(html.H1(title, className='title')) if title else html.Div(),
            html.Ul(
                className=f'nav',
                children=nav_items
            ),
        ],
        **kwargs,
    )


@component
def Link(text, href='', **kwargs):
    # TODO: CSS pointer-events have been set to none for the nested anchor tag
    # so that clicking the link doesn't cause a page redirect to the target
    # link. This however means we lose some useful link hover behaviour.
    # https://github.com/plotly/dash-core-components/issues/129
    return dcc.Link(
        children=html.A(text, href=href),
        href=href,
        className='link',
        **kwargs
    )



@component
def Fa(name, **kwargs):
    """A convenience component for adding Font Awesome icons"""
    return html.I(className=f"fa {name}")
