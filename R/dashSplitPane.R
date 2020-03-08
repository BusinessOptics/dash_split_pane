# AUTO GENERATED FILE - DO NOT EDIT

dashSplitPane <- function(children=NULL, id=NULL, allowResize=NULL, className=NULL, primary=NULL, minSize=NULL, maxSize=NULL, size=NULL, split=NULL, style=NULL, resizerStyle=NULL, paneStyle=NULL, pane1Style=NULL, pane2Style=NULL, paneClassName=NULL, pane1ClassName=NULL, pane2ClassName=NULL, resizerClassName=NULL, step=NULL, persistence=NULL, persisted_props=NULL, persistence_type=NULL) {
    
    props <- list(children=children, id=id, allowResize=allowResize, className=className, primary=primary, minSize=minSize, maxSize=maxSize, size=size, split=split, style=style, resizerStyle=resizerStyle, paneStyle=paneStyle, pane1Style=pane1Style, pane2Style=pane2Style, paneClassName=paneClassName, pane1ClassName=pane1ClassName, pane2ClassName=pane2ClassName, resizerClassName=resizerClassName, step=step, persistence=persistence, persisted_props=persisted_props, persistence_type=persistence_type)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'DashSplitPane',
        namespace = 'dash_split_pane',
        propNames = c('children', 'id', 'allowResize', 'className', 'primary', 'minSize', 'maxSize', 'size', 'split', 'style', 'resizerStyle', 'paneStyle', 'pane1Style', 'pane2Style', 'paneClassName', 'pane1ClassName', 'pane2ClassName', 'resizerClassName', 'step', 'persistence', 'persisted_props', 'persistence_type'),
        package = 'dashSplitPane'
        )

    structure(component, class = c('dash_component', 'list'))
}
