from collections import Counter

import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, State, Output

from ..app import app
from ..components import Col, Row


layout = html.Div([
    dcc.Markdown("""
# Character Counter

This demo counts the number of characters in the text box and updates a bar
chart with their frequency as you type."""),
    html.Div(
        dcc.Textarea(
            id='text-input',
            value='Type some text into me!',
            style={'width':'40em', 'height': '5em'},
        )
    ),
    html.Div('Sort by:'),
    dcc.RadioItems(
        id='sort-type',
        options=[
            {'label': 'Frequency', 'value': 'frequency'},
            {'label': 'Character code', 'value': 'code'},
        ],
        value='frequency'
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
    dcc.Graph(id='graph', className='red')
])


@app.callback(
    Output('graph', 'figure'),      # Output
    [Input('text-input', 'value'),  # Inputs
     Input('sort-type', 'value'),
     Input('normalize', 'value')],  
    [],                             # States
)
def callback(text, sort_type, normalize):
    if normalize == 'yes':
        text = text.lower()

    if sort_type == 'frequency':
        sort_func = lambda x:-x[1]
    else:
        sort_func = lambda x:ord(x[0])
        
    counts = Counter(text)

    if len(counts) == 0:
        x_data = []
        y_data = []
    else:
        x_data, y_data = zip(*sorted(
            counts.items(),
            key=sort_func))
    return {
        'data': [
            {'x': x_data, 'y':y_data, 'type': 'bar', 'name': 'trace1'},
        ],
        'layout': {
            'title': 'Frequency of Characters',
            'height': '600',
            'font': {'size': 16}
        },
    }

