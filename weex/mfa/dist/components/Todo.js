// { "framework": "Vue"} 

/******/ (function(modules) { // webpackBootstrap
/******/ 	// The module cache
/******/ 	var installedModules = {};
/******/
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/
/******/ 		// Check if module is in cache
/******/ 		if(installedModules[moduleId]) {
/******/ 			return installedModules[moduleId].exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = installedModules[moduleId] = {
/******/ 			i: moduleId,
/******/ 			l: false,
/******/ 			exports: {}
/******/ 		};
/******/
/******/ 		// Execute the module function
/******/ 		modules[moduleId].call(module.exports, module, module.exports, __webpack_require__);
/******/
/******/ 		// Flag the module as loaded
/******/ 		module.l = true;
/******/
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/
/******/
/******/ 	// expose the modules object (__webpack_modules__)
/******/ 	__webpack_require__.m = modules;
/******/
/******/ 	// expose the module cache
/******/ 	__webpack_require__.c = installedModules;
/******/
/******/ 	// define getter function for harmony exports
/******/ 	__webpack_require__.d = function(exports, name, getter) {
/******/ 		if(!__webpack_require__.o(exports, name)) {
/******/ 			Object.defineProperty(exports, name, {
/******/ 				configurable: false,
/******/ 				enumerable: true,
/******/ 				get: getter
/******/ 			});
/******/ 		}
/******/ 	};
/******/
/******/ 	// getDefaultExport function for compatibility with non-harmony modules
/******/ 	__webpack_require__.n = function(module) {
/******/ 		var getter = module && module.__esModule ?
/******/ 			function getDefault() { return module['default']; } :
/******/ 			function getModuleExports() { return module; };
/******/ 		__webpack_require__.d(getter, 'a', getter);
/******/ 		return getter;
/******/ 	};
/******/
/******/ 	// Object.prototype.hasOwnProperty.call
/******/ 	__webpack_require__.o = function(object, property) { return Object.prototype.hasOwnProperty.call(object, property); };
/******/
/******/ 	// __webpack_public_path__
/******/ 	__webpack_require__.p = "";
/******/
/******/ 	// Load entry module and return exports
/******/ 	return __webpack_require__(__webpack_require__.s = 4);
/******/ })
/************************************************************************/
/******/ ([
/* 0 */
/***/ (function(module, exports, __webpack_require__) {

var __vue_exports__, __vue_options__
var __vue_styles__ = []

/* styles */
__vue_styles__.push(__webpack_require__(1)
)

/* script */
__vue_exports__ = __webpack_require__(2)

/* template */
var __vue_template__ = __webpack_require__(3)
__vue_options__ = __vue_exports__ = __vue_exports__ || {}
if (
  typeof __vue_exports__.default === "object" ||
  typeof __vue_exports__.default === "function"
) {
if (Object.keys(__vue_exports__).some(function (key) { return key !== "default" && key !== "__esModule" })) {console.error("named exports are not supported in *.vue files.")}
__vue_options__ = __vue_exports__ = __vue_exports__.default
}
if (typeof __vue_options__ === "function") {
  __vue_options__ = __vue_options__.options
}
__vue_options__.__file = "/Users/ritesh/Downloads/traning/weex/mfa/src/components/Todo.vue"
__vue_options__.render = __vue_template__.render
__vue_options__.staticRenderFns = __vue_template__.staticRenderFns
__vue_options__._scopeId = "data-v-ee48fd14"
__vue_options__.style = __vue_options__.style || {}
__vue_styles__.forEach(function (module) {
  for (var name in module) {
    __vue_options__.style[name] = module[name]
  }
})
if (typeof __register_static_styles__ === "function") {
  __register_static_styles__(__vue_options__._scopeId, __vue_styles__)
}

module.exports = __vue_exports__


/***/ }),
/* 1 */
/***/ (function(module, exports) {

module.exports = {
  "header": {
    "width": "750",
    "paddingTop": "10",
    "paddingRight": "10",
    "paddingBottom": "10",
    "paddingLeft": "10",
    "fontSize": "40",
    "textAlign": "center",
    "fontWeight": "bold",
    "color": "#000000",
    "backgroundColor": "#00b4ff"
  },
  "filter-tabs": {
    "flexDirection": "row",
    "backgroundColor": "#00b4ff"
  },
  "filter-tab": {
    "marginTop": "0",
    "marginRight": "20",
    "marginBottom": "0",
    "marginLeft": "20",
    "paddingTop": "10",
    "paddingRight": "10",
    "paddingBottom": "10",
    "paddingLeft": "10",
    "width": "210"
  },
  "active-tab": {
    "borderTopLeftRadius": "25",
    "borderTopRightRadius": "25",
    "backgroundColor": "#FFFFFF"
  },
  "filter-text": {
    "textAlign": "center",
    "fontSize": "30"
  },
  "todo": {
    "width": "730",
    "borderWidth": "1",
    "borderColor": "#000000",
    "borderRadius": "3",
    "marginTop": "10",
    "marginRight": "10",
    "marginBottom": "10",
    "marginLeft": "10",
    "flexDirection": "row"
  },
  "active-todo": {
    "backgroundColor": "#FAFAD2"
  },
  "completed-todo": {
    "backgroundColor": "#62dd96"
  },
  "todo-details": {
    "fontSize": "20",
    "paddingTop": "20",
    "paddingRight": "20",
    "paddingBottom": "20",
    "paddingLeft": "20",
    "width": "670"
  },
  "btn": {
    "justifyContent": "center"
  },
  "btn-text": {
    "textAlign": "center",
    "fontSize": "30",
    "paddingTop": "10",
    "paddingRight": "10",
    "paddingBottom": "10",
    "paddingLeft": "10",
    "color": "#808080"
  },
  "add-todo": {
    "position": "absolute",
    "bottom": "0",
    "borderWidth": "2",
    "borderStyle": "solid",
    "borderColor": "#00b4ff",
    "flexDirection": "row"
  },
  "new-todo": {
    "textAlign": "center",
    "width": "650",
    "fontSize": "30",
    "paddingTop": "10",
    "paddingRight": "10",
    "paddingBottom": "10",
    "paddingLeft": "10",
    "color": "#000000"
  },
  "btn-send": {
    "width": "96",
    "backgroundColor": "#00b4ff",
    "backgroundColor:active": "#00b4ff"
  },
  "btn-send-text": {
    "color": "#000000",
    "fontSize": "30"
  }
}

/***/ }),
/* 2 */
/***/ (function(module, exports, __webpack_require__) {

"use strict";


Object.defineProperty(exports, "__esModule", {
  value: true
});
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//

var storage = weex.requireModule('storage');
var modal = weex.requireModule('modal');

exports.default = {
  data: function data() {
    return {
      newTodo: '',
      todosList: [],
      filter: 'all',
      filterButtons: ['all', 'active', 'completed']
    };
  },
  methods: {
    created: function created() {
      var _this = this;

      storage.getItem('todos_weex_app', function (event) {
        _this.todosList = JSON.parse(event.data || '[]');
      });
    },
    addTodo: function addTodo() {
      this.todosList.push({
        title: this.newTodo,
        isActive: true,
        editMode: false,
        completed: false,
        deleted: false
      });
      storage.setItem('todos_weex_app', JSON.stringify(this.todosList));
      this.newTodo = '';
      modal.toast({
        message: 'New Todo added',
        duration: 1
      });
    },
    filterTodo: function filterTodo(type) {
      this.filter = type;
    },
    removeTodo: function removeTodo(todo) {
      todo.deleted = true;
      modal.toast({
        message: 'Todo removed',
        duration: 1
      });
    },
    toggleComplete: function toggleComplete(todo) {
      todo.completed = !todo.completed;
      var modalMessage = todo.title + ' is marked ' + (todo.completed ? 'completed' : 'active');
      modal.toast({
        message: modalMessage,
        duration: 1
      });
    }
  }
};

/***/ }),
/* 3 */
/***/ (function(module, exports) {

module.exports={render:function (){var _vm=this;var _h=_vm.$createElement;var _c=_vm._self._c||_h;
  return _c('div', [_c('text', {
    staticClass: ["header"]
  }, [_vm._v("Todos")]), _c('list', [_c('header', {
    staticClass: ["filter-tabs"],
    appendAsTree: true,
    attrs: {
      "append": "tree"
    }
  }, _vm._l((_vm.filterButtons), function(btn, x) {
    return _c('div', {
      key: x,
      class: ['filter-tab', btn === _vm.filter ? 'active-tab' : ''],
      on: {
        "click": function($event) {
          _vm.filterTodo(btn)
        }
      }
    }, [_c('text', {
      staticClass: ["filter-text"]
    }, [_vm._v(_vm._s(btn))])])
  })), (!_vm.todosList.length) ? _c('text', [_vm._v("No Todos Added")]) : _vm._e(), _vm._l((_vm.todosList), function(todo, i) {
    return (!todo.deleted && (_vm.filter == 'all' || (_vm.filter == 'active' && !todo.completed) || (_vm.filter == 'completed' && todo.completed))) ? _c('cell', {
      key: i,
      appendAsTree: true,
      attrs: {
        "append": "tree"
      }
    }, [_c('div', {
      class: ['todo', todo.completed ? 'completed-todo' : 'active-todo']
    }, [_c('text', {
      staticClass: ["todo-details"],
      on: {
        "click": function($event) {
          _vm.toggleComplete(todo)
        }
      }
    }, [_vm._v(_vm._s(todo.title))]), _c('div', {
      staticClass: ["btn", "btn-delete"],
      on: {
        "click": function($event) {
          _vm.removeTodo(todo)
        }
      }
    }, [_c('text', {
      staticClass: ["btn-text", "btn-delete-text"]
    }, [_vm._v("×")])])])]) : _vm._e()
  })], 2), _c('div', {
    staticClass: ["add-todo"]
  }, [_c('input', {
    staticClass: ["new-todo"],
    attrs: {
      "type": "text",
      "placeholder": "Add a new todo",
      "value": (_vm.newTodo)
    },
    on: {
      "keydown": _vm.addTodo,
      "return": _vm.addTodo,
      "input": function($event) {
        _vm.newTodo = $event.target.attr.value
      }
    }
  }), _c('div', {
    staticClass: ["btn", "btn-send"],
    on: {
      "click": _vm.addTodo
    }
  }, [_c('text', {
    staticClass: ["btn-text", "btn-send-text"]
  }, [_vm._v("Save")])])])])
},staticRenderFns: []}
module.exports.render._withStripped = true

/***/ }),
/* 4 */
/***/ (function(module, exports, __webpack_require__) {

"use strict";


var _Todo = __webpack_require__(0);

var _Todo2 = _interopRequireDefault(_Todo);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

_Todo2.default.el = '#root';
new Vue(_Todo2.default);

/***/ })
/******/ ]);