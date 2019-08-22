import Vue from "vue";
const fileSystemModule = require("tns-core-modules/file-system");

function getFile(name) {
  const appDirPath = fileSystemModule.knownFolders.currentApp().path;
  // android.os.Environment.getExternalStorageDirectory() + "/compareto/";
  const fileName = name + ".csv";
  const filePath = fileSystemModule.path.join(appDirPath, fileName);
  return fileSystemModule.File.fromPath(filePath);
}

function writeData(state) {
  const file = getFile(state.table);
  let fileData = "'',";
  fileData += "" + state.properties.join(",") + "";
  state.items.forEach((item, i) => {
    fileData += "\n" + item + "";
    fileData += "," + state.data[i].join(",") + "";
  });
  file
    .writeText(fileData)
    .then(() => {
      if (state.items.length && state.properties.length) {
        state.isNew = false;
      }
    })
    .catch(err => {
      console.log(err);
    });
}

const mutations = {
  initTables(state) {
    const app = fileSystemModule.knownFolders.currentApp();
    state.tables = [];
    let files = app.getEntitiesSync();
    files.forEach(file => {
      if (file.path.includes(".csv")) {
        const name = file.path.split("/").slice(-1)[0];
        state.tables.push(name.split(".csv")[0]);
      }
    });
  },
  initTable(state, table) {
    const file = getFile(table);
    file.readText().then(content => {
      let lines = content.split("\n");
      // state.properties.splice(0, state.properties.length, lines[0].split(',').splice(0,1));
      let cells = lines[0].split(",");
      state.properties = cells.splice(1, cells.length);
      lines.splice(0, 1);
      state.items = [];
      let lastDataIndex = 0;
      lines.forEach((line, i) => {
        cells = line.split(",");
        state.items.push(cells[0]);
        Vue.set(state.data, i, cells.splice(1, cells.length));
        lastDataIndex = i;
      });
      state.data.forEach((d, i) => {
        if (i > lastDataIndex) {
          Vue.set(state.data, i, []);
        }
      });
      state.table = table;
    });
  },
  deleteTable(state, table) {
    const file = getFile(table);
    file
      .remove()
      .then(res => {
        const app = fileSystemModule.knownFolders.currentApp();
        state.tables = [];
        let files = app.getEntitiesSync();
        files.forEach(file => {
          if (file.path.includes(".csv")) {
            const name = file.path.split("/").slice(-1)[0];
            state.tables.push(name.split(".csv")[0]);
          }
        });
      })
      .catch(err => {
        console.log(err.stack);
      });
  },
  setSelectTable(state, table) {
    state.table = table;
  },
  setItemsSetupDone(state, value) {
    state.isItemsSetupDone = value;
  },
  setPropertiesSetupDone(state, value) {
    state.isPropertiesSetupDone = value;
  },
  addItem(state, item) {
    state.items.push(item);
    Vue.set(state.data, state.items.length - 1, []);
    writeData(state);
  },
  addProperty(state, property) {
    state.properties.push(property);
    writeData(state);
  },
  deleteItem(state, index) {
    state.items.splice(index, 1);
    state.data.splice(index, 1);
    writeData(state);
  },
  deleteProperty(state, index) {
    for (let i = 0; i < state.data.length; i++) {
      var d = state.data[i];
      d.splice(index, 1);
      Vue.set(state.data, i, d);
    }
    state.properties.splice(index, 1);
    writeData(state);
  },
  updateData(state, data) {
    if (data.col == 0) {
      Vue.set(state.properties, data.row - 1, data.data);
    } else if (data.row == 0) {
      Vue.set(state.items, data.col - 1, data.data);
    } else {
      var d = state.data[data.col - 1];
      d[data.row - 1] = data.data;
      Vue.set(state.data, data.col - 1, d);
    }
    writeData(state);
  }
};

export default mutations;
