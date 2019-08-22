import { deleteCourse, getCourses, saveCourse } from "../api/courseApi";
import { getAuthors } from "../api/authorApi";
import store from "../store";

export const addCourse = payload => dispatch => {
  saveCourse(payload).then(result => {
    store.dispatch(
      Object.assign({ type: payload.id ? "EDIT_COURSE" : "ADD_COURSE" }, result)
    );
  });
};

export const deleteCourseById = payload => dispatch => {
  deleteCourse(payload.id).then(result => {
    store.dispatch(Object.assign({ type: "DELETE_COURSE" }, payload));
  });
};

export const initCourses = () => dispatch => {
  getCourses().then(result => {
    store.dispatch({ type: "INIT_COURSES", courses: result });
  });
};

export const initAuthors = () => dispatch => {
  getAuthors().then(result => {
    store.dispatch({ type: "INIT_AUTHORS", authors: result });
  });
};
