<template>
<div>
    <p>Edit Todo "{{oldtodo}}"</p>
    <input v-model="newtodo" />
    <button class="btn-sm btn-primary" v-on:click="editTodo">Update</button>
</div>
</template>

<script>
export default {
  props: {
    oldtodo: {
      type: String,
    },
    newtodo: {
      type: String,
    },
    index: {
      type: Number,
    },
    todoslist: {
      type: [],
    }
  },
  methods: {
    editTodo: function () {
        var todos = this.todoslist;
        var todo = todos.splice(this.index, 1)[0];
        todo.title = this.newtodo;
        todos.splice(this.index, 0, todo);
        localStorage.setItem("todos", JSON.stringify(todos));
        alert('Todo Updated.');
        window.location.href = "index.html";
    }
  }
}
</script>