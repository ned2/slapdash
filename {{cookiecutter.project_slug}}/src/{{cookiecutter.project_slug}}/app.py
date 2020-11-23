from . import create_flask, create_dash
from .router import DashRouter
from .navbar import DashNavBar


# The Flask instance
server = create_flask()

# The Dash instance
app = create_dash(server)

# The URL router 
router = DashRouter(app)

# The Navigation Bar
navbar = DashNavBar(app, router)
