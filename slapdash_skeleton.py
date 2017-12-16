from dash import Dash
from dash.dependencies import Input, State, Output, Event
import dash_core_components as dcc
import dash_html_components as html


app = Dash()
app.title = 'Slapdash Skeleton'


app.layout = html.Div([
        # TODO
        html.Div(id='target'),
        dcc.Input(id='input', type='text', value=''),
        html.Button(id='submit', n_clicks=0, children='Save')
    ]
)


@app.callback(Output('target', 'children'), [Input('submit', 'n_clicks')],
              [State('input', 'value')])
def callback(n_clicks, state):
    return "callback received value: {}".format(state)


if __name__ == '__main__':
    app.run_server()
