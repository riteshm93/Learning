import Vue from "nativescript-vue";
import App from "./components/App";
import VueDevtools from "nativescript-vue-devtools";
import RadSideDrawer from "nativescript-ui-sidedrawer/vue";

import store from "./store";

if (TNS_ENV !== "production") {
  Vue.use(VueDevtools);
}
// Prints Vue logs when --env.production is *NOT* set while building
Vue.config.silent = TNS_ENV === "production";
// Vue.config.silent = true;

Vue.use(RadSideDrawer);

new Vue({
  render: h => h("frame", [h(App)]),
  store
}).$start();
