import dash_core_components as dcc
import dash_html_components as html
import dash_table as dt
import plotly.figure_factory as ff
from collections import namedtuple
from layouts.layout_elements import (
    left_menu,
    distribution_parameters,
    distribution_parameters_c,
)


##----------------------------------------------------------------
## main_plots
##----------------------------------------------------------------
main_plots = [  # -------------------------------------------------------------------------- div2 main plots
    html.Div(
        [
            dcc.Graph(id="histogram", config={"displayModeBar": False})
        ],  # -------------------------------------------------------------------------- div2-top
        style={"vertical-align": "top"},
    ),
    html.Div(
        [],  # -------------------------------------------------------------------------- div2-separator
        style={"vertical-aligh": "top"},
    ),
    html.Div(
        # -------------------------------------------------------------------------- div2-bottom
        [dcc.Graph(id="scatter", config={"displayModeBar": False})],
        style={"vertical-aligh": "top"},
    ),
]


##----------------------------------------------------------------
## compare_plots
##----------------------------------------------------------------

compare_plots = [  # -------------------------------------------------------------------------- div1 compare plots open
    html.Div(
        [
            dcc.Graph(id="histogram_c", config={"displayModeBar": False})
        ],  # -------------------------------------------------------------------------- div2-top
        style={"vertical-align": "top"},
    ),
    html.Div(
        [],  # -------------------------------------------------------------------------- div2-separator
        style={"vertical-aligh": "top"},
    ),
    html.Div(
        # -------------------------------------------------------------------------- div2-bottom
        [dcc.Graph(id="scatter_c", config={"displayModeBar": False})],
        style={"vertical-aligh": "top"},
    ),
]


##----------------------------------------------------------------
## main layout
##----------------------------------------------------------------

page_1 = html.Div(
    [
        html.Div(
            [html.H1(children="ENTER TITLE HERE")], style={"vertical-align": "top"}
        ),
        html.Div(
            [
                html.Div(
                    left_menu,
                    style={
                        "width": "10%",
                        "display": "inline-block",
                        "position": "relative",
                        "vertical-align": "top",
                    },
                ),
                html.Div(
                    style={
                        "width": "1%",
                        "display": "inline-block",
                        "position": "relative",
                    },
                ),
                html.Div(
                    main_plots,
                    style={
                        "width": "40%",
                        "display": "inline-block",
                        "position": "relative",
                    },
                ),
                html.Div(
                    style={
                        "width": "1%",
                        "display": "inline-block",
                        "position": "relative",
                    },
                ),
                html.Div(
                    [
                        html.Div(
                            id="compare_plots", hidden=True, children=compare_plots,
                        )
                    ],
                    style={
                        "width": "40%",
                        "display": "inline-block",
                        "position": "relative",
                        "vertical-align": "top",
                    },
                ),
            ],
            style={"vertical-align": "top"},
        ),
    ],
    # className="page"
)
