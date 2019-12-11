/* eslint no-magic-numbers: 0 */
import React, {Component} from 'react';

import {DashSplitPane} from '../lib';

class App extends Component {
    constructor() {
        super();
        this.state = {};
        this.setProps = this.setProps.bind(this);
    }

    setProps(newProps) {
        this.setState(newProps);
    }

    render() {
        return (
            <div>
                <DashSplitPane
                    setProps={this.setProps}
                    size={400}
                    {...this.state}
                >
                    <div>LEFT</div>
                    <div>RIGHT</div>
                </DashSplitPane>
            </div>
        );
    }
}

export default App;
