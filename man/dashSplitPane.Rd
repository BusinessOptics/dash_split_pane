% Auto-generated: do not edit by hand
\name{dashSplitPane}

\alias{dashSplitPane}

\title{DashSplitPane component}

\description{
Split-Pane Dash component, can be nested or split vertically or horizontally!  Based on react-split-pane (https://github.com/tomkp/react-split-pane)
}

\usage{
dashSplitPane(children=NULL, id=NULL, allowResize=NULL, className=NULL, primary=NULL,
minSize=NULL, maxSize=NULL, size=NULL, split=NULL, style=NULL,
resizerStyle=NULL, paneStyle=NULL, pane1Style=NULL, pane2Style=NULL,
paneClassName=NULL, pane1ClassName=NULL, pane2ClassName=NULL,
resizerClassName=NULL, step=NULL, persistence=NULL, persisted_props=NULL,
persistence_type=NULL)
}

\arguments{
\item{children}{A list of or a singular dash component, string or number. The children of the split pane. There must be exactly 2 children}

\item{id}{Character. The ID used to identify this component in Dash callbacks.}

\item{allowResize}{Logical. Whether resizing is possible}

\item{className}{Character. The class name of the primary container}

\item{primary}{A value equal to: 'first', 'second'. By dragging 'draggable' surface you can change size of the first pane.
The first pane keeps then its size while the second pane is resized by
browser window. By default it is the left pane for 'vertical' SplitPane
and the top pane for 'horizontal' SplitPane. If you want to keep size of
the second pane and let the first pane to shrink or grow by browser
window dimensions, set SplitPane prop primary to second. In case of
'horizontal' SplitPane the height of bottom pane remains the same.}

\item{minSize}{Character | numeric. The minimum size you can drag the smallest pane to}

\item{maxSize}{Character | numeric. You can limit the maximal size of the 'fixed' pane using the maxSize
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
also in the full-screen case of use.}

\item{size}{Character | numeric. The size of the fixed pane. This prop is updated when the pane resized
by dragging}

\item{split}{A value equal to: 'vertical', 'horizontal'. Whether to split horizontally or vertically}

\item{style}{Styling to be applied to the main container.}

\item{resizerStyle}{Styling to be applied to the resizer bar}

\item{paneStyle}{Styling to be applied to the both panes}

\item{pane1Style}{Styling to be applied to the first pane, with precedence over `paneStyle`}

\item{pane2Style}{Styling to be applied to the second pane, with precedence over `paneStyle`}

\item{paneClassName}{Character. Classname for panes}

\item{pane1ClassName}{Character. Classname for primary pane}

\item{pane2ClassName}{Character. Classname for secondary pane}

\item{resizerClassName}{Character. Classname for resizer}

\item{step}{Numeric. You can use the step prop to only allow resizing in fixed increments.}

\item{persistence}{Logical | character | numeric. Used to allow user interactions in this component to be persisted when
the component - or the page - is refreshed. If `persisted` is truthy and
hasn't changed from its previous value, a `value` that the user has
changed while using the app will keep that change, as long as
the new `value` also matches what was given originally.
Used in conjunction with `persistence_type`.}

\item{persisted_props}{List of a value equal to: 'size's. Properties whose user interactions will persist after refreshing the
component or the page. Since only `size` is allowed this prop can
normally be ignored.}

\item{persistence_type}{A value equal to: 'local', 'session', 'memory'. Where persisted user changes will be stored:
memory: only kept in memory, reset on page refresh.
local: window.localStorage, data is kept after the browser quit.
session: window.sessionStorage, data is cleared once the browser quit.}
}
