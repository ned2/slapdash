import os
import sys

from flask import Flask, send_from_directory

from .utils import CustomIndexDash
from .settings import STATIC_FOLDER, STATIC_URL_PATH, URL_BASE_PATHNAME
from .exceptions import HaltCallback


server = Flask(
    __name__,
    static_folder=STATIC_FOLDER,
    static_url_path=STATIC_URL_PATH
)

app = CustomIndexDash(
    __name__,
    server=server,
    url_base_pathname=URL_BASE_PATHNAME
)

# We need to suppress validations as we will be initialising callbacks
# that target element IDs that won't yet occur in the layout. 
app.config.supress_callback_exceptions = True


@server.route('/favicon.ico')
def favicon():
    """Serve the favicon"""
    return send_from_directory(
        os.path.join(server.root_path, STATIC_FOLDER),
        'favicon.ico',
        mimetype='image/x-icon'
    )


@server.errorhandler(HaltCallback)
def handle_error(error):
    """Handle a halted callback and return an empty 204 response"""
    print(error, file=sys.stderr)
    return ('', 204)
