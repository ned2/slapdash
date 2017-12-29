import dash_core_components as dcc
import dash_html_components as html

from .server import server, app
from . import settings
from . import router
from . import callbacks


app.title = settings.TITLE

app.layout = html.Div([
    html.Div(id=settings.CONTAINER_ID),
    dcc.Location(id='url', refresh=False)
])

