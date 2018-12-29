from flask import Flask
from dash import Dash


def create_flask(config_object=f'{__package__}.settings'):
    """Create the Flask instance for this application"""
    server = Flask(__package__)
    
    # load default settings
    server.config.from_object(config_object)

    # load additional settings that will override the defaults in settings.py. eg
    # $ export SLAPDASH_SETTINGS=/some/path/prod_settings.py
    server.config.from_envvar('SLAPDASH_SETTINGS', silent=True)

    return server


def create_dash(server):
    """Create the Dash instance for this application"""
    app = Dash(
        server=server,
        external_stylesheets=server.config['EXTERNAL_STYLESHEETS'],
        external_scripts=server.config['EXTERNAL_SCRIPTS'],
        routes_pathname_prefix=server.config['URL_BASE_PATHNAME'],
        suppress_callback_exceptions=True,
    )

    app.title = server.config['TITLE']
    app.scripts.config.serve_locally = server.config['SERVE_LOCALLY']
    app.css.config.serve_locally = server.config['SERVE_LOCALLY']
    return app
