from .server import app, server
from .layouts import main_layout_header
from . import router
from . import callbacks


app.title = server.config['TITLE']
app.layout = main_layout_header()
