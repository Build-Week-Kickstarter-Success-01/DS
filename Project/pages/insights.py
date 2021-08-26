# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# 1 column layout
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## User Feedback
            
            Please let us know how you enjoyed using our app! 
            We want to provide the best experience we can for our users!


            """
        ),
        dcc.Textarea(
            id = 'User-Input',
            placeholder= 'Let us know how we did!',
            style = {'width':'100%'},
            className='mb-5'
        ),
        dbc.Button('Submit', color='primary')
    ],
)

layout = dbc.Row([column1])