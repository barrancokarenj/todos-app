<template>
  <div class="todoRow flex flex-row items-center m-4">
    <input type="checkbox" v-model="todo.complete" @click="$emit('onChange', todo)" />
    <input v-model="todo.description" @input="$emit('onChange', todo)"
      class="block w-full mx-4 p-4 ps-10 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50"/>
    <button @click="$emit('onDelete', todo)">
      <font-awesome-icon :icon="['fas', 'trash']" />
    </button>
  </div>
</template>

<script>
export default {
  props: ['todo']
}
</script>
