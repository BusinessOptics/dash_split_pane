# AUTO GENERATED FILE - DO NOT EDIT

dashSplitPane <- function(children=NULL, id=NULL, allowResize=NULL, className=NULL, primary=NULL, minSize=NULL, maxSize=NULL, defaultSize=NULL, size=NULL, split=NULL, style=NULL, resizerStyle=NULL, paneClassName=NULL, pane1ClassName=NULL, pane2ClassName=NULL, paneStyle=NULL, pane1Style=NULL, pane2Style=NULL, resizerClassName=NULL, step=NULL) {
    
    props <- list(children=children, id=id, allowResize=allowResize, className=className, primary=primary, minSize=minSize, maxSize=maxSize, defaultSize=defaultSize, size=size, split=split, style=style, resizerStyle=resizerStyle, paneClassName=paneClassName, pane1ClassName=pane1ClassName, pane2ClassName=pane2ClassName, paneStyle=paneStyle, pane1Style=pane1Style, pane2Style=pane2Style, resizerClassName=resizerClassName, step=step)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'DashSplitPane',
        namespace = 'dash_split_pane',
        propNames = c('children', 'id', 'allowResize', 'className', 'primary', 'minSize', 'maxSize', 'defaultSize', 'size', 'split', 'style', 'resizerStyle', 'paneClassName', 'pane1ClassName', 'pane2ClassName', 'paneStyle', 'pane1Style', 'pane2Style', 'resizerClassName', 'step'),
        package = 'dashSplitPane'
        )

    structure(component, class = c('dash_component', 'list'))
}
