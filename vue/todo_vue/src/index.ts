import TodoItem from "./components/TodoItem.vue";
import EditTodo from "./components/EditTodo.vue";

if(!localStorage.todos) {
  localStorage.setItem("todos", "[]")
}

interface Todo {
  id: number;
  title: string;
  isActive: boolean;
}

new Vue({
  el: '#content',
  data: {
    newTodoText: ''
  },
  computed: {
    todosList: function (): Object[] {
        return JSON.parse(localStorage.getItem("todos")||'');
      }
  },
  components: {
    TodoItem
  },
  methods: {
    addNewTodo: function () {
        var vm = this as any;
        var todos: Object[] = vm.todosList;
        todos.push({
          id: vm.todosList.length,
          title: vm.newTodoText,
          isActive: true
        })
        vm.newTodoText = '';
        localStorage.setItem("todos", JSON.stringify(todos));
        alert("New Todo added.");
        window.location.href = "index.html";
    },
    redirectToEditTodoPage: function (index: number) {
        localStorage.editIndex = index;
        window.location.href = "edit-todo.html";
    },
    deleteTodo: function (index: number) {
        var vm = this as any
        var todos = vm.todosList;
        var todo = <Todo>todos[index];
        if(confirm('Are you sure you want to delete todo: "' + todo.title + '"?'))
        {
          todos.splice(index, 1)[0];
          todo.isActive = false;
          todos.splice(index, 0, todo);
          localStorage.setItem("todos", JSON.stringify(todos));
          window.location.href = "index.html";
        }
    }
  }
})

new Vue({
  el: '#edit-content',
  data: {
    newTodoText: '',
  },
  components: {
    EditTodo
  },
  computed: {
    todosList: function (): Object[] {
        return JSON.parse(localStorage.getItem("todos")||'');
      },
    oldTodoText: function (): string {
        var vm = this as any;
        return vm.todosList[localStorage.editIndex].title;
      },
    index: function (): number {
        return localStorage.editIndex;
      },
  }
})