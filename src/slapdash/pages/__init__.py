import dash_html_components as html


def page_not_found(pathname):
    return html.P("No page '{}'".format(pathname))


