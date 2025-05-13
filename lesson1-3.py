import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Sample data
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

app = dash.Dash(__name__)

# app.layout = html.Div([
#     html.H1("Hello, Dash!"),
#     html.P("This is your first Dash app.")
# ])

# app.layout = html.Div([
#     html.H2("Try typing something:"),
#     dcc.Input(id='input-box', type='text', placeholder='Enter text here:'),
#     html.Div(id='output')
# ])

# @app.callback(
#     Output('output', 'children'),
#     Input('input-box', 'value')
# )
# def update_output(value):
#     if value:
#         return f'You typed: {value}'
#     return 'Waiting for input...'
app.layout = html.Div([
    html.H2("Fruit Amount by City"),
    dcc.Dropdown(
        id='city-dropdown',
        options=[
            {'label': city, 'value': city} for city in df['City'].unique()
        ],
        value='SF'
    ),
    dcc.Graph(id='fruit-graph')
])

@app.callback(
    Output('fruit-graph', 'figure'),
    Input('city-dropdown', 'value')
)
def update_figure(selected_city):
    filtered_df = df[df['City'] == selected_city]
    fig = px.bar(filtered_df, x='Fruit', y='Amount', title=f'Fruit in {selected_city}')
    return fig


if __name__ == "__main__":
    app.run(debug=True)
