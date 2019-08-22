function course(state = [], action) {
  switch (action.type) {
    case "ADD_COURSE_REQUESTED": {
      const newState = state.concat([
        {
          id: action.id,
          authorId: action.authorId,
          category: action.category,
          slug: action.slug,
          title: action.title
        }
      ]);
      return newState;
    }
    case "DELETE_COURSE_REQUESTED": {
      let newState = [...state];
      let index = -1;
      newState.forEach((course, i) => {
        index = course.id === action.id ? i : index;
      });
      newState.splice(index, 1);
      return newState;
    }
    case "EDIT_COURSE_REQUESTED": {
      let newState = [...state];
      let index = -1;
      newState.forEach((course, i) => {
        index = course.id === action.id ? i : index;
      });
      newState.splice(index, 1, {
        id: action.id,
        authorId: action.authorId,
        category: action.category,
        slug: action.slug,
        title: action.title
      });
      return newState;
    }
    case "COURSES_REQUESTED": {
      return state.length ? state : action.courses;
    }
    default:
      return state;
  }
}

export default course;
