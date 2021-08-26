# Imports from 3rd party libraries
import dash
from dash_core_components.Dropdown import Dropdown
from dash_core_components.Markdown import Markdown
from plotly.express import colors
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
from joblib import load
import numpy as np

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown('## Predictions:'),
        dcc.Markdown('#### Kickstarter Name'),
        dcc.Input(
            id = 'Name',
            placeholder= 'Enter name here...',
            type= 'text',
            value = '',
            className='mb-5',
            ),
        
    
        dcc.Markdown('#### Description'),
        dcc.Textarea(
            id = 'Desc',
            placeholder= 'Enter Description Here...',
            value = 'Enter Full Description Here',
            style={'width':'100%'},
            className='mb-5',    
        ),
        dcc.Markdown('''
                     #### Keywords
                     
                     Keywords must be entered with a dash in between with NO spaces
                     '''),
        dcc.Input(
            id= 'Keywords',
            placeholder= 'Enter-keywords-as-shown...',
            type= 'text',
            value = '',
            className= 'mb-5',
        ),
        
        dcc.Markdown('''
                     #### Backer Count
                     
                     Will more than 25 people donate to your campaign?
                     '''),
        dcc.Dropdown(
            id = 'Backers_count',
            options =[
                {'label' : 'Yes', 'value' : '1'},
                {'label' : 'No', 'value': '0'}
            ],
            value='No',
            className='mb-5',
            ),
    ],
    md=4,
)

column2 = dbc.Col(
    [
        dcc.Markdown('##  ', className='mb-5'),
        dcc.Markdown('''
                     #### Currency
                     
                     Three letter acronym for origin of currency
                     '''),
        dcc.Input(
            id = 'Currency',
            type = 'text',
            placeholder='USD',
            className='mb-5',
        ),
        dcc.Markdown('#### Country'),
        dcc.Input(
            id = 'Country',
            type = 'text',
            placeholder = 'US',
            className = 'mb-5',
        ),
        dcc.Markdown('''
                     #### Duration
                     
                     Is your campaign going to last 31 days or less?
                     '''),
        dcc.Dropdown(
            id = 'Duration',
            options = [
                {"label": "Yes", "value" : "1"},
                {'label':'No', 'value':'0'}   
            ],
            className='mb-5'
        ),
            
        dcc.Markdown('''
                     #### Goal
                     '''),
        dcc.Input(
            id = 'Goal',
            type = 'text',
            placeholder= '0',
            className= 'mb-5'
        ),
        dbc.Button('Predict My Success!', color='primary')
    ]
)

column3 = dbc.Col(
    [
    dcc.Graph(id='pie-chart')
    ]
)

layout = dbc.Row([column1, column2, column3])

