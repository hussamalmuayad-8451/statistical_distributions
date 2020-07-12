from copy import copy
from dash.dependencies import Input, Output, State
from collections import defaultdict
import plotly.graph_objs as go
import numpy as np
from layouts.layout import page_1
from app import app

from collections import namedtuple

normal  = namedtuple("normal","N mean standard_deviation")
poisson = namedtuple("poisson","N mean")
binomial= namedtuple("binomial","N n p")  

@app.callback(
    [Output("normal","hidden"),
     Output("poisson","hidden"),
     Output("binomial","hidden")],
     [Input("distribution_name","value")]
)
def display_parameters(value):
    if value == "normal":
        return (False, True, True)
    elif value == "poisson":
        return (True, False, True)
    elif value == "binomial":
        return (True, True, False)
    else:
        return (False, True, True)

@app.callback(
    Output("parameter_registry","children"),    
    [Input("distribution_name","value"),        #args[0]
     Input("N","value"),                        #args[1]
     Input("mean","value"),                     #args[2]
     Input("standard_deviation","value"),       #args[3]
     Input("lambda","value"),                   #args[4]
     Input("n","value"),                        #args[5]
     Input("p","value")]                        #args[6]
)   
def registry_updater(*args):
    if args[0]=="normal":
        normal_parameters=normal._make([args[1], args[2], args[3]])
        return normal_parameters
    elif args[0]=="poisson":
        poisson_parameters=poisson._make([args[1], args[4]]) 
        return poisson_parameters
    elif args[0]=="binomial":
        binomial_parameters=binomial._make([args[1], args[5], args[6]])
        return binomial_parameters
    else:
        normal_parameters=normal._make([args[1], args[2], args[3]])
        return normal_parameters



@app.callback(
            Output("histogram","figure"),
            [Input("distribution_name","value"),
             Input("parameter_registry","children"),
             Input("bins","value")]
            )
def update_histogram(*args):
    distribution_name, parameters, bins = args
    #print(distribution_name, parameters)
    if distribution_name=="normal":
        random_var = np.random.normal(loc=parameters[1], scale=parameters[2], size=parameters[0])
    elif distribution_name=="poisson":
        random_var = np.random.poisson(lam=parameters[1], size=parameters[0])
    elif distribution_name=="binomial":
        random_var = np.random.binomial(n=parameters[1], p=parameters[2], size=parameters[0])
    else:
        random_var = np.random.normal(loc=parameters[1], scale=parameters[2], size=parameters[0]) 

    
    histogram = go.Histogram(
        {
            "x": random_var,
            "nbinsx": bins,
            "histnorm": "percent",
            "xbins": {"start": 0, "size": 10},
            "autobinx": True,
            "marker": {"color": "#ff8533"},  # EB89B5
            "opacity": 0.75,
        })
    my_layout = {
        "title": "histogram normal distribution",
        "xaxis": {"title": "Z"},
        "yaxis": {"title": "Probability"},
        "autosize": "False",
        # "height"    : "600",
        # "width"     : "1200",
        "showlegend": False
    }

    return {"data": [histogram], "layout": my_layout}


@app.callback(
            Output("scatter","figure"),
            [Input("distribution_name","value"),
             Input("parameter_registry","children")]
            )
def update_scatter(*args):
    distribution_name, parameters = args
    if distribution_name=="normal":
        random_var = np.random.normal(loc=parameters[1], scale=parameters[2], size=parameters[0])
    elif distribution_name=="poisson":
        random_var = np.random.poisson(lam=parameters[1], size=parameters[0])
    elif distribution_name=="binomial":
        random_var = np.random.binomial(n=parameters[1], p=parameters[2], size=parameters[0])
    else:
        random_var = np.random.normal(loc=parameters[1], scale=parameters[2], size=parameters[0]) 
    
    scatter = go.Scatter(
        {
            "y": random_var,
            "opacity": 0.75,
            "mode":"markers"
        })
    my_layout = {
        "title": "distribution scatter plot",
        "xaxis": {"title": "probability"},
        "yaxis": {"title": "Percent"},
        "autosize": "False",
        "showlegend": False
    }

    return {"data": [scatter], "layout": my_layout}


#@app.callback(
#            Output("N_display","children"),
#            [Input("N","value")]
#            )
#def n_display(value):
#    return str(value)


@app.callback(
            Output("compare_plots","hidden"),
            [Input("onoff","value")]
            )
def reveal_compare_plots(value):
    if value=="Off":
        return True
    else:
        return False



#numpy.random.randint  uniform
#numpy.random.binomial
#numpy.random.beta(a, b, size=None)