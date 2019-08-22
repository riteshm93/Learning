import React from "react";
import { connect } from "react-redux";
import { Link } from "react-router-dom";
import store from "../store";

class Courses extends React.Component {
  renderAuthor(authorId) {
    let authorName = "";
    this.props.authors.forEach(author => {
      if (author.id === authorId) authorName = author.name;
    });
    return authorName;
  }

  deleteCourse = event => {
    store.dispatch({type: 'DELETE_COURSE', id: parseInt(event.target.id)});
  };

  renderCourse(course) {
    return (
      <tr key={course.id}>
        <td>
          <button className="btn btn-light">Watch</button>
        </td>
        <td>
          <Link
            to={{
              pathname: "/course/" + course.slug,
              state: {
                course: course
              }
            }}
          >
            {course.title}
          </Link>
        </td>
        <td>{this.renderAuthor(course.authorId)}</td>
        <td>{course.category}</td>
        <td>
          <button
            className="btn btn-outline-danger"
            id={course.id}
            onClick={this.deleteCourse}
          >
            Delete
          </button>
        </td>
      </tr>
    );
  }

  render() {
    const courses = this.props.courses;
    return (
      <div>
        <h2>Courses</h2>
        <Link to="/course/">
          <button className="btn btn-primary my-3">Add Course</button>
        </Link>
        <table className="table">
          <thead>
            <tr>
              <th />
              <th>Title</th>
              <th>Author</th>
              <th>Category</th>
              <th />
            </tr>
          </thead>
          <tbody>
            {courses.map((course, i) => {
              return this.renderCourse(course);
            })}
          </tbody>
        </table>
      </div>
    );
  }
}

function mapStateToProps(state) {
  return {
    courses: state.courses,
    authors: state.authors
  };
}

export default connect(
  mapStateToProps,
)(Courses);
