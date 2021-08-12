import dash
from dash.dependencies import Output, Input
import dash_core_components as dcc
import dash_html_components as html
import plotly
import random
import plotly.graph_objs as go
from collections import deque
import numpy as np


X = deque(maxlen=20)
X.append(1)
Y = deque(maxlen=20)
Y.append(1)

X1 = deque(maxlen=20)
X1.append(1)
Y1 = deque(maxlen=20)
Y1.append(1)


app = dash.Dash(__name__)

# LAYOUT OF THE WEB PAGE
app.layout = html.Div(
    [
    	html.Div([html.P('Nice plot')]),
        dcc.Graph(id='live-graph', animate=True),
        dcc.Interval(
            id='graph-update',
            interval=1000,
            n_intervals = 0
        ),
        html.Div([html.P('Another nice plot')]),
        dcc.Graph(id='live-graph1', animate=True),
        dcc.Interval(
            id='graph-update1',
            interval=1000,
            n_intervals = 0
        )
    ]
)


@app.callback(Output('live-graph', 'figure'),
        [Input('graph-update', 'n_intervals')])
def update_graph_scatter(n):
    X.append(X[-1]+1)
    Y.append(Y[-1]+Y[-1]*random.uniform(-0.1,0.1))

    data = plotly.graph_objs.Scatter(
            x=list(X),
            y=list(Y),
            name='Scatter',
            mode= 'lines+markers'
            )
    

    return {'data': [data],'layout' : go.Layout(height=300, xaxis=dict(range=[min(X),max(X)]),                                             yaxis=dict(range=[min(Y),max(Y)]),)}

@app.callback(Output('live-graph1', 'figure'),
        [Input('graph-update', 'n_intervals')])
def update_graph_scatter1(n):
    X1.append(X1[-1]+1)
    Y1.append(np.sin(X1[-1]))

    data = plotly.graph_objs.Scatter(
            x=list(X1),
            y=list(Y1),
            name='Scatter',
            mode='lines+markers',
            line={'color': 'rgba(255, 0, 0, 100)'})

    return {'data': [data],'layout' : go.Layout(height=300,xaxis=dict(range=[min(X1),max(X1)]),                                             yaxis=dict(range=[min(Y1),max(Y1)]),)}



if __name__ == '__main__':
    app.run_server(debug=True)
