function author(state = [], action) {
  switch (action.type) {
    case "AUTHORS_REQUESTED": {
      return state.length ? state : action.authors;
    }
    default:
      return state;
  }
}

export default author;
