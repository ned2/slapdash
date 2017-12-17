"""A Skeleton template for bootstrapping creation of Plotly Dash apps.

Some useful references:

1. The Dash User Guide
   https://plot.ly/dash

2. Plotly Python client figure reference -- documents the contents of
   plotly.graph_objs, which contains the different types of charts available, as
   well the Layout class, for customising the appearance of charts.
   https://plot.ly/python/reference

3. The Dash Community Forum
   https://community.plot.ly/c/dash

"""
from collections import Counter

from dash import Dash
from dash.dependencies import Input, State, Output, Event
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
#import dash_table_experiments as dt 


app = Dash()
app.title = 'Dash Skeleton'


app.layout = html.Div([
    dcc.Markdown("""
# Dash Skeleton app

This demo app counts the number of characters in the text box and updates a bar
chart with their frequency as you type."""),
    html.Div(
        dcc.Textarea(
            id='text-input',
            value='Type some text into me!',
            style={'width':'40em', 'height': '5em'},
        )
    ),
    html.Div('Normalize character case?'),
    dcc.RadioItems(
        id='normalize',
        options=[
            {'label': 'No', 'value': 'no'},
            {'label': 'Yes', 'value': 'yes'},
        ],
        value='no'
    ),
    dcc.Graph(id='graph')
])


@app.callback(
    Output('graph', 'figure'),                                    # Output
    [Input('text-input', 'value'), Input('normalize', 'value')],  # Inputs
    [],                                                           # States
    []                                                            # Events
)
def callback(text, normalize):
    if normalize == 'yes':
        text = text.lower()

    counts = Counter(text)

    if len(counts) == 0:
        x_data = []
        y_data = []
    else:
        x_data, y_data = zip(*sorted(
            counts.items(),
            reverse=True,
            key=lambda x:x[1]))
    return {
        'data': [
            {'x': x_data, 'y':y_data, 'type': 'bar', 'name': 'trace1'},
        ],
        'layout': {
            'title': 'Frequency of Characters',
            'height': '600',
            'font': {'size': 16}
        }
    }


if __name__ == '__main__':
    # To make this app publicly available, supply the parameter host='0.0.0.0'.
    # You should also disable debug mode in production.
    app.run_server(debug=True, port=8050)
