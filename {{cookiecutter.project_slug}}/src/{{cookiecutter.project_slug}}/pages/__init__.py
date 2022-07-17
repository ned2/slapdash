from dash import html as _html


def page_not_found(pathname):
    return _html.P("No page '{}'".format(pathname))
