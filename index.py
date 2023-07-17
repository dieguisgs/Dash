import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
# see https://community.plot.ly/t/nolayoutexception-on-deployment-of-multi-page-dash-app-example-code/12463/2?u=dcomfort
from app import server
from app import app
from layouts import layout_1, layout_2, layout_3
import callbacks

import pandas as pd
import io
import xlsxwriter
from flask import send_file
import dash_bootstrap_components as dbc

# see https://dash.plot.ly/external-resources to alter header, footer and favicon
app.index_string = ''' 
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>Stark Performance Marketing Report</title>
        {%favicon%}
        {%css%}
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
        </footer>
        <div>Stark Performance Marketing Report</div>
    </body>
</html>
'''

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    dbc.Button('HOME', id='home-link', href='/', external_link=True, className='m-3'),
    dbc.Button('Meteológica', id='page-1-link', href='/page-1', external_link=True, className='m-3'),
    dbc.Button('Predicciones Day-Ahead', id='page-2-link', href='/page-2', external_link=True, className='m-3'),
    dbc.Button('Precios Paises', id='page-3-link', href='/page-3', external_link=True, className='m-3'),
    html.Div(id='page-content')
])

# Update page
# # # # # # # # #

# Leer la imagen y codificarla en base64
with open('gest.png', 'rb') as f:
    image_encoded = base64.b64encode(f.read()).decode('utf-8')

# Crea la cadena de la fuente para html.Img
image_data = f'data:image/png;base64,{image_encoded}'


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])


def display_page(pathname):
    if pathname == '/page-1':
        return layout_1
    elif pathname == '/page-2':
        return layout_2
    elif pathname == '/page-3':
        return layout_3
    else:
        return html.Div([
            html.H3('Bienvenido a la aplicación Dash de Gesternova.'),
            html.P('Haga clic en uno de los botones para ver las visualizaciones.'),
            html.Img(src=image_data, style={'width':'20%', 'display': 'block', 'margin-left': 'auto', 'margin-right': 'auto'})
        ])

# # # # # # # # #
# detail the way that external_css and external_js work and link to alternative method locally hosted
# # # # # # # # #
# external_css = ["https://cdnjs.cloudflare.com/ajax/libs/normalize/7.0.0/normalize.min.css",
#                 "https://cdnjs.cloudflare.com/ajax/libs/skeleton/2.0.4/skeleton.min.css",
#                 "//fonts.googleapis.com/css?family=Raleway:400,300,600",
#                 "https://codepen.io/bcd/pen/KQrXdb.css",
#                 "https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css",
#                 "https://codepen.io/dmcomfort/pen/JzdzEZ.css"]

# for css in external_css:
#     app.css.append_css({"external_url": css})

# external_js = ["https://code.jquery.com/jquery-3.2.1.min.js",
#                "https://codepen.io/bcd/pen/YaXojL.js"]

# for js in external_js:
#     app.scripts.append_script({"external_url": js})

if __name__ == '__main__':
    app.run_server(debug=True)
