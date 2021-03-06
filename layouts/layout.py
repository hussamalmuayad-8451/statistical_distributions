import dash_core_components as dcc
import dash_html_components as html
import dash_table as dt
import plotly.figure_factory as ff
from collections import namedtuple
from layouts.layout_elements import (
    left_menu,
    left_menu_jnt,
    main_plots,
    joint_plots,
    compare_plots,
    distribution_parameters,
    distribution_parameters_c,
)


##----------------------------------------------------------------
## main layout
##----------------------------------------------------------------

page_1 = html.Div(
    [
        html.Div(
            [html.H1(children="Statistical Distributions")],
            className="title",
            style={"vertical-align": "top"},
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
        html.Div([html.Div(children="created by")], className="footer_a"),
        html.Div([html.Div(children="Hussam Almuayad")], className="footer_b"),
    ],
    className="page",
)




##----------------------------------------------------------------
## main layout
##----------------------------------------------------------------

page_2 = html.Div(
    [
        html.Div(
            [html.H1(children="Statistical Distributions")],
            className="title",
            style={"vertical-align": "top"},
        ),
        html.Div(
            [
                html.Div(
                    left_menu_jnt,
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
                    joint_plots,
                    style={
                        "width": "80%",
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
            ],
            style={"vertical-align": "top"},
        ),
        html.Div([html.Div(children="created by")], className="footer_a"),
        html.Div([html.Div(children="Hussam Almuayad")], className="footer_b"),
    ],
    className="page",
)