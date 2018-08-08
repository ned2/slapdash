import os
import sys

from flask import Flask, send_from_directory

from .custom_dash import CustomIndexDash
from .exceptions import HaltCallback


server = Flask(__name__)

# load default settings
server.config.from_object(f'{__package__}.settings')


# load additional settings that will override the defaults in settings.py. eg
# $ export SLAPDASH_SETTINGS=/some/path/prod_settings.py
server.config.from_envvar('SLAPDASH_SETTINGS', silent=True)


app = CustomIndexDash(
    server=server,
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


@server.errorhandler(HaltCallback)
def handle_error(error):
    """Handle a halted callback and return an empty 204 response"""
    print(error, file=sys.stderr)
    return ('', 204)
