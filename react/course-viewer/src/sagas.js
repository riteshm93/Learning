import { deleteCourse, getCourses, saveCourse } from "./api/courseApi";
import { getAuthors } from "./api/authorApi";
import { put, takeEvery, all } from 'redux-saga/effects'

function* saveCourseData(payload) {
  const course = yield saveCourse(payload.course);
  return yield put({ type: payload.course.id ? "EDIT_COURSE_REQUESTED" : "ADD_COURSE_REQUESTED", course });
}

function* watchSaveCourse() {
  yield takeEvery('SAVE_COURSE', saveCourseData);
};

function* deleteCourseById(payload) {
  yield deleteCourse(payload.id);
  return yield put({ type: "DELETE_COURSE_REQUESTED", payload });
}

function* watchDeleteCourseById() {
  yield takeEvery('DELETE_COURSE', deleteCourseById);
};

function* initCourses() {
  const courses = yield getCourses();
  return yield put({ type: "COURSES_REQUESTED", courses: courses });
}

function* initAuthors() {
  const authors = yield getAuthors();
  return yield put({ type: "AUTHORS_REQUESTED", authors: authors });
}

export default function* rootSaga() {
  yield all([
    initAuthors(),
    initCourses(),
    watchSaveCourse(),
    watchDeleteCourseById()
  ])
}