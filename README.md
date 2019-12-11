# Dash Split pane

A Dash Split-Pane component, can be nested or split vertically or horizontally!

This is based on React Split Pane: [https://github.com/tomkp/react-split-pane](https://github.com/tomkp/react-split-pane)

## Installation

Install via pip

```
pip install dash-split-pane
```

## Usage

```python
import dash_split_pane

dash_split_pane.DashSplitPane(
    children=[html.Div("LEFT PANE"), html.Div("RIGHT PANE")],
    id="splitter",
    split="vertical",
    size=50,
)
```

All the props from [react-split-pane](https://github.com/tomkp/react-split-pane) are exposed, except for `defaultSize` (only `size` needs to be used).

The `size` property will be updated to dash when a drag is complete.

For more information see [react-split-pane](https://github.com/tomkp/react-split-pane)
