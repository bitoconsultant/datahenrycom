import dash
from dash import html

app = dash.Dash(__name__)

# app layout
app.layout = html.Div([
    html.H1('Hello, DataHenry.com.co'),
    html.H2('Web Site Under construction')
])

# run app
if __name__ == '__main__':
    app.run_server(debug=True)