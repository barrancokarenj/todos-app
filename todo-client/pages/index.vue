<template>
  <Layout>
    <TodoList />
  </Layout>
</template>

<script>
import Layout from "../components/Layout.vue";
import TodoList from "../components/TodoList.vue";
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import Vue from 'vue';

Vue.component('font-awesome-icon', FontAwesomeIcon);

export default {
  name: "IndexPage",
  components: { Layout, TodoList }
}
</script>