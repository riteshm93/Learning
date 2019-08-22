import React from "react";
import { connect } from "react-redux";
import { withRouter } from "react-router";
import store from "../store";

class Course extends React.Component {
  constructor(props) {
    super(props);
    const course = this.props.location.state
      ? this.props.location.state.course
      : {
          title: this.props.title || "",
          authorId: this.props.authorId || 1,
          category: this.props.category || ""
        };
    this.state = Object.assign(course);
  }

  handleTitleChange = event => {
    this.setState({ title: event.target.value });
  };

  handleAuthorChange = event => {
    this.setState({ authorId: parseInt(event.target.value) });
  };

  handleCategoryChange = event => {
    this.setState({ category: event.target.value });
  };

  handleSubmit = event => {
    const course = this.state;
    store.dispatch({type: 'SAVE_COURSE', course});
    this.props.history.push("/courses");
    event.preventDefault();
  };

  render() {
    const mode = this.props.location.state ? "Edit" : "Add";
    return (
      <div>
        <h2>{mode} Courses</h2>
        <form onSubmit={this.handleSubmit}>
          <div className="form-group">
            <label htmlFor="titleInput">Title</label>
            <input
              className="form-control"
              id="titleInput"
              type="text"
              value={this.state.title}
              onChange={this.handleTitleChange}
            />
          </div>
          <div className="form-group">
            <label htmlFor="authorInput">Author</label>
            <select
              className="form-control"
              id="authorInput"
              value={this.state.authorId}
              onChange={this.handleAuthorChange}
            >
              {this.props.authors.map((author, i) => {
                return (
                  <option key={i} value={author.id}>
                    {author.name}
                  </option>
                );
              })}
            </select>
          </div>
          <div className="form-group">
            <label htmlFor="categoryInput">Category</label>
            <input
              className="form-control"
              id="categoryInput"
              type="text"
              value={this.state.category}
              onChange={this.handleCategoryChange}
            />
          </div>
          <button type="submit" className="btn btn-primary">
            Save
          </button>
        </form>
      </div>
    );
  }
}

function mapStateToProps(state) {
  return {
    authors: state.authors
  };
}

export default withRouter(
  connect(
    mapStateToProps,
  )(Course)
);
