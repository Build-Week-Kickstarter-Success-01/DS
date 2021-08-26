# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Our Value Proposition

            We want to help others make informed business decisions to help shape the future of the self-starter business. We will do this through providing
            accurate modeling for the most accurate predictions and creating a user interface that is visually appealing and meets our clients needs.

            ✅ Kickstart your Success is an app that focuses on providing you an accurate prediction to your kickstarter's success or failure.

            ❌ Kickstart your Success was designed to give our users a vision of the future and arm them with knowledge for their business success!

            """
        ),
        dcc.Link(dbc.Button('Your Call To Action', color='primary'), href='/predictions')
    ],
    md=4,
)

column2 = dbc.Col(
    [
        html.Img(src= app.get_asset_url('kickstarter.png'))
        #dcc.Graph(figure=fig),
    ]
)

layout = dbc.Row([column1, column2])