from collections import Counter
from textwrap import dedent

import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, State, Output

from ..app import app


def get_layout(**kwargs):
    initial_text = kwargs.get("text", "Type some text into me!")

    # Note that if you need to access multiple values of an argument, you can
    # use args.getlist("param")
    return html.Div(
        [
            dcc.Markdown(
                dedent(
                    """
                    # Character Counter
                    
                    This demo counts the number of characters in the text box and
                    updates a bar chart with their frequency as you type.
                    """
                )
            ),
            dbc.FormGroup(
                dbc.Textarea(
                    id="text-input",
                    value=initial_text,
                    style={"width": "40em", "height": "5em"},
                )
            ),
            dbc.FormGroup(
                [
                    dbc.Label("Sort by:"),
                    dbc.RadioItems(
                        id="sort-type",
                        options=[
                            {"label": "Frequency", "value": "frequency"},
                            {"label": "Character code", "value": "code"},
                        ],
                        value="frequency",
                    ),
                ]
            ),
            dbc.FormGroup(
                [
                    dbc.Label("Normalize character case?"),
                    dbc.RadioItems(
                        id="normalize",
                        options=[
                            {"label": "No", "value": "no"},
                            {"label": "Yes", "value": "yes"},
                        ],
                        value="no",
                    ),
                ]
            ),
            dcc.Graph(id="graph"),
        ]
    )


@app.callback(
    Output("graph", "figure"),
    [
        Input("text-input", "value"),
        Input("sort-type", "value"),
        Input("normalize", "value"),
    ],
    [],  # States
)
def callback(text, sort_type, normalize):
    if normalize == "yes":
        text = text.lower()

    if sort_type == "frequency":
        sort_func = lambda x: -x[1]
    else:
        sort_func = lambda x: ord(x[0])

    counts = Counter(text)

    if len(counts) == 0:
        x_data = []
        y_data = []
    else:
        x_data, y_data = zip(*sorted(counts.items(), key=sort_func))
    return {
        "data": [{"x": x_data, "y": y_data, "type": "bar", "name": "trace1"}],
        "layout": {
            "title": "Frequency of Characters",
            "height": "600",
            "font": {"size": 16},
        },
    }
