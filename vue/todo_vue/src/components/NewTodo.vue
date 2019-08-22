<template>
<div>
        <input
          v-model="newTodoText"
          placeholder="Add a todo"
        >
        <br />
        <button class="btn-sm btn-primary" v-on:click="addNewTodo">Add Todo</button>
</div>
</template>

<script>

</script>