from .server import server, app
from .settings import TITLE
from .layouts import main_layout_header, main_layout_sidebar
from . import router
from . import callbacks


app.title = TITLE
app.layout = main_layout_sidebar()
