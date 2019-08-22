<template>
<div>
  <text class="header">Todos</text>
  <list>
    <header class="filter-tabs">
      <div v-for="(btn, x) in filterButtons" :key="x" :class="['filter-tab', btn === filter ? 'active-tab': '']" @click="filterTodo(btn)">
        <text class="filter-text">{{btn}}</text>
      </div>
    </header>
    <text v-if='!todosList.length'>No Todos Added</text>
    <cell v-for="(todo, i) in todosList" v-bind:key="i"
    v-if="!todo.deleted && (filter == 'all' || (filter == 'active' && !todo.completed) || (filter == 'completed' && todo.completed))">
      <div :class="['todo', todo.completed ? 'completed-todo'   : 'active-todo' ]" >
        <text class="todo-details" @click="toggleComplete(todo)">{{todo.title}}</text>
        <div class="btn btn-delete" @click="removeTodo(todo)">
          <text class="btn-text btn-delete-text">&#215;</text>
        </div>
      </div>
    </cell>
  </list>
  <div class="add-todo">
    <input class='new-todo' type='text' placeholder="Add a new todo" v-model='newTodo' @keydown.enter='addTodo' @return='addTodo' />
    <div class="btn btn-send" @click="addTodo">
      <text class="btn-text btn-send-text">Save</text>
    </div>
  </div>
</div>
</template>

<script>
var storage = weex.requireModule('storage')
var modal = weex.requireModule('modal')

export default {
  data: function () {
    return ({
      newTodo: '',
      todosList: [],
      filter: 'all',
      filterButtons: ['all', 'active', 'completed']
    })
  },
  methods: {
    created () {
      storage.getItem('todos_weex_app', event => {
        this.todosList = JSON.parse(event.data || '[]')
      })
    },
    addTodo () {
      this.todosList.push({
        title: this.newTodo,
        isActive: true,
        editMode: false,
        completed: false,
        deleted: false
      })
      storage.setItem('todos_weex_app', JSON.stringify(this.todosList))
      this.newTodo = ''
      modal.toast({
        message: 'New Todo added',
        duration: 1
      })
    },
    filterTodo (type) {
      this.filter = type
    },
    removeTodo (todo) {
      todo.deleted = true
      modal.toast({
        message: 'Todo removed',
        duration: 1
      })
    },
    toggleComplete (todo) {
      todo.completed = !todo.completed
      var modalMessage = todo.title + ' is marked ' + (todo.completed ? 'completed' : 'active')
      modal.toast({
        message: modalMessage,
        duration: 1
      })
    }
  }
}
</script>

<style>
.header {
  width: 750px;
  padding: 10px;
  font-size: 40px;
  text-align: center;
  font-weight: bold;
  color: #000000;
  background-color: #00b4ff;
}
.filter-tabs{
  flex-direction: row;
  background-color: #00b4ff
}
.filter-tab{
  margin: 0px 20px;
  padding: 10px;
  width: 210px;
}
.active-tab{
  border-top-left-radius: 25px;
  border-top-right-radius: 25px;
  background-color: #FFFFFF;
}
.filter-text{
  text-align: center;
  font-size: 30px;
}
.todo{
  width: 730px;
  border-width: 1px;
  border-color: #000000;
  border-radius: 3px;
  margin: 10px;
  flex-direction: row;
}
.active-todo{
  background-color: #FAFAD2;
}
.completed-todo{
  background-color: #62dd96;
}
.todo-details{
  font-size: 20px;
  padding: 20px;
  width: 670px;
}
.btn {
  justify-content: center;
}
.btn-text {
  text-align: center;
  font-size: 30px;
  padding: 10px;
  color: #808080;
}
.add-todo{
  position: absolute;
  bottom: 0px;
  border-width: 2px;
  border-style: solid;
  border-color: #00b4ff;
  flex-direction: row;
}
.new-todo{
  text-align: center;
  width: 650px;
  font-size: 30px;
  padding: 10px;
  color: #000000;
}
.btn-send {
  width: 96px;
  background-color: #00b4ff;
}
.btn-send:active {
  background-color: #00b4ff;
}
.btn-send-text {
  color: #000000;
  font-size: 30px;
}
</style>
