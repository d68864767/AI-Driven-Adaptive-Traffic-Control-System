```python
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from system_integration import integrate_system

# Load the model and data
model, data = integrate_system()

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
    html.H1("AI-Driven Adaptive Traffic Control System"),
    html.Div([
        html.Div([
            dcc.Graph(id='live-update-graph'),
            dcc.Interval(
                id='interval-component',
                interval=1*1000,  # in milliseconds
                n_intervals=0
            )
        ])
    ]),
    html.Div(id='live-update-text')
])

# Define callback to update graph
@app.callback(Output('live-update-graph', 'figure'),
              [Input('interval-component', 'n_intervals')])
def update_graph_live(n):
    # Create the graph with subplots
    fig = make_subplots(rows=2, cols=1, vertical_spacing=0.2)

    fig.add_trace(
        go.Scatter(
            x=list(range(len(data))),
            y=data['congestion'],
            name="Congestion",
            line=dict(color='firebrick', width=2)
        )
    )

    fig.update_layout(height=700, width=800, title_text="Real-Time Traffic Congestion")
    return fig

# Define callback to update metrics
@app.callback(Output('live-update-text', 'children'),
              [Input('interval-component', 'n_intervals')])
def update_metrics(n):
    style = {'padding': '5px', 'fontSize': '16px'}
    return [
        html.Span('Congestion Level: {0:.2f}'.format(data['congestion'].iloc[-1]), style=style),
    ]

if __name__ == '__main__':
    app.run_server(debug=True)
```

