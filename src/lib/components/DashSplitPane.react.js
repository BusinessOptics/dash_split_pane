import React, {Component} from 'react';
import PropTypes from 'prop-types';
import stylePropType from 'react-style-proptype';
import SplitPane from 'react-split-pane';

/**
 * Split-Pane React component, can be nested or split vertically or horizontally!
 *
 * Based on react-split-pane (https://github.com/tomkp/react-split-pane)
 */
export default class DashSplitPane extends Component {
    render() {
        const {id, setProps, children, ...props} = this.props;

        return (
            <SplitPane
                id={id}
                onDragFinished={size => setProps({size})}
                {...props}
            >
                {children[0]}
                {children[1]}
            </SplitPane>
        );
    }
}

DashSplitPane.defaultProps = {
    allowResize: true,
    minSize: 50,
    primary: 'first',
    split: 'vertical',
    paneClassName: '',
    pane1ClassName: '',
    pane2ClassName: '',
    persisted_props: ['size'],
    persistence_type: 'local',
};

DashSplitPane.propTypes = {
    /** The children of the split pane. There must be exactly 2 children */
    children: PropTypes.node,

    /**
     * The ID used to identify this component in Dash callbacks.
     */
    id: PropTypes.string,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,

    /** Whether resizing is possible */
    allowResize: PropTypes.bool,

    /** The class name of the primary container */
    className: PropTypes.string,

    /**
     * By dragging 'draggable' surface you can change size of the first pane.
     * The first pane keeps then its size while the second pane is resized by
     * browser window. By default it is the left pane for 'vertical' SplitPane
     * and the top pane for 'horizontal' SplitPane. If you want to keep size of
     * the second pane and let the first pane to shrink or grow by browser
     * window dimensions, set SplitPane prop primary to second. In case of
     * 'horizontal' SplitPane the height of bottom pane remains the same.
     */
    primary: PropTypes.oneOf(['first', 'second']),

    /**
     * The minimum size you can drag the smallest pane to
     */
    minSize: PropTypes.oneOfType([PropTypes.string, PropTypes.number]),

    /**
     * You can limit the maximal size of the 'fixed' pane using the maxSize
     * parameter with a positive value (measured in pixels but state just a
     * number). If you wrap the SplitPane into a container component (yes you
     * can, just remember the container has to have the relative or absolute
     * positioning), then you'll need to limit the movement of the splitter
     * (resizer) at the end of the SplitPane (otherwise it can be dragged
     * outside the SplitPane and you don't catch it never more). For this
     * purpose use the maxSize parameter with value 0. When dragged the
     * splitter/resizer will stop at the border of the SplitPane component and
     * think this you'll be able to pick it again and drag it back then.
     * And more: if you set the maxSize to negative value (e.g. -200), then
     * the splitter stops 200px before the border (in other words it sets the
     * minimal size of the 'resizable' pane in this case). This can be useful
     * also in the full-screen case of use.
     */
    maxSize: PropTypes.oneOfType([PropTypes.string, PropTypes.number]),

    /**
     * The size of the fixed pane. This prop is updated when the pane resized
     * by dragging
     * */
    size: PropTypes.oneOfType([PropTypes.string, PropTypes.number]),

    /**
     * Whether to split horizontally or vertically
     */
    split: PropTypes.oneOf(['vertical', 'horizontal']),

    /** Styling to be applied to the main container. */
    style: stylePropType,

    /** Styling to be applied to the resizer bar */
    resizerStyle: stylePropType,

    /** Styling to be applied to the both panes */
    paneStyle: stylePropType,

    /** Styling to be applied to the first pane, with precedence over `paneStyle` */
    pane1Style: stylePropType,

    /** Styling to be applied to the second pane, with precedence over `paneStyle` */
    pane2Style: stylePropType,

    /** Classname for panes*/
    paneClassName: PropTypes.string,

    /** Classname for primary pane */
    pane1ClassName: PropTypes.string,

    /** Classname for secondary pane */
    pane2ClassName: PropTypes.string,

    /** Classname for resizer */
    resizerClassName: PropTypes.string,

    /**
     * You can use the step prop to only allow resizing in fixed increments.
     */
    step: PropTypes.number,

    /**
     * Used to allow user interactions in this component to be persisted when
     * the component - or the page - is refreshed. If `persisted` is truthy and
     * hasn't changed from its previous value, a `value` that the user has
     * changed while using the app will keep that change, as long as
     * the new `value` also matches what was given originally.
     * Used in conjunction with `persistence_type`.
     */
    persistence: PropTypes.oneOfType([
        PropTypes.bool,
        PropTypes.string,
        PropTypes.number,
    ]),

    /**
     * Properties whose user interactions will persist after refreshing the
     * component or the page. Since only `size` is allowed this prop can
     * normally be ignored.
     */
    persisted_props: PropTypes.arrayOf(PropTypes.oneOf(['size'])),

    /**
     * Where persisted user changes will be stored:
     * memory: only kept in memory, reset on page refresh.
     * local: window.localStorage, data is kept after the browser quit.
     * session: window.sessionStorage, data is cleared once the browser quit.
     */
    persistence_type: PropTypes.oneOf(['local', 'session', 'memory']),
};
