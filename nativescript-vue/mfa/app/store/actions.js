export const initTables = ({ commit }) => {
  return new Promise((resolve, reject) => {
    commit("initTables");
    resolve();
  }).catch(error => {
    console.error(`Error initializing app : ${error}.`);
    reject(error);
  });
};

export const initTable = ({ commit }, table) => {
  return new Promise((resolve, reject) => {
    commit("initTable", table);
    resolve();
  }).catch(error => {
    console.error(`Error initializing table : ${error}.`);
    reject(error);
  });
};

export const deleteTable = ({ commit }, table) => {
  return new Promise((resolve, reject) => {
    commit("deleteTable", table);
    resolve();
  }).catch(error => {
    console.error(`Error deleting table : ${error}.`);
    reject(error);
  });
};

export const setSelectTable = ({ commit }, table) => {
  return new Promise((resolve, reject) => {
    commit("setSelectTable", table);
    resolve();
  }).catch(error => {
    console.error(`Error selecting table : ${error}.`);
    reject(error);
  });
};

export const setItemsSetupDone = ({ commit }, value) => {
  return new Promise((resolve, reject) => {
    commit("setItemsSetupDone", value);
    resolve();
  }).catch(error => {
    console.error(`Error initializing items : ${error}.`);
    reject(error);
  });
};

export const setPropertiesSetupDone = ({ commit }, value) => {
  return new Promise((resolve, reject) => {
    commit("setPropertiesSetupDone", value);
    resolve();
  }).catch(error => {
    console.error(`Error initializing properties : ${error}.`);
    reject(error);
  });
};

export const addItem = ({ commit }, item) => {
  return new Promise((resolve, reject) => {
    commit("addItem", item);
    resolve();
  }).catch(error => {
    console.error(`Error adding item : ${error}.`);
    reject(error);
  });
};

export const addProperty = ({ commit }, property) => {
  return new Promise((resolve, reject) => {
    commit("addProperty", property);
    resolve();
  }).catch(error => {
    console.error(`Error adding property : ${error}.`);
    reject(error);
  });
};

export const deleteItem = ({ commit }, index) => {
  return new Promise((resolve, reject) => {
    commit("deleteItem", index);
    resolve();
  }).catch(error => {
    console.error(`Error deleting item : ${error}.`);
    reject(error);
  });
};

export const deleteProperty = ({ commit }, index) => {
  return new Promise((resolve, reject) => {
    commit("deleteProperty", index);
    resolve();
  }).catch(error => {
    console.error(`Error deleting property : ${error}.`);
    reject(error);
  });
};

export const updateData = ({ commit }, data) => {
  return new Promise((resolve, reject) => {
    commit("updateData", data);
    resolve();
  }).catch(error => {
    console.error(`Error updating item : ${error}.`);
    reject(error);
  });
};
