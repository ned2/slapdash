from flask import Flask
from dash import Dash


def create_app(config_object=f'{__package__}.settings'):
    server = Flask(__package__)
    
    # load default settings
    server.config.from_object(config_object)

    # load additional settings that will override the defaults in settings.py. eg
    # $ export SLAPDASH_SETTINGS=/some/path/prod_settings.py
    server.config.from_envvar('SLAPDASH_SETTINGS', silent=True)

    return server


def create_dash(server):
    app = Dash(server=server)

    app.title = server.config['TITLE']
    app.config.routes_pathname_prefix = server.config['ROUTES_PATHNAME_PREFIX']

    # Suppress callback validation as we will be initialising callbacks that target
    # element IDs that won't yet occur in the layout.
    app.config.supress_callback_exceptions = True

    return app
