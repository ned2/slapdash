import dash_core_components as dcc
import dash_html_components as html

from .components import Col, Row


page1 = html.Div("Page 1")
page2 = html.Div("Page 2")
page3 = html.Div("Page 3")


def page_not_found(pathname):
    return html.P("No page '{}'".format(pathname))


