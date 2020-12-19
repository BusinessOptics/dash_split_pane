# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DashSplitPane(Component):
    """A DashSplitPane component.
Split-Pane Dash component, can be nested or split vertically or horizontally!

Based on react-split-pane (https://github.com/tomkp/react-split-pane)

Keyword arguments:
- children (a list of or a singular dash component, string or number; optional): The children of the split pane. There must be exactly 2 children
- id (string; optional): The ID used to identify this component in Dash callbacks.
- allowResize (boolean; default True): Whether resizing is possible
- className (string; optional): The class name of the primary container
- primary (a value equal to: 'first', 'second'; default 'first'): By dragging 'draggable' surface you can change size of the first pane.
The first pane keeps then its size while the second pane is resized by
browser window. By default it is the left pane for 'vertical' SplitPane
and the top pane for 'horizontal' SplitPane. If you want to keep size of
the second pane and let the first pane to shrink or grow by browser
window dimensions, set SplitPane prop primary to second. In case of
'horizontal' SplitPane the height of bottom pane remains the same.
- minSize (string | number; default 50): The minimum size you can drag the smallest pane to
- maxSize (string | number; optional): You can limit the maximal size of the 'fixed' pane using the maxSize
parameter with a positive value (measured in pixels but state just a
number). If you wrap the SplitPane into a container component (yes you
can, just remember the container has to have the relative or absolute
positioning), then you'll need to limit the movement of the splitter
(resizer) at the end of the SplitPane (otherwise it can be dragged
outside the SplitPane and you don't catch it never more). For this
purpose use the maxSize parameter with value 0. When dragged the
splitter/resizer will stop at the border of the SplitPane component and
think this you'll be able to pick it again and drag it back then.
And more: if you set the maxSize to negative value (e.g. -200), then
the splitter stops 200px before the border (in other words it sets the
minimal size of the 'resizable' pane in this case). This can be useful
also in the full-screen case of use.
- size (string | number; optional): The size of the fixed pane. This prop is updated when the pane resized
by dragging
- split (a value equal to: 'vertical', 'horizontal'; default 'vertical'): Whether to split horizontally or vertically
- style (optional): Styling to be applied to the main container.
- resizerStyle (optional): Styling to be applied to the resizer bar
- paneStyle (optional): Styling to be applied to the both panes
- pane1Style (optional): Styling to be applied to the first pane, with precedence over `paneStyle`
- pane2Style (optional): Styling to be applied to the second pane, with precedence over `paneStyle`
- paneClassName (string; default ''): Classname for panes
- pane1ClassName (string; default ''): Classname for primary pane
- pane2ClassName (string; default ''): Classname for secondary pane
- resizerClassName (string; optional): Classname for resizer
- step (number; optional): You can use the step prop to only allow resizing in fixed increments.
- persistence (boolean | string | number; optional): Used to allow user interactions in this component to be persisted when
the component - or the page - is refreshed. If `persisted` is truthy and
hasn't changed from its previous value, a `value` that the user has
changed while using the app will keep that change, as long as
the new `value` also matches what was given originally.
Used in conjunction with `persistence_type`.
- persisted_props (list of a value equal to: 'size's; default ['size']): Properties whose user interactions will persist after refreshing the
component or the page. Since only `size` is allowed this prop can
normally be ignored.
- persistence_type (a value equal to: 'local', 'session', 'memory'; default 'local'): Where persisted user changes will be stored:
memory: only kept in memory, reset on page refresh.
local: window.localStorage, data is kept after the browser quit.
session: window.sessionStorage, data is cleared once the browser quit."""
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, allowResize=Component.UNDEFINED, className=Component.UNDEFINED, primary=Component.UNDEFINED, minSize=Component.UNDEFINED, maxSize=Component.UNDEFINED, size=Component.UNDEFINED, split=Component.UNDEFINED, style=Component.UNDEFINED, resizerStyle=Component.UNDEFINED, paneStyle=Component.UNDEFINED, pane1Style=Component.UNDEFINED, pane2Style=Component.UNDEFINED, paneClassName=Component.UNDEFINED, pane1ClassName=Component.UNDEFINED, pane2ClassName=Component.UNDEFINED, resizerClassName=Component.UNDEFINED, step=Component.UNDEFINED, persistence=Component.UNDEFINED, persisted_props=Component.UNDEFINED, persistence_type=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'allowResize', 'className', 'primary', 'minSize', 'maxSize', 'size', 'split', 'style', 'resizerStyle', 'paneStyle', 'pane1Style', 'pane2Style', 'paneClassName', 'pane1ClassName', 'pane2ClassName', 'resizerClassName', 'step', 'persistence', 'persisted_props', 'persistence_type']
        self._type = 'DashSplitPane'
        self._namespace = 'dash_split_pane'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'allowResize', 'className', 'primary', 'minSize', 'maxSize', 'size', 'split', 'style', 'resizerStyle', 'paneStyle', 'pane1Style', 'pane2Style', 'paneClassName', 'pane1ClassName', 'pane2ClassName', 'resizerClassName', 'step', 'persistence', 'persisted_props', 'persistence_type']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(DashSplitPane, self).__init__(children=children, **args)
