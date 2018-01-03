from functools import wraps

from dash import Dash

from .settings import STATIC_URL_PATH, STYLESHEETS, URL_BASE_PATHNAME


def get_url(path):
    """Expands the an internal URL to include prefix the app is mounted at """
    return f"{URL_BASE_PATHNAME}{path}"


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


class CustomIndexDash(Dash):
    """Custom Dash class overriding index() method for local CSS support"""
    def _generate_css_custom_html(self):
        link_str = '<link rel="stylesheet" href="{}/{}">'
        return '\n'.join(link_str.format(STATIC_URL_PATH, path)
                         for path in STYLESHEETS)

    def index(self, *args, **kwargs):
        scripts = self._generate_scripts_html()
        css = self._generate_css_dist_html()
        custom_css = self._generate_css_custom_html()
        config = self._generate_config_html()
        title = getattr(self, 'title', 'Dash')
        return f'''
        <!DOCTYPE html>
        <html>
            <head>
                <meta charset="UTF-8">
                <title>{title}</title>
                {css}
                {custom_css}
            </head>
            <body>
                <div id="react-entry-point">
                    <div class="_dash-loading">
                        Loading...
                    </div>
                </div>
                <footer>
                    {config}
                    {scripts}
                </footer>
            </body>
        </html>
        '''
