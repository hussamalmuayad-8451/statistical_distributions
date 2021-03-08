import dash_core_components as dcc
import dash_html_components as html
import dash_table as dt
import plotly.figure_factory as ff
from collections import namedtuple
from layouts.layout_elements import (
    left_menu,
    main_plots,
    compare_plots,
    distribution_parameters,
    distribution_parameters_c,
)


##----------------------------------------------------------------
## main layout
##----------------------------------------------------------------

page_1 = html.Div(
    [
        html.Header(
            [html.H1(children="Statistical Distributions")], className="header",
        ),
        html.Div(
            [
                html.Div(left_menu, className="left_menu"),

                html.Div(main_plots, className="main_plots"),
                html.Div(
                    id="compare_plots",
                    hidden=True,
                    children=compare_plots,
                    className="compare_plots",
                ),
            ],
        ),
        html.Footer(
            [html.Div(children="created by"), html.Div(children="Hussam Almuayad")],
            className="page1",
        ),
    ]
)
