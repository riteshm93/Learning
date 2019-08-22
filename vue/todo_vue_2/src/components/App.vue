<template>
<div class='todos'>
    <input class='new-todo' placeholder="Add a new todo" v-model='newTodo' v-on:keydown.enter='addTodo'/>
    <ul v-if='todosList.length'>
        <li>
            <ul class = "options">
                <li v-on:click='showAll'>All</li>
                <li v-on:click='showActive'>Active</li>
                <li v-on:click='showCompleted'>Completed</li>
                <li v-on:click='clearAll'>Clear All</li>
            </ul>
        </li>
        <todo-item
        v-for="todo in todosList"
        v-if="filter == 'all' || (filter == 'active' && !todo.completed)|| (filter == 'completed' && todo.completed)"
        v-bind:key="todo.id"
        v-bind:todo="todo">
        </todo-item>
    </ul>
</div>
</template>

<script lang="ts">
import Vue from 'vue';
import TodoItem from './TodoItem.vue';

export default Vue.extend({
    data: function() {
        return({
        newTodo: '',
        todosList: JSON.parse(localStorage.getItem("todos") || '[]'),
        filter: 'all',
        });
    },
    components: {
        TodoItem
    },
    methods: {
        addTodo: function() {
            this.todosList.push({
                id: this.todosList.length,
                title: this.newTodo,
                isActive: true,
                editMode: false,
                completed: false
            });
            localStorage.setItem("todos", JSON.stringify(this.todosList));
            this.newTodo = '';
        },
        showAll: function() {
            this.filter = 'all';
        },
        showActive: function() {
            this.filter = 'active';
        },
        showCompleted: function() {
            this.filter = 'completed';
        },
        clearAll: function() {
            let todos = [Object];
            this.todosList.forEach(function(todo: any, index: number) {
                todo.completed = true;
                todos[index] = todo;
            });
            localStorage.setItem("todos", JSON.stringify(todos));
        }
    }
})
</script>

<style>
.new-todo{
    width: 100%;
}
.todos{
    margin: 10px 25%;
}
.options{
    margin: 5px;
}
.options li{
    display: inline;
    margin: 8px;
    color: grey;
}
.options li:hover{
    color: blue;
}
</style>

