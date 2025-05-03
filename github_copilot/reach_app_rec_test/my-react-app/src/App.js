import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import AppComponent from './components/App';

const App = () => {
    return (
        <Router>
            <Switch>
                <Route path="/" component={AppComponent} />
            </Switch>
        </Router>
    );
};

export default App;