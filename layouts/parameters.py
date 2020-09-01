import dash_core_components as dcc
import dash_html_components as html
import dash_table as dt
import plotly.figure_factory as ff
from collections import namedtuple

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
            dcc.Input(id="alpha", type="number", value=0, step=1),
            html.Div(children="Beta", style={"font-style": "italic"}),
            dcc.Input(id="beta", type="number", value=1, step=1),
        ],
    ),
    html.Div(
        id="beta",
        hidden=True,
        children=[
            html.Div(children="Shape", style={"font-style": "italic"}),
            dcc.Input(id="alpha", type="number", value=2, min=1, step=1),
            html.Div(children="Scale", style={"font-style": "italic"}),
            dcc.Input(id="beta", type="number", value=3, min=1, step=1),
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
            dcc.Input(id="df_1", type="number", value=2, min=1, step=1),
            html.Div(children="Degrees of Freedom 2", style={"font-style": "italic"}),
            dcc.Input(id="df_2", type="number", value=2, min=1, step=1),
        ],
    ),
    html.Div(
        id="gamma",
        hidden=True,
        children=[
            html.Div(children="Kappa (shape)", style={"font-style": "italic"}),
            dcc.Input(id="kappa", type="number", value=1, min=1, step=0.1),
            html.Div(children="Theta (scale)", style={"font-style": "italic"}),
            dcc.Input(id="theta", type="number", value=3, min=1, step=0.1),
        ],
    ),
    html.Div(
        id="gumbel",
        hidden=True,
        children=[
            html.Div(children="Mean", style={"font-style": "italic"}),
            dcc.Input(id="mean", type="number", value=0),
            html.Div(children="Beta (scale)", style={"font-style": "italic"}),
            dcc.Input(id="beta", type="number", value=2, min=0, step=0.1),
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
            html.Div(children="Kappa (concentration)", style={"font-style": "italic"}),
            dcc.Input(id="kappa", type="number", value=1, min=1, step=0.5),
        ],
    ),
    html.Div(
        id="wald",
        hidden=True,
        children=[
            html.Div(children="Mean", style={"font-style": "italic"}),
            dcc.Input(id="mean", type="number", value=0),
            html.Div(children="Lambda (shape)", style={"font-style": "italic"}),
            dcc.Input(id="lambda", type="number", value=1, min=1, step=0.5),
        ],
    ),
    html.Div(
        id="weibull",
        hidden=True,
        children=[
            html.Div(children="Lambda (scale)", style={"font-style": "italic"}),
            dcc.Input(id="lambda", type="number", value=1, min=1, step=0.1),
        ],
    ),
]


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
]
