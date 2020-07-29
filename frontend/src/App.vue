<template>
  <div id="app">
    <Header></Header>
    <Body></Body>
  </div>
</template>

<script>
import Header from "./components/Header.vue";
import Body from "./components/Body.vue";

export default {
  name: "App",
  components: {
    Header,
    Body,
  },
};
</script>

<style>
@import "~bootstrap/dist/css/bootstrap.css";
</style>
