import Vue from "nativescript-vue";
import Vuex from "vuex";

import mutations from "./mutations";
import * as actions from "./actions";
import * as getters from "./getters";

Vue.use(Vuex);

const store = new Vuex.Store({
  state: {
    table: "",
    tables: [],
    isItemsSetupDone: true,
    isPropertiesSetupDone: true,
    items: [],
    properties: [],
    data: []
  },
  mutations,
  actions,
  getters
});

Vue.prototype.$store = store;

export default store;
