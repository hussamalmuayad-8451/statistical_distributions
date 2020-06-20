import dash_core_components as dcc
import dash_html_components as html
import dash_table as dt
import plotly.figure_factory as ff

my_distributions = ["Normal","Poisson","Binomial","Student T","Negative Binomial"]



##----------------------------------------------------------------
## distribution parameters
##----------------------------------------------------------------
distribution_parameters=[
                                html.Div(
                                    id="normal",
                                    hidden=False,
                                    children=[
                                        html.Div(children="Mean"),
                                        dcc.Input(type="number", value=1),
                                        html.Div(children="Standard deviation"),
                                        dcc.Input(type="number", value=1),
                                    ],
                                ),
                                html.Div(
                                    id="poisson",
                                    hidden=True,
                                    children=[
                                        html.Div(children="lambda"),
                                        dcc.Input(type="number", value=1),
                                    ],
                                ),
                            ]



##----------------------------------------------------------------
## main layout
##----------------------------------------------------------------

page_1 = html.Div(
    [  # -------------------------------------------------------------------------- div0
        html.Div(
            [  # -------------------------------------------------------------------------- div1-left-panel
                html.Div(
                    [
                        dcc.Dropdown(
                            id="dist_drop",
                            options=[
                                {"label": i, "value": i} for i in my_distributions
                            ],
                            value="Normal",
                        ),
                        html.H6("N observations"),
                        dcc.Input(type="number", value=100),
                        html.Div(
                            distribution_parameters
                        ),
                    ],  # -------------------------------------------------------------------------- div2-top
                    style={"vertical-alight": "top"},
                ),
                html.Div(
                    [],  # -------------------------------------------------------------------------- div2-separator
                    style={"vertical-alight": "top"},
                ),
                html.Div(
                    [
                        dcc.RadioItems(
                            id="onoff",
                            labelStyle = {"display": "inline-block"},
                            options=[{"label": i, "value": i} for i in ["On", "Off"]],
                            value="Off",
                        )
                    ],  # -------------------------------------------------------------------------- div2-bottom
                    style={"vertical-alight": "top"},
                ),
            ],
            style={"width": "35%", "display": "inline-block", "position": "relative"},
            className="div1",
        ),
        html.Div(
            [],  # -------------------------------------------------------------------------- div1-separator
            style={"width": "7%", "display": "inline-block", "position": "relative"},
            className="div1",
        ),
        html.Div(
            [  # -------------------------------------------------------------------------- div1-right-plots
                html.Div(
                    [dcc.Graph(id = "histogram", config={"displayModeBar": False})],  # -------------------------------------------------------------------------- div2-top
                    style={"vertical-align": "top"},
                ),
                html.Div(
                    [],  # -------------------------------------------------------------------------- div2-separator
                    style={"vertical-aligh": "top"},
                ),
                html.Div(
                    # -------------------------------------------------------------------------- div2-bottom
                    [dcc.Graph(id = "scatter", config={"displayModeBar": False})],
                    style={"vertical-aligh": "top"},
                ),
            ],
            style={"width": "55%", "display": "inline-block", "position": "relative"},
            className="div1",
        ),
    ],
    className="div0",
)
