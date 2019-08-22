import React from "react";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";

import About from "./About";
import Course from "./Course";
import Courses from "./Courses";
import Headers from "./Headers";
import Home from "./Home";

class App extends React.Component {
  render() {
    return (
      <Router>
        <div>
          <Headers />
          <Switch>
            <Route exact path="/" component={Home} />
            <Route path="/about" component={About} />
            <Route path="/course" component={Course} />
            <Route path="/courses" component={Courses} />
            <Route component={NoMatch} />
          </Switch>
        </div>
      </Router>
    );
  }
}

function NoMatch() {
  return <h2>Ooops! Page not found.</h2>;
}

export default App;
