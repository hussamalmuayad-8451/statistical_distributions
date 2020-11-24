from copy import copy
from dash.dependencies import Input, Output, State
from collections import defaultdict
import plotly.graph_objs as go
import plotly.figure_factory as ff
import numpy as np
from layouts.layout import page_1
from app import app

from collections import namedtuple

# mean standard deviation
normal = namedtuple("normal", "N mean standard_deviation")
# lambda
poisson = namedtuple("poisson", "N mean")
# n bernouli trials p probability(0,1)
binomial = namedtuple("binomial", "N n p")
# r number of failures before a success >0, p probability of success (0,1)
nbinomial = namedtuple("nbinomial", "N r p")
# df degrees of freedom >0
student = namedtuple("student", "N df")
# a min, b max
uniform = namedtuple("uniform", "N a b")
# a shape >0, b shape>0
beta = namedtuple("beta", "N a b")
# df degrees of freedom >0
chisq = namedtuple("chisq", "N k")
# lambda > 0, mean=1/lambda
exponential = namedtuple("exponential", "N lambda_")
# df_1, df_2 of two chi square distributions
f = namedtuple("f", "N df_1 df_2")
# k shape > 0, theta scale > 0
gamma = namedtuple("gamma", "N k theta")
# mean, beta: scale > 0
gumbel = namedtuple("gumbel", "N mean beta")
lognormal = namedtuple("lognormal", "N mean standard_deviation")
cauchy = namedtuple("cauchy", "N")
# mean, kappa > 0
vonmises = namedtuple("vonmises", "N mean kappa")
# mean > 0 ,lambda (shape)> 0
wald = namedtuple("wald", "N mean lambda_")
# lambda scale > 0 kappa shape > 0
weibull = namedtuple("weibull", "N lambda_")


@app.callback(Output("N", "value"), [Input("distribution_name", "value")])
def adjust_bins(value):
    if value == "student T":
        return 70
    elif value == "cauchy":
        return 300
    elif value == "uniform":
        return 30
    else:
        return 1500


# ---------------------------------------------------------------- main plots
@app.callback(
    [
        Output("normal", "hidden"),
        Output("poisson", "hidden"),
        Output("binomial", "hidden"),
        Output("nbinomial", "hidden"),
        Output("student", "hidden"),
        Output("uniform", "hidden"),
        Output("beta", "hidden"),
        Output("chisq", "hidden"),
        Output("exponential", "hidden"),
        Output("f", "hidden"),
        Output("gamma", "hidden"),
        Output("gumbel", "hidden"),
        Output("lognormal", "hidden"),
        Output("cauchy", "hidden"),
        Output("vonmises", "hidden"),
        Output("wald", "hidden"),
        Output("weibull", "hidden"),
    ],
    [Input("distribution_name", "value")],
)
def display_parameters(value):
    if value == "normal":
        return (
            False,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
        )
    elif value == "poisson":
        return (
            True,
            False,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
        )
    elif value == "binomial":
        return (
            True,
            True,
            False,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
        )
    elif value == "negative binomial":
        return (
            True,
            True,
            True,
            False,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
        )
    elif value == "student T":
        return (
            True,
            True,
            True,
            True,
            False,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
        )
    elif value == "uniform":
        return (
            True,
            True,
            True,
            True,
            True,
            False,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
        )
    elif value == "beta":
        return (
            True,
            True,
            True,
            True,
            True,
            True,
            False,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
        )
    elif value == "chi square":
        return (
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            False,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
        )
    elif value == "exponential":
        return (
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            False,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
        )
    elif value == "f":
        return (
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            False,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
        )
    elif value == "gamma":
        return (
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            False,
            True,
            True,
            True,
            True,
            True,
            True,
        )
    elif value == "gumbel":
        return (
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            False,
            True,
            True,
            True,
            True,
            True,
        )
    elif value == "lognormal":
        return (
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            False,
            True,
            True,
            True,
            True,
        )
    elif value == "cauchy":
        return (
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            False,
            True,
            True,
            True,
        )
    elif value == "vonmises":
        return (
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            False,
            True,
            True,
        )
    elif value == "wald":
        return (
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            False,
            True,
        )
    else:
        return (
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            False,
        )


@app.callback(
    Output("parameter_registry", "children"),
    [
        Input("distribution_name", "value"),  # args[0]
        Input("N", "value"),  # args[1] normal
        Input("mean", "value"),  # args[2] normal
        Input("standard_deviation", "value"),  # args[3] normal
        Input("lambda", "value"),  # args[4] poisson
        Input("n", "value"),  # args[5] binomial
        Input("p", "value"),  # args[6] binomail
        Input("r", "value"),  # args[7] nbinomail
        Input("p", "value"),  # args[8] nbinomail
        Input("df", "value"),  # args[9] studentt
        Input("alpha_", "value"),  # args[10] uniform
        Input("beta_", "value"),  # args[11] uniform
        Input("alpha_", "value"),  # args[12] beta
        Input("beta_", "value"),  # args[13] beta
        Input("df", "value"),  # args[14] chisq
        Input("lambda", "value"),  # args[15] exponential
        Input("df_1", "value"),  # args[16] f
        Input("df_2", "value"),  # args[17] f
        Input("kappa", "value"),  # args[18] gamma
        Input("theta", "value"),  # args[19] gamma
        Input("mean", "value"),  # args[20] gumbel
        Input("beta_", "value"),  # args[21] gumbel
        Input("mean", "value"),  # args[22] lognormal
        Input("standard_deviation", "value"),  # args[23] lognormal
        Input("mean", "value"),  # args[24] vonmises
        Input("kappa", "value"),  # args[25] vonmises
        Input("mean", "value"),  # args[26] wald
        Input("lambda", "value"),  # args[27] wald
        Input("lambda", "value"),  # args[28] weibull
    ],
)
def registry_updater(*args):
    if args[0] == "normal":
        normal_parameters = normal._make([args[1], args[2], args[3]])
        return normal_parameters
    elif args[0] == "poisson":
        poisson_parameters = poisson._make([args[1], args[4]])
        return poisson_parameters
    elif args[0] == "binomial":
        binomial_parameters = binomial._make([args[1], args[5], args[6]])
        return binomial_parameters
    elif args[0] == "negative binomial":
        nbinomial_parameters = nbinomial._make([args[1], args[7], args[8]])
        return nbinomial_parameters
    elif args[0] == "student T":
        student_parameters = student._make([args[1], args[9]])
        return student_parameters
    elif args[0] == "uniform":
        uniform_parameters = uniform._make([args[1], args[10], args[11]])
        return uniform_parameters
    elif args[0] == "beta":
        beta_parameters = beta._make([args[1], args[12], args[13]])
        return beta_parameters
    elif args[0] == "chi square":
        chisq_parameters = chisq._make([args[1], args[14]])
        return chisq_parameters
    elif args[0] == "exponential":
        exponential_parameters = exponential._make([args[1], args[15]])
        return exponential_parameters
    elif args[0] == "f":
        f_parameters = f._make([args[1], args[16], args[17]])
        return f_parameters
    elif args[0] == "gamma":
        gamma_parameters = gamma._make([args[1], args[18], args[19]])
        return gamma_parameters
    elif args[0] == "gumbel":
        gumbel_parameters = gumbel._make([args[1], args[20], args[21]])
        return gumbel_parameters
    elif args[0] == "lognormal":
        lognormal_parameters = lognormal._make([args[1], args[22], args[23]])
        return lognormal_parameters
    elif args[0] == "cauchy":
        cauchy_parameters = cauchy._make([args[1]])
        return cauchy_parameters
    elif args[0] == "vonmises":
        vonmises_parameters = vonmises._make([args[1], args[24], args[25]])
        return vonmises_parameters
    elif args[0] == "wald":
        wald_parameters = wald._make([args[1], args[26], args[27]])
        return wald_parameters
    elif args[0] == "weibull":
        weibull_parameters = weibull._make([args[1], args[28]])
        return weibull_parameters
    else:
        normal_parameters = normal._make([args[1], args[2], args[3]])
        return normal_parameters


@app.callback(
    [Output("histogram", "figure"), Output("scatter", "figure")],
    [
        Input("distribution_name", "value"),
        Input("parameter_registry", "children"),
        Input("bins", "value"),
    ],
)
def update_histogram(*args):
    distribution_name, parameters, bins = args

    if distribution_name == "normal":
        random_var = np.random.normal(
            loc=parameters[1], scale=parameters[2], size=parameters[0]
        )
    elif distribution_name == "poisson":
        random_var = np.random.poisson(lam=parameters[1], size=parameters[0])
    elif distribution_name == "binomial":
        random_var = np.random.binomial(
            n=parameters[1], p=parameters[2], size=parameters[0]
        )
    elif distribution_name == "negative binomial":
        random_var = np.random.negative_binomial(
            n=parameters[1], p=parameters[2], size=parameters[0]
        )
    elif distribution_name == "student T":
        random_var = np.random.standard_t(df=parameters[1], size=parameters[0])
    elif distribution_name == "uniform":
        random_var = np.random.uniform(
            low=parameters[1], high=parameters[2], size=parameters[0]
        )
    elif distribution_name == "beta":
        random_var = np.random.beta(
            a=parameters[1], b=parameters[2], size=parameters[0]
        )
    elif distribution_name == "chi square":
        random_var = np.random.chisquare(df=parameters[1], size=parameters[0])
    elif distribution_name == "exponential":
        random_var = np.random.exponential(scale=parameters[1], size=parameters[0])
    elif distribution_name == "f":
        random_var = np.random.f(
            dfnum=parameters[1], dfden=parameters[2], size=parameters[0]
        )
    elif distribution_name == "gamma":
        random_var = np.random.gamma(
            shape=parameters[1], scale=parameters[2], size=parameters[0]
        )
    elif distribution_name == "gumbel":
        random_var = np.random.gumbel(
            loc=parameters[1], scale=parameters[2], size=parameters[0]
        )
    elif distribution_name == "lognormal":
        random_var = np.random.lognormal(
            mean=parameters[1], sigma=parameters[2], size=parameters[0]
        )
    elif distribution_name == "cauchy":
        random_var = np.random.standard_cauchy(size=parameters[0])
    elif distribution_name == "vonmises":
        random_var = np.random.vonmises(
            mu=parameters[1], kappa=parameters[2], size=parameters[0]
        )
    elif distribution_name == "wald":
        random_var = np.random.wald(
            mean=parameters[1], scale=parameters[2], size=parameters[0]
        )
    elif distribution_name == "weibull":
        random_var = np.random.weibull(a=parameters[1], size=parameters[0])
    else:
        random_var = np.random.normal(
            loc=parameters[1], scale=parameters[2], size=parameters[0]
        )

    hist_0 = go.Histogram(
        {
            "x": random_var.tolist(),
            "nbinsx": bins,
            "autobinx": True,
            "marker": {
                "color": "#eb89b5",
                "line": {"width": 1, "color": "MediumPurple",},
            },
            "opacity": 0.75,
        }
    )

    hist_0_layout = {
        "title": f"Probability Density - {distribution_name.capitalize()} Distribution",
        "xaxis": {"title": "Z"},
        "yaxis": {"title": "Probability"},
        "height": "450",
        "autosize": False,
        "showlegend": False,
    }

    scatter_0 = go.Scatter({"y": random_var.tolist(), "opacity": 0.75, "mode": "markers"})

    scatter_0_layout = {
        "title": f"Scatter Plot - {distribution_name.capitalize()} Distribution",
        "xaxis": {"title": "Index"},
        "yaxis": {"title": "Value"},
        "height": "450",
        "autosize": False,
        "showlegend": False,
    }

    return (
        {"data": [hist_0], "layout": hist_0_layout},
        {"data": [scatter_0], "layout": scatter_0_layout},
    )


@app.callback(Output("compare_plots_menu", "hidden"), [Input("onoff", "value")])
def reveal_compare_plots(value):
    if value == "Off":
        return True
    else:
        return False


@app.callback(Output("compare_plots", "hidden"), [Input("onoff", "value")])
def reveal_compare_plots(value):
    if value == "Off":
        return True
    else:
        return False


# ---------------------------------------------------------------- comparison plots
@app.callback(
    [
        Output("normal_c", "hidden"),
        Output("poisson_c", "hidden"),
        Output("binomial_c", "hidden"),
        Output("nbinomial_c", "hidden"),
        Output("student_c", "hidden"),
        Output("uniform_c", "hidden"),
        Output("beta_c", "hidden"),
        Output("chisq_c", "hidden"),
        Output("exponential_c", "hidden"),
        Output("f_c", "hidden"),
        Output("gamma_c", "hidden"),
        Output("gumbel_c", "hidden"),
        Output("lognormal_c", "hidden"),
        Output("cauchy_c", "hidden"),
        Output("vonmises_c", "hidden"),
        Output("wald_c", "hidden"),
        Output("weibull_c", "hidden"),
    ],
    [Input("distribution_name_c", "value")],
)
def display_parameters_c(value):
    if value == "normal":
        return (
            False,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
        )
    elif value == "poisson":
        return (
            True,
            False,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
        )
    elif value == "binomial":
        return (
            True,
            True,
            False,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
        )
    elif value == "negative binomial":
        return (
            True,
            True,
            True,
            False,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
        )
    elif value == "student T":
        return (
            True,
            True,
            True,
            True,
            False,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
        )
    elif value == "uniform":
        return (
            True,
            True,
            True,
            True,
            True,
            False,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
        )
    elif value == "beta":
        return (
            True,
            True,
            True,
            True,
            True,
            True,
            False,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
        )
    elif value == "chi square":
        return (
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            False,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
        )
    elif value == "exponential":
        return (
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            False,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
        )
    elif value == "f":
        return (
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            False,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
        )
    elif value == "gamma":
        return (
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            False,
            True,
            True,
            True,
            True,
            True,
            True,
        )
    elif value == "gumbel":
        return (
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            False,
            True,
            True,
            True,
            True,
            True,
        )
    elif value == "lognormal":
        return (
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            False,
            True,
            True,
            True,
            True,
        )
    elif value == "cauchy":
        return (
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            False,
            True,
            True,
            True,
        )
    elif value == "vonmises":
        return (
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            False,
            True,
            True,
        )
    elif value == "wald":
        return (
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            False,
            True,
        )
    else:
        return (
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            False,
        )


@app.callback(
    Output("parameter_registry_c", "children"),
    [
        Input("distribution_name_c", "value"),  # args[0]
        Input("N_c", "value"),  # args[1] normal
        Input("mean_c", "value"),  # args[2] normal
        Input("standard_deviation_c", "value"),  # args[3] normal
        Input("lambda_c", "value"),  # args[4] poisson
        Input("n_c", "value"),  # args[5] binomial
        Input("p_c", "value"),  # args[6] binomail
        Input("r_c", "value"),  # args[7] nbinomail
        Input("p_c", "value"),  # args[8] nbinomail
        Input("df_c", "value"),  # args[9] studentt
        Input("alpha_c", "value"),  # args[10] uniform
        Input("beta_c", "value"),  # args[11] uniform
        Input("alpha_c", "value"),  # args[12] beta
        Input("beta_c", "value"),  # args[13] beta
        Input("df_c", "value"),  # args[14] chisq
        Input("lambda_c", "value"),  # args[15] exponential
        Input("df_1_c", "value"),  # args[16] f
        Input("df_2_c", "value"),  # args[17] f
        Input("kappa_c", "value"),  # args[18] gamma
        Input("theta_c", "value"),  # args[19] gamma
        Input("mean_c", "value"),  # args[20] gumbel
        Input("beta_c", "value"),  # args[21] gumbel
        Input("mean_c", "value"),  # args[22] lognormal
        Input("standard_deviation_c", "value"),  # args[23] lognormal
        Input("mean_c", "value"),  # args[24] vonmises
        Input("kappa_c", "value"),  # args[25] vonmises
        Input("mean_c", "value"),  # args[26] wald
        Input("lambda_c", "value"),  # args[27] wald
        Input("lambda_c", "value"),  # args[28] weibull
    ],
)
def registry_updater(*args):
    if args[0] == "normal":
        normal_parameters = normal._make([args[1], args[2], args[3]])
        return normal_parameters
    elif args[0] == "poisson":
        poisson_parameters = poisson._make([args[1], args[4]])
        return poisson_parameters
    elif args[0] == "binomial":
        binomial_parameters = binomial._make([args[1], args[5], args[6]])
        return binomial_parameters
    elif args[0] == "negative binomial":
        nbinomial_parameters = nbinomial._make([args[1], args[7], args[8]])
        return nbinomial_parameters
    elif args[0] == "student T":
        student_parameters = student._make([args[1], args[9]])
        return student_parameters
    elif args[0] == "uniform":
        uniform_parameters = uniform._make([args[1], args[10], args[11]])
        return uniform_parameters
    elif args[0] == "beta":
        beta_parameters = beta._make([args[1], args[12], args[13]])
        return beta_parameters
    elif args[0] == "chi square":
        chisq_parameters = chisq._make([args[1], args[14]])
        return chisq_parameters
    elif args[0] == "exponential":
        exponential_parameters = exponential._make([args[1], args[15]])
        return exponential_parameters
    elif args[0] == "f":
        f_parameters = f._make([args[1], args[16], args[17]])
        return f_parameters
    elif args[0] == "gamma":
        gamma_parameters = gamma._make([args[1], args[18], args[19]])
        return gamma_parameters
    elif args[0] == "gumbel":
        gumbel_parameters = gumbel._make([args[1], args[20], args[21]])
        return gumbel_parameters
    elif args[0] == "lognormal":
        lognormal_parameters = lognormal._make([args[1], args[22], args[23]])
        return lognormal_parameters
    elif args[0] == "cauchy":
        cauchy_parameters = cauchy._make([args[1]])
        return cauchy_parameters
    elif args[0] == "vonmises":
        vonmises_parameters = vonmises._make([args[1], args[24], args[25]])
        return vonmises_parameters
    elif args[0] == "wald":
        wald_parameters = wald._make([args[1], args[26], args[27]])
        return wald_parameters
    elif args[0] == "weibull":
        weibull_parameters = weibull._make([args[1], args[28]])
        return weibull_parameters
    else:
        normal_parameters = normal._make([args[1], args[2], args[3]])
        return normal_parameters


@app.callback(
    [Output("histogram_c", "figure"), Output("scatter_c", "figure")],
    [
        Input("distribution_name_c", "value"),
        Input("parameter_registry_c", "children"),
        Input("bins", "value"),
    ],
)
def update_histogram_c(*args):
    distribution_name, parameters, bins = args

    if distribution_name == "normal":
        random_var = np.random.normal(
            loc=parameters[1], scale=parameters[2], size=parameters[0]
        )
    elif distribution_name == "poisson":
        random_var = np.random.poisson(lam=parameters[1], size=parameters[0])
    elif distribution_name == "binomial":
        random_var = np.random.binomial(
            n=parameters[1], p=parameters[2], size=parameters[0]
        )
    elif distribution_name == "negative binomial":
        random_var = np.random.negative_binomial(
            n=parameters[1], p=parameters[2], size=parameters[0]
        )
    elif distribution_name == "student T":
        random_var = np.random.standard_t(df=parameters[1], size=parameters[0])
    elif distribution_name == "uniform":
        random_var = np.random.uniform(
            low=parameters[1], high=parameters[2], size=parameters[0]
        )
    elif distribution_name == "beta":
        random_var = np.random.beta(
            a=parameters[1], b=parameters[2], size=parameters[0]
        )
    elif distribution_name == "chi square":
        random_var = np.random.chisquare(df=parameters[1], size=parameters[0])
    elif distribution_name == "exponential":
        random_var = np.random.exponential(scale=parameters[1], size=parameters[0])
    elif distribution_name == "f":
        random_var = np.random.f(
            dfnum=parameters[1], dfden=parameters[2], size=parameters[0]
        )
    elif distribution_name == "gamma":
        random_var = np.random.gamma(
            shape=parameters[1], scale=parameters[2], size=parameters[0]
        )
    elif distribution_name == "gumbel":
        random_var = np.random.gumbel(
            loc=parameters[1], scale=parameters[2], size=parameters[0]
        )
    elif distribution_name == "lognormal":
        random_var = np.random.lognormal(
            mean=parameters[1], sigma=parameters[2], size=parameters[0]
        )
    elif distribution_name == "cauchy":
        random_var = np.random.standard_cauchy(size=parameters[0])
    elif distribution_name == "vonmises":
        random_var = np.random.vonmises(
            mu=parameters[1], kappa=parameters[2], size=parameters[0]
        )
    elif distribution_name == "wald":
        random_var = np.random.wald(
            mean=parameters[1], scale=parameters[2], size=parameters[0]
        )
    elif distribution_name == "weibull":
        random_var = np.random.weibull(a=parameters[1], size=parameters[0])
    else:
        random_var = np.random.normal(
            loc=parameters[1], scale=parameters[2], size=parameters[0]
        )

    hist_1 = go.Histogram(
        {
            "x": random_var.tolist(),
            "nbinsx": bins,
            "autobinx": True,
            "marker": {
                "color": "#eb89b5",
                "line": {"width": 1, "color": "MediumPurple",},
            },
            "opacity": 0.75,
        }
    )

    hist_1_layout = {
        "title": f"Probability Density - {distribution_name.capitalize()} Distribution",
        "xaxis": {"title": "Z"},
        "yaxis": {"title": "Probability"},
        "height": "450",
        "autosize": False,
        "showlegend": False,
    }
    scatter_1 = go.Scatter({"y": random_var.tolist(), "opacity": 0.75, "mode": "markers"})
    scatter_1_layout = {
        "title": f"Scatter Plot - {distribution_name.capitalize()} Distribution",
        "xaxis": {"title": "Index"},
        "yaxis": {"title": "Value"},
        "height": "450",
        "autosize": True,
        "showlegend": False,
    }

    return (
        {"data": [hist_1], "layout": hist_1_layout},
        {"data": [scatter_1], "layout": scatter_1_layout},
    )
