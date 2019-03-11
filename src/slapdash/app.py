from . import create_flask, create_dash
from .layouts import main_layout_header, main_layout_sidebar


# The Flask instance
server = create_flask()

# The Dash instance
app = create_dash(server)


# Push an application context so we can use Flask's 'current_app'
with server.app_context():
    # Register the URLS with Flask's config
    # problem is that the URLS require the pages to be imported
    # to get their layouts, but that also triggers the callbacks
    # to be loaded, however the layout has yet to be assigned! crap
    from .urls import URLS

    server.config["URLS"] = URLS

    # configure the Dash instance's layout
    app.layout = main_layout_sidebar

    # load the rest of our Dash app
    from . import index
