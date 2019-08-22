import React from "react";
import { NavLink } from "react-router-dom";

class Headers extends React.PureComponent {
  render() {
    return (
      <ul className="nav">
        <li className="nav-item">
          <NavLink exact to="/" activeClassName="selected-nav-item">
            Home
          </NavLink>
        </li>
        <li className="nav-item">
          <NavLink to="/courses" activeClassName="selected-nav-item">
            Courses
          </NavLink>
        </li>
        <li className="nav-item">
          <NavLink to="/about" activeClassName="selected-nav-item">
            About
          </NavLink>
        </li>
      </ul>
    );
  }
}

export default Headers;
