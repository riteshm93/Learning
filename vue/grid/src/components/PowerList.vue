<template>
<p>{{item}}</p>
</template>

<script lang="ts">
import Vue from 'vue'
export default Vue.extend({
  props: {
      item: {
          type: String
      }
  }
})
</script>
