# Your Apps title
TITLE = 'Slapdash'

# URL PREFIX the the app will be mounted at 
URL_BASE_PATHNAME = '/'

# where your static files live relative to the top level op the package
STATIC_FOLDER = 'static'

# The URL your static files will be mounted at 
STATIC_URL_PATH = '/static'

# The ID of the element used to inject each page of the multi-page app into
CONTAINER_ID = 'dash-container'

# The style sheets you want to include in every page of the app. These are
# relative to the STATIC_URL_PATH
STYLESHEETS = [
    'slapdash.css',
    'bootstrap.min.css',
    'font-awesome/css/font-awesome.css',
]
