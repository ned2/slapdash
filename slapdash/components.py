import dash_core_components as dcc
import dash_html_components as html


def add_class(className, args_dict):
    if 'className' in args_dict:
        args_dict['className'] = f'{className} {args_dict["className"]}'
    else:
        args_dict['className'] = className

        
def add_base_styles(styles, args_dict):
    if 'style' in args_dict:
        styles.update(args_dict['style'])
    args_dict['style'] = styles 




    
def Row(children=None, **kwargs):
    add_class('row', kwargs)
    return html.Div(children=children, **kwargs)

    
def Col(children=None, bp=None, size=None, **kwargs):
    if size is None and bp is None:
        col_class = 'col'
    elif bp is None:
        col_class = f'col-{size}'
    else:        
        col_class = f'col-{bp}-{size}'
    add_class(col_class, kwargs)
    return html.Div(children=children, **kwargs)


def FontA(name):
    return html.I(className=f"fa {name}")
