import dash_core_components as dcc
import dash_html_components as html
from dash import Dash
from dash.dependencies import Input, State, Output, Event
from flask import send_from_directory

from . import router


# Assorted parameters
################################################

# where your static files live relative to the top level op the package
STATIC_PATH = 'static'

# The URL your static files will be mounted at 
STATIC_URL_PATH = '/static'

# The ID of the element used to inject each page of the multi-page app into
CONTAINER_ID = 'dash-container'

# The style sheets you want to include in every page of the app. These are
# relative to the STATIC directory
STYLESHEETS = [
    'bootstrap.min.css',
    'font-awesome/css/font-awesome.css',
]



# Make the app!!
################################################

app = Dash()
app.title = 'Slapdash'
app.config['suppress_callback_exceptions'] = True

# This is currently the best way to add local CSS style sheets to a Dash app.
# More convenient support to adding to the <head> should be coming soon.
sheets = [
    html.Link(
        rel='stylesheet',
        href='{}/{}'.format(STATIC_URL_PATH, sheet)
    ) for sheet in STYLESHEETS]

app.layout = html.Div(sheets + [
    html.Div(id=CONTAINER_ID)
])
    


# Register routes of static assets
################################################

# Note that for a scalable app that needs to serve a large number of users, you
# should serve your static assets with a web server such as nginx or Apache,
# rather than with Flask, as we're doing here.


@app.server.route('/static/<path:path>')
def send_static(path):
    return send_from_directory(STATIC_PATH, path)


@app.server.route('/favicon.ico')
def favicon():
    """Serve the favicon"""
    return send_from_directory(
        os.path.join(server.root_path, STATIC_PATH),
        'favicon.ico',
        mimetype='image/vnd.microsoft.icon'
    )


if __name__ == '__main__':
    app.run_server(debug=True)
