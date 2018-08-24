import os
import sys

from dash import Dash
from flask import Flask, send_from_directory
from flask.helpers import get_root_path

from .exceptions import HaltCallback

server = Flask(__package__)


# load default settings
server.config.from_object(f'{__package__}.settings')


# load additional settings that will override the defaults in settings.py. eg
# $ export SLAPDASH_SETTINGS=/some/path/prod_settings.py
server.config.from_envvar('SLAPDASH_SETTINGS', silent=True)


# need to work around a bug in Dash: https://github.com/plotly/dash/issues/345
# can remove this param from the Dash constructor once fixed
assets_folder = os.path.join(get_root_path(server.name), 'assets')


app = Dash(
    server=server,
    assets_folder=assets_folder,
    url_base_pathname=server.config['URL_BASE_PATHNAME']
)

# We need to suppress validations as we will be initialising callbacks
# that target element IDs that won't yet occur in the layout. 
app.config.supress_callback_exceptions = True


@server.route('/favicon.ico')
def favicon():
    """Serve the favicon"""
    return send_from_directory(
        os.path.join(server.root_path, server.config['STATIC_FOLDER']),
        'favicon.ico',
        mimetype='image/x-icon'
    )
