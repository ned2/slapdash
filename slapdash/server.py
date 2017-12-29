import os

from flask import Flask, send_from_directory

from .utils import CustomIndexDash
from . import settings


server = Flask(
    __name__,
    static_folder=settings.STATIC_FOLDER,
    static_url_path=settings.STATIC_URL_PATH
)

app = CustomIndexDash(
    __name__,
    server=server,
    url_base_pathname=settings.URL_BASE_PATHNAME
)
# import dash_html_components as html
# import dash_core_components as dcc
# app.layout = html.Div([
#     html.Div(id=settings.CONTAINER_ID),
#     dcc.Location(id='url', refresh=False)
# ])


app.config.supress_callback_exceptions = True


# Note that for a scalable app that needs to serve a large number of users, you
# should serve your static assets with a web server such as nginx or Apache,
# rather than with Flask, as we're doing here.

# @server.route(f'{settings.STATIC_URL_PATH}/<path:path>')
# def send_static(path):
#     return send_from_directory(settings.STATIC_FOLDER, path)


@server.route('/favicon.ico')
def favicon():
    """Serve the favicon"""
    return send_from_directory(
        os.path.join(server.root_path, settings.STATIC_FOLDER),
        'favicon.ico',
        mimetype='image/x-icon'
    )
