import React from "react";
import { Link } from "react-router-dom";

class Home extends React.PureComponent {
  render() {
    return (
      <div className="bg-light p-4">
        <h2>Pluralsight Administration</h2>
        <p>React, Redux, React Router for ultra-responsive web apps.</p>
        <Link to="/About">
          <button className="btn btn-primary">Learn more</button>
        </Link>
      </div>
    );
  }
}

export default Home;
