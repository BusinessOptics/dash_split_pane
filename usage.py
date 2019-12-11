import dash_split_pane
import dash
from dash.dependencies import Input, Output
import dash_html_components as html

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        dash_split_pane.DashSplitPane(
            children=[html.Div(id="left-pane"), html.Div("RIGHT PANE")],
            id="splitter",
            split="vertical",
            size=50,
            persistence=True,
        ),
    ]
)


@app.callback(Output("left-pane", "children"), [Input("splitter", "size")])
def show_size(size):
    return size


if __name__ == "__main__":
    app.run_server(debug=True)
