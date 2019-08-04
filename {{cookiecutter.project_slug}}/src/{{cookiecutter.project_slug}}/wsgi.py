from .app import server as application
from .app import app


# When using a WSGI server or running with Flask, the dev tools need to be
# manually enabled. By default debug mode is off. To enable dev mode, set the
# environment variable `DASH_DEBUG` to `true`. You can also turn individual dev
# tools features on using this method. See https://dash.plot.ly/devtools
app.enable_dev_tools(debug=False)
