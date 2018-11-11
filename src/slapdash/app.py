from . import create_app, create_dash
from .layouts import main_layout_header


# The Flask instance
server = create_app()

# The Dash instance
app = create_dash(server)

# Push an application context so we can use Flask's 'current_app'
with server.app_context():
    # configure the Dash instance's layout
    app.layout = main_layout_header()

    from . import index
