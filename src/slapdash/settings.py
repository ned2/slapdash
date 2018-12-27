# These parameters will be passed to the 'config' attribute of the Flask
# instance used by the Dash app. They must be in UPPER CASE in order to take
# effect. For more information see http://flask.pocoo.org/docs/config.

# 
# Config for the Dash instance 
#

# Your App's title
TITLE = 'Slapdash'

# Prefix 
ROUTES_PATHNAME_PREFIX = '/'

# If you want to use Bootstrap from a CDN, Dash Bootstrap Components contains
# links to bootstrapcdn:
#
# import dash_bootstrap_components as dbc
# EXTERNAL_STYLESHEETS = [dbc.themes.BOOTSTRAP]
# 
# or if you want to use a Bootswatch theme: 
# import dash_bootstrap_components as dbc
# EXTERNAL_STYLESHEETS = [dbc.themes.CERULEAN]
EXTERNAL_STYLESHEETS = []


#
# Other Slapdash config
#

# The ID of the element used to inject each page of the multi-page app into
CONTENT_CONTAINER_ID = 'dash-container'

NAVBAR_CONTAINER_ID = 'navbar'

# Ordered iterable of navbar items: tuples of (route, name), where 'route' is a
# string corresponding to path of the route (will be prefixed with
# URL_BASE_PATHNAME) and 'name' is a string corresponding to the name of the nav
# item.
NAV_ITEMS = (
    ('page1', 'Page 1'),
    ('page2', 'Page 2'),
    ('page3', 'Page 3'),
)

