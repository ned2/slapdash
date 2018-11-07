from dash import Dash
from flask import Flask

#
# The Flask instance
#
server = Flask(__package__)

# load default settings from settings.py
server.config.from_object(f'{__package__}.settings')

# load additional settings that will override the defaults in settings.py. eg
# $ export SLAPDASH_SETTINGS=/some/path/prod_settings.py
server.config.from_envvar('SLAPDASH_SETTINGS', silent=True)


#
# The Dash instance
#
app = Dash(server=server)

app.title = server.config['TITLE']

# Suppress callback validation as we will be initialising callbacks that target
# element IDs that won't yet occur in the layout.
app.config.supress_callback_exceptions = True

