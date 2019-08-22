<template lang="html">
<li>
  <h5>{{ title }}</h5>
  <button class="btn-sm btn-warning" v-on:click="$emit('edit')"><i class="fa fa-pencil-square-o"></i> Edit</button>
  <button class="btn-sm btn-danger" v-on:click="$emit('delete')"><i class="fa fa-trash-o"></i> Delete</button>
</li>
</template>

<script lang="ts">
export default Vue.extend({
  props: ['title']
})
</script>

<style lang="scss">
h5{display: inline;}
li{padding: 5px 0;}
</style>