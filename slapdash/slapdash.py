from .server import server, app
from .settings import TITLE
from .layouts import main_layout
from . import router
from . import callbacks


app.title = TITLE
app.layout = main_layout()
