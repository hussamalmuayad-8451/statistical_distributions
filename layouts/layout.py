import dash_core_components as dcc
import dash_html_components as html
import dash_table as dt
import plotly.figure_factory as ff
from collections import namedtuple
from layouts.parameters import distribution_parameters, distribution_parameters_c

available_distributions = [
    "normal",
    "poisson",
    "binomial",
    "negative binomial",
    "student T",
    "uniform",
    "beta",
    "chi square",
    "exponential",
    "f",
    "gamma",
    "gumbel",
    "lognormal",
    "cauchy",
    "vonmises",
    "wald",
    "weibull"
]

available_distributions_c = [i+"_c" for i in available_distributions]


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

compare_plots = [
    # -------------------------------------------------------------------------- div1 compare plots open
    html.Div(
        [
            dcc.Graph(id="histogram_c", config={"displayModeBar": False})
        ],  # -------------------------------------------------------------------------- div2 compare histogram
        style={"width": "48%", "display": "inline-block","position": "relative",},
    ),
    html.Div(
        # -------------------------------------------------------------------------- div2 compare scatter
        [dcc.Graph(id="scatter_c", config={"displayModeBar": False})],
        style={"width": "48%", "display": "inline-block","position": "relative",}, #
    ),
]


##----------------------------------------------------------------
## main layout
##----------------------------------------------------------------

page_1 = html.Div(
    # -------------------------------------------------------------------------- div0 open
    [
        html.Div(
            # -------------------------------------------------------------------------- div1 title open
            [html.H1(children="ENTER TITLE HERE")]
            # -------------------------------------------------------------------------- div1 title close
        ),
        html.Div(
            # -------------------------------------------------------------------------- div1 body open
            [
                html.Div(
                    # -------------------------------------------------------------------------- div2 left menu
                    [
                        html.Div(
                            [
                                html.H6("N observations"),
                                dcc.Slider(
                                    id="N",
                                    min=200,
                                    max=9000,
                                    value=4000,
                                    step=200,
                                    marks={
                                        i: f"{str(i)}" for i in range(1000, 10000, 1000)
                                    },
                                ),
                                html.H6("Bins"),
                                dcc.Slider(
                                    id="bins",
                                    min=10,
                                    max=160,
                                    value=10,
                                    step=10,
                                    marks={i: f"{str(i)}" for i in range(10, 180, 30)},
                                ),
                                html.Div(
                                    [
                                        dcc.Dropdown(
                                            id="distribution_name",
                                            options=[
                                                {"label": i.capitalize(), "value": i}
                                                for i in available_distributions
                                            ],
                                            value="normal",
                                            clearable=False,
                                        ),
                                        html.Div(distribution_parameters),
                                        html.Div(id="parameter_registry", hidden=True),
                                    ],
                                    style={"font-size": 14, "margin-top": "20px"},
                                ),
                            ],
                        ),
                        html.Div(
                            [],
                            # -------------------------------------------------------------------------- div2 left on-off separator
                            className="top_spacer",
                        ),
                        html.Div(
                            [
                                dcc.RadioItems(
                                    id="onoff",
                                    labelStyle={"display": "inline-block"},
                                    options=[
                                        {"label": "On", "value": "On"},
                                        {"label": "Off", "value": "Off"},
                                    ],
                                    value="Off",
                                )
                            ],
                            # -------------------------------------------------------------------------- div2 toggle on separator
                        ),
                        html.Div(
                            id="compare_plots_menu",
                            hidden=True,
                            children=html.Div(
                                [
                                    html.H6("N observations"),
                                    dcc.Slider(
                                        id="N_c",
                                        min=200,
                                        max=9000,
                                        value=5000,
                                        step=200,
                                        marks={
                                            i: f"{str(i)}"
                                            for i in range(1000, 9000, 1000)
                                        },
                                    ),
                                    html.Div(
                                        # -------------------------------------------------------------------spacer div
                                        [
                                            dcc.Dropdown(
                                                id="distribution_name_c",
                                                options=[
                                                    {
                                                        "label": i.split("_")[0].capitalize(),
                                                        "value": i,
                                                    }
                                                    for i in available_distributions_c
                                                ],
                                                value="normal_c",
                                                clearable=False,
                                            ),
                                            html.Div(distribution_parameters_c),
                                            html.Div(
                                                id="parameter_registry_c", hidden=True
                                            ),
                                        ],
                                        style={"font-size": 14, "margin-top": "20px"},
                                    ),
                                ]
                            ),
                        ),
                    ],
                    style={
                        "width": "30%",
                        "display": "inline-block",
                        "position": "relative",
                        "vertical-align": "top",
                    },
                    className="div2",
                ),
                html.Div(
                    [],  # -------------------------------------------------------------------------- div2 menu-main plot separator
                    style={
                        "width": "2%",
                        "display": "inline-block",
                        "position": "relative",
                    },
                    #className="div1",
                ),
                html.Div(
                    main_plots,
                    style={
                        "width": "67%",
                        "display": "inline-block",
                        "position": "relative",
                    },
                    className="div1",
                ),
            ], style={"vertical-align": "top"},
            # -------------------------------------------------------------------------- div1 body close
        ),
        html.Div([
        html.Div(
            id="compare_plots",
            hidden=True,
            children=html.Div(compare_plots, className="div0")
            # -------------------------------------------------------------------------- div1 compare plots close
        ),
        ],className="div2_spacer"),
    ], 
    className="page"
    # -------------------------------------------------------------------------- div0 close
)
