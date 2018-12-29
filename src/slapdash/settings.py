# Variables defined in this file will be passed to the 'config' attribute of the
# Flask instance used by the Dash app. They must be in UPPER CASE in order to
# take effect. For more information see http://flask.pocoo.org/docs/config.

# 
# Config for the Dash instance 
#

# Your App's title. The value of this parameter will be propagated into
# `app.title`
TITLE = 'Slapdash'

# The value of this parameter will be propagated into both
# `app.scripts.config.serve_locally` and `app.css.config.serve_locally`
SERVE_LOCALLY = True

# Prefix for Dash URL routes and client-side requests. Passed into Dash's
# `url_base_pathname` keyword argument. Must begin and end with a '/'.
URL_BASE_PATHNAME = '/'

# Custom CSS files go in here. Passed into Dash's `external_stylesheets`
# keyword argument.  If you want to use Bootstrap from a CDN, Dash Bootstrap
# Components contains links to bootstrapcdn:
#
# import dash_bootstrap_components as dbc
# EXTERNAL_STYLESHEETS = [dbc.themes.BOOTSTRAP]
# 
# or if you want to use a Bootswatch theme: 
#
# import dash_bootstrap_components as dbc
# EXTERNAL_STYLESHEETS = [dbc.themes.CYBORG]
EXTERNAL_STYLESHEETS = []

# Custom CSS files go in here. Passed into Dash's `external_scripts` keyword
# argument
EXTERNAL_SCRIPTS = []


#
# Layout config
#

# The ID of the element used to inject each page of the multi-page app into
CONTENT_CONTAINER_ID = 'page-content'

NAVBAR_CONTAINER_ID = 'navbar-items'
