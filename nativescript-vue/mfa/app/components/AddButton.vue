<template>
  <StackLayout class="fab-button" @tap="$emit('onButtonTap')" @touch="onButtonTouch">
    <GridLayout
      rows="2, auto"
      horizontalAlignment="center"
      class="fab-icon"
    >
      <Label row="1" class="fab-dash--1"/>
      <Label row="1" class="fab-dash--2"/>
    </GridLayout>
  </StackLayout>
</template>

<script>
export default {
  methods: {
    onButtonTouch(args) {
      console.log('aaa');
      this.$emit("onButtonTouch", args);
    }
  }
};
</script>

<style scoped>
.fab-button {
  width: 36;
  height: 36;
  background-color: #487955;
  border-radius: 18;
  vertical-align: center;
}

.fab-icon {
  height: 18;
  width: 18;
}

.fab-dash--1,
.fab-dash--2 {
  background-color: #fff;
  transform: translate(0, -2);
  height: 18;
  width: 3;
}

.fab-dash--1 {
  transform: rotate(90deg) translate(0, -2);
}
</style>