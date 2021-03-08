import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_table as dt
import plotly.figure_factory as ff
from collections import namedtuple
import copy

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
    "weibull",
]

# available_distributions_c = copy.copy(available_distributions)


##----------------------------------------------------------------
## distribution parameters
##----------------------------------------------------------------
distribution_parameters = [
    html.Div(
        id="normal",
        hidden=False,
        children=[
            html.Div(children="Mean"),
            dcc.Input(id="mean", type="number", value=0),
            html.Div(children="Standard deviation"),
            dcc.Input(id="standard_deviation", type="number", value=1),
        ],
    ),
    html.Div(
        id="poisson",
        hidden=True,
        children=[
            html.Div(children="lambda"),
            dcc.Input(id="lambda", type="number", value=1),
        ],
    ),
    html.Div(
        id="binomial",
        hidden=True,
        children=[
            html.Div(children="n (bernoulli trial)", style={"font-style": "italic"}),
            dcc.Input(id="n", type="number", value=10),
            html.Div(
                children="p (probability of success)", style={"font-style": "italic"}
            ),
            dcc.Input(id="p", type="number", value=0.5, min=0, max=1, step=0.1),
        ],
    ),
    html.Div(
        id="nbinomial",
        hidden=True,
        children=[
            html.Div(
                children="r (failures before success)", style={"font-style": "italic"}
            ),
            dcc.Input(id="r", type="number", value=5, min=0, step=1),
            html.Div(
                children="p (probability of success)", style={"font-style": "italic"}
            ),
            dcc.Input(id="p", type="number", value=0.5, min=0, max=1, step=0.1),
        ],
    ),
    html.Div(
        id="student",
        hidden=True,
        children=[
            html.Div(children="Degreed of Freedom", style={"font-style": "italic"}),
            dcc.Input(id="df", type="number", value=2, min=1, step=1),
        ],
    ),
    html.Div(
        id="uniform",
        hidden=True,
        children=[
            html.Div(children="Alpha", style={"font-style": "italic"}),
            dcc.Input(id="alpha_", type="number", value=0, step=1),
            html.Div(children="Beta", style={"font-style": "italic"}),
            dcc.Input(id="beta_", type="number", value=1, step=1),
        ],
    ),
    html.Div(
        id="beta",
        hidden=True,
        children=[
            html.Div(children=f"{chr(945)} (shape)", style={"font-style": "italic"}),
            dcc.Input(id="alpha_", type="number", value=2, min=1, step=1),
            html.Div(children=f"{chr(946)} (scale)", style={"font-style": "italic"}),
            dcc.Input(id="beta_", type="number", value=3, min=1, step=1),
        ],
    ),
    html.Div(
        id="chisq",
        hidden=True,
        children=[
            html.Div(children="Degreed of Freedom", style={"font-style": "italic"}),
            dcc.Input(id="df", type="number", value=2, min=1, step=1),
        ],
    ),
    html.Div(
        id="exponential",
        hidden=True,
        children=[
            html.Div(children="Lambda", style={"font-style": "italic"}),
            dcc.Input(id="lambda", type="number", value=3, min=1, step=0.1),
        ],
    ),
    html.Div(
        id="f",
        hidden=True,
        children=[
            html.Div(children="Degrees of Freedom 1", style={"font-style": "italic"}),
            dcc.Input(id="df_1", type="number", value=5, min=1, step=1),
            html.Div(children="Degrees of Freedom 2", style={"font-style": "italic"}),
            dcc.Input(id="df_2", type="number", value=9, min=1, step=1),
        ],
    ),
    html.Div(
        id="gamma",
        hidden=True,
        children=[
            html.Div(children=f"{chr(952)} (shape)", style={"font-style": "italic"}),
            dcc.Input(id="kappa", type="number", value=1, min=1, step=0.1),
            html.Div(children=f"{chr(954)} (scale)", style={"font-style": "italic"}),
            dcc.Input(id="theta", type="number", value=3, min=1, step=0.1),
        ],
    ),
    html.Div(
        id="gumbel",
        hidden=True,
        children=[
            html.Div(children="Mean", style={"font-style": "italic"}),
            dcc.Input(id="mean", type="number", value=0),
            html.Div(children=f"{chr(946)} (scale)", style={"font-style": "italic"}),
            dcc.Input(id="beta_", type="number", value=2, min=0, step=0.1),
        ],
    ),
    html.Div(
        id="lognormal",
        hidden=True,
        children=[
            html.Div(children="Mean"),
            dcc.Input(id="mean", type="number", value=0),
            html.Div(children="Standard deviation"),
            dcc.Input(id="standard_deviation", type="number", value=1),
        ],
    ),
    html.Div(
        id="cauchy",
        hidden=True,
        children=[
            html.Div(children="No Parameters Required", style={"font-style": "italic"}),
        ],
    ),
    html.Div(
        id="vonmises",
        hidden=True,
        children=[
            html.Div(children="Mean", style={"font-style": "italic"}),
            dcc.Input(id="mean", type="number", value=0),
            html.Div(
                children=f"{chr(952)} (concentration)", style={"font-style": "italic"}
            ),
            dcc.Input(id="kappa", type="number", value=1, min=1, step=0.5),
        ],
    ),
    html.Div(
        id="wald",
        hidden=True,
        children=[
            html.Div(children="Mean", style={"font-style": "italic"}),
            dcc.Input(id="mean", type="number", value=0),
            html.Div(children=f"{chr(955)} (shape)", style={"font-style": "italic"}),
            dcc.Input(id="lambda", type="number", value=1, min=1, step=0.5),
        ],
    ),
    html.Div(
        id="weibull",
        hidden=True,
        children=[
            html.Div(children=f"{chr(955)} (scale)", style={"font-style": "italic"}),
            dcc.Input(id="lambda", type="number", value=1, min=1, step=0.1),
        ],
    ),
]


##----------------------------------------------------------------
## distribution parameters_c
##----------------------------------------------------------------
distribution_parameters_c = [
    html.Div(
        id="normal_c",
        hidden=False,
        children=[
            html.Div(children="Mean"),
            dcc.Input(id="mean_c", type="number", value=0),
            html.Div(children="Standard deviation"),
            dcc.Input(id="standard_deviation_c", type="number", value=1),
        ],
    ),
    html.Div(
        id="poisson_c",
        hidden=True,
        children=[
            html.Div(children="lambda"),
            dcc.Input(id="lambda_c", type="number", value=1),
        ],
    ),
    html.Div(
        id="binomial_c",
        hidden=True,
        children=[
            html.Div(children="n (bernoulli trial)", style={"font-style": "italic"}),
            dcc.Input(id="n_c", type="number", value=10),
            html.Div(
                children="p (probability of success)", style={"font-style": "italic"}
            ),
            dcc.Input(id="p_c", type="number", value=0.5, min=0, max=1, step=0.1),
        ],
    ),
    html.Div(
        id="nbinomial_c",
        hidden=True,
        children=[
            html.Div(
                children="r (failures beforee success)", style={"font-style": "italic"}
            ),
            dcc.Input(id="r_c", type="number", value=5, min=0, step=1),
            html.Div(
                children="p (probability of success)", style={"font-style": "italic"}
            ),
            dcc.Input(id="p_c", type="number", value=0.5, min=0, max=1, step=0.1),
        ],
    ),
    html.Div(
        id="student_c",
        hidden=True,
        children=[
            html.Div(children="Degreed of Freedom", style={"font-style": "italic"}),
            dcc.Input(id="df_c", type="number", value=2, min=1, step=1),
        ],
    ),
    html.Div(
        id="uniform_c",
        hidden=True,
        children=[
            html.Div(children="Alpha", style={"font-style": "italic"}),
            dcc.Input(id="alpha_c", type="number", value=0, step=1),
            html.Div(children="Beta", style={"font-style": "italic"}),
            dcc.Input(id="beta_c", type="number", value=1, step=1),
        ],
    ),
    html.Div(
        id="beta_c",
        hidden=True,
        children=[
            html.Div(children=f"{chr(945)} (shape)", style={"font-style": "italic"}),
            dcc.Input(id="alpha_c", type="number", value=2, min=1, step=1),
            html.Div(children=f"{chr(946)} (scale)", style={"font-style": "italic"}),
            dcc.Input(id="beta_c", type="number", value=3, min=1, step=1),
        ],
    ),
    html.Div(
        id="chisq_c",
        hidden=True,
        children=[
            html.Div(children="Degreed of Freedom", style={"font-style": "italic"}),
            dcc.Input(id="df_c", type="number", value=2, min=1, step=1),
        ],
    ),
    html.Div(
        id="exponential_c",
        hidden=True,
        children=[
            html.Div(children="Lambda", style={"font-style": "italic"}),
            dcc.Input(id="lambda_c", type="number", value=3, min=1, step=0.1),
        ],
    ),
    html.Div(
        id="f_c",
        hidden=True,
        children=[
            html.Div(children="Degrees of Freedom 1", style={"font-style": "italic"}),
            dcc.Input(id="df_1_c", type="number", value=5, min=1, step=1),
            html.Div(children="Degrees of Freedom 2", style={"font-style": "italic"}),
            dcc.Input(id="df_2_c", type="number", value=9, min=1, step=1),
        ],
    ),
    html.Div(
        id="gamma_c",
        hidden=True,
        children=[
            html.Div(children=f"{chr(952)} (shape)", style={"font-style": "italic"}),
            dcc.Input(id="kappa_c", type="number", value=1, min=1, step=0.1),
            html.Div(children=f"{chr(954)} (scale)", style={"font-style": "italic"}),
            dcc.Input(id="theta_c", type="number", value=3, min=1, step=0.1),
        ],
    ),
    html.Div(
        id="gumbel_c",
        hidden=True,
        children=[
            html.Div(children="Mean", style={"font-style": "italic"}),
            dcc.Input(id="mean_c", type="number", value=0),
            html.Div(children=f"{chr(946)} (scale)", style={"font-style": "italic"}),
            dcc.Input(id="beta_c", type="number", value=2, min=0, step=0.1),
        ],
    ),
    html.Div(
        id="lognormal_c",
        hidden=True,
        children=[
            html.Div(children="Mean"),
            dcc.Input(id="mean_c", type="number", value=0),
            html.Div(children="Standard deviation"),
            dcc.Input(id="standard_deviation", type="number", value=1),
        ],
    ),
    html.Div(
        id="cauchy_c",
        hidden=True,
        children=[
            html.Div(children="No Parameters Required", style={"font-style": "italic"}),
        ],
    ),
    html.Div(
        id="vonmises_c",
        hidden=True,
        children=[
            html.Div(children="Mean", style={"font-style": "italic"}),
            dcc.Input(id="mean_c", type="number", value=0),
            html.Div(
                children=f"{chr(952)} (concentration)", style={"font-style": "italic"}
            ),
            dcc.Input(id="kappa", type="number", value=1, min=1, step=0.5),
        ],
    ),
    html.Div(
        id="wald_c",
        hidden=True,
        children=[
            html.Div(children="Mean", style={"font-style": "italic"}),
            dcc.Input(id="mean_c", type="number", value=0),
            html.Div(children=f"{chr(955)} (shape)", style={"font-style": "italic"}),
            dcc.Input(id="lambda_c", type="number", value=1, min=1, step=0.5),
        ],
    ),
    html.Div(
        id="weibull_c",
        hidden=True,
        children=[
            html.Div(children=f"{chr(955)} (scale)", style={"font-style": "italic"}),
            dcc.Input(id="lambda_c", type="number", value=1, min=1, step=0.1),
        ],
    ),
]


##----------------------------------------------------------------
## left_menu
##----------------------------------------------------------------
left_menu = [
    html.Div(
        [
            html.H6("Bins"),
            dcc.Slider(
                id="bins",
                min=10,
                max=200,
                value=10,
                step=10,
                marks={i: f"{str(i)}" for i in [10, 50, 100, 150, 200]},
            ),
            html.H6("N observations"),
            dcc.Slider(
                id="N",
                min=200,
                max=3000,
                value=1500,
                step=200,
                marks={i: f"{str(i)}" for i in [200, 500, 1000, 2000, 3000]},
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
        [dcc.Checklist(id="onoff", options=[{"label": " COMPARE", "value": "Yes"},])]
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
                    max=3000,
                    value=1500,
                    step=200,
                    marks={i: f"{str(i)}" for i in [200, 500, 1000, 2000, 3000]},
                ),
                html.Div(
                    # -------------------------------------------------------------------spacer div
                    [
                        dcc.Dropdown(
                            id="distribution_name_c",
                            options=[
                                {"label": i.split("_")[0].capitalize(), "value": i,}
                                for i in available_distributions
                            ],
                            value="normal",
                            clearable=False,
                        ),
                        html.Div(distribution_parameters_c),
                        html.Div(id="parameter_registry_c", hidden=True),
                    ],
                    style={"font-size": 14, "margin-top": "20px"},
                ),
            ]
        ),
    ),
]
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