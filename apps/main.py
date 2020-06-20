from copy import copy
from dash.dependencies import Input, Output, State
from collections import defaultdict
import plotly.graph_objs as go

from layouts.layout import page_1
from app import app



@app.callback(
    [Output("normal","hidden"),
     Output("poisson","hidden")],
     [Input("dist_drop","value")]
)
def display_parameters(value):
    if value == "Normal":
        return (False, True)
    elif value == "Poisson":
        return (True, False)

@app.callback(
            Output("histogram","figure"),
            [Input("dist_drop","value"),
            Input("",""),