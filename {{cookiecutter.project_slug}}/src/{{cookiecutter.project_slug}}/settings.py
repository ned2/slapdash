# Variables defined in this file will be passed to the 'config' attribute of the
# Flask instance used by the Dash app. Any values corresponding to Dash
# keword arguments will be passed They must be in UPPER CASE in order to take effect. For more information see
# http://flask.pocoo.org/docs/config.

# Your App's title. The value of this parameter will be propagated into
# `app.title`
TITLE = "{{ cookiecutter.project_name }}"

# The value of this parameter will be propagated into both
# `app.scripts.config.serve_locally` and `app.css.config.serve_locally`
SERVE_LOCALLY = False


#
# Dash.__init__ keyword arguments
#

# URL prefix for client-side requests and client-side requests. If not None,
# must begin and end with a '/'.
REQUESTS_PATHNAME_PREFIX = None

# URL prefix for server-side routes. If not None, must begin and end with a
# '/'.
ROUTES_PATHNAME_PREFIX = None

# Externally hosted CSS files go in here. If you want to use Bootstrap from a
# CDN, Dash Bootstrap Components contains links to bootstrapcdn:
#
# import dash_bootstrap_components as dbc
# EXTERNAL_STYLESHEETS = [dbc.themes.BOOTSTRAP]
#
# or if you want to use a Bootswatch theme:
#
# import dash_bootstrap_components as dbc
# EXTERNAL_STYLESHEETS = [dbc.themes.CYBORG]
EXTERNAL_STYLESHEETS = []

# Externally hosted Javascript files go in here.
EXTERNAL_SCRIPTS = []


#
# Layout config
#

# The ID of the dcc.Location component used for multi-page apps
LOCATION_COMPONENT_ID = "dash-location"

# The ID of the element used to inject each page of the multi-page app into
CONTENT_CONTAINER_ID = "page-content"

# The ID of the element used to inject the navbar items into
NAVBAR_CONTAINER_ID = "navbar-items"
