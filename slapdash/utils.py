from functools import wraps

from .server import server


def get_url(path):
    """Expands the an internal URL to include prefix the app is mounted at"""
    base_path = server.config['URL_BASE_PATHNAME'] 
    return f"{base_path}{path}"


def component(func):
    """Decorator to help use vanilla functions as pseudo Dash Components"""
    @wraps(func)
    def function_wrapper(*args, **kwargs):
        # remove className and style args from input kwargs so the component
        # function does not have to worry about clobbering them.
        className = kwargs.pop('className', None)
        style = kwargs.pop('className', None)
        children = kwargs.pop('children', None)
        
        # call the component function and get the result
        result = func(*args, **kwargs)

        # now restore the initial classes and styles by adding them
        # to any values the component introduced

        if className is not None:
            if hasattr(result, 'className'):
                result.className = f'{className} {result.className}'
            else:
                result.className = className

        if style is not None:
            if hasattr(result, 'style'):
                result.style = style.update(result.style)
            else:
                result.style = style

        # pass through the children attribute, only if the new component did not
        # set it.
        if children is not None and hasattr(result, 'children'):
            result.children = children
                

        return result
    return function_wrapper
