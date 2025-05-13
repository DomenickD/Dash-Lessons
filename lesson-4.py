import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Sample Data
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H2("Fruit Sales Dashboard"),
    html.Div([
        html.Div([
            html.Label("Select City"),
            dcc.Dropdown(
                id='city-dropdown',
                options=[{'label': city, 'value': city} for city in df['City'].unique()],
                value='SF'
            )
        ], style={'width': '48%', 'display': 'inline-block'}),

        html.Div([
            html.Label("Select Fruit"),
            dcc.Dropdown(
                id='fruit-dropdown',
                options=[{'label': fruit, 'value': fruit} for fruit in df['Fruit'].unique()],
                value='Apples'
            )
        ], style={'width': '48%', 'display': 'inline-block', 'float': 'right'})
    ]),
    dcc.Graph(id='filtered-graph')
])

@app.callback(
    Output('filtered-graph', 'figure'),
    Input('city-dropdown', 'value'),
    Input('fruit-dropdown', 'value')
)
def update_graph(city, fruit):
    filtered_df = df[(df['City'] == city) & (df['Fruit'] == fruit)]
    fig = px.bar(filtered_df, x='Fruit', y='Amount', title=f'{fruit} in {city}')
    return fig

if __name__ == '__main__':
    app.run(debug=True)
