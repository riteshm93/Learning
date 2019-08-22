<template>
<li v-if="todo.isActive">
    <div class ="row">
        <span class="col-sm-1 h5">
            <input class="status-toggle" type="checkbox" v-model="todo.completed" v-on:click="toggleStatus"/>
        </span>
        <span class="col-sm-10 h5">
            {{todo.title}}
            <span v-if="!todo.editMode">
                <i class="fa fa-lg fa-pencil-square-o text-primary" v-on:click="toggleEditMode"></i>
            </span>
        </span>
        <span class="col-sm-1">
            <i id='delete' class="fa fa-lg fa-trash-o text-danger" v-on:click="deleteTodo" ></i>
        </span>
    </div>
    <div class="row" v-if="todo.editMode">
        <span class="col-sm-11" >
            <input class='edit-input' v-model.lazy="todo.title"/>
        </span>
        <span class="col-sm-1">
            <i class="fa fa-lg fa-check text-success" v-on:click="toggleEditMode"></i>
        </span>
    </div>
</li>
</template>

<script lang="ts">
import Vue from 'vue';

export default Vue.extend({
    props: {
        todo: {
            type: Object
        }
    },
    methods: {
        deleteTodo: function() {
            this.todo.isActive = false;
            this.updateTodo(this.todo.id, this.todo);
        },
        toggleEditMode: function() {
            this.todo.editMode = !this.todo.editMode;
            this.updateTodo(this.todo.id, this.todo);
        },
        toggleStatus: function() {
            this.todo.completed = !this.todo.completed;
            this.updateTodo(this.todo.id, this.todo);
        },
        updateTodo: function (index: number, todo: Object){
            let todos = JSON.parse(localStorage.getItem("todos") || "[]");
            todos[index] = todo;
            localStorage.setItem("todos", JSON.stringify(todos));
        }
    }
})
</script>


<style scoped>
.edit-input{
    width: 100%;
}
li{
    border: 1px solid black;
    border-radius: 3px;
    padding: 20px;
    background: lightgoldenrodyellow;
    margin: 10px;
}
.status-toggle{
    margin-top: 4px;
}
</style>
