import dash
from dash import dcc, html, Output, Input, State, dash_table
import base64
import io
import pandas as pd

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H2("CSV Upload and Preview"),
    dcc.Upload(
        id='upload-data',
        children=html.Div([
            '📁 Drag and Drop or ',
            html.A('Select a CSV File')
        ]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
        multiple=False
    ),
    html.Div(id='output-table'),
    html.P("Starting to add my own stuff here!")
])

def parse_contents(contents):
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    try:
        df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
    except Exception as e:
        return html.Div(['❌ There was an error processing this file.'])
    
    return dash_table.DataTable(
        data=df.head(10).to_dict('records'),
        columns=[{'name': i, 'id': i} for i in df.columns],
        style_table={'overflowX': 'auto'},
        page_size=10
    )

@app.callback(
    Output('output-table', 'children'),
    Input('upload-data', 'contents'),
    prevent_initial_call=True
)
def update_output(contents):
    if contents:
        return parse_contents(contents)

if __name__ == '__main__':
    app.run(debug=True)
