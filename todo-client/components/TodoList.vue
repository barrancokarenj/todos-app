<template>
  <div class="w-full max-w-xl p-4 bg-white border border-gray-200 rounded-lg shadow-lg lg:p-8">
    <h1 class="mx-[10px] mb-4 text-center text-2xl">Your To Do List</h1>
    <div class="flex items-center justify-between mb-8">
      <div class="w-full">
        <label for="default-search" class="mb-2 text-sm font-medium text-gray-900 sr-only">Search</label>
        <div class="relative">
            <div class="absolute inset-y-0 start-0 flex items-center ps-3 pointer-events-none">
                <font-awesome-icon :icon="['fas', 'search']" />
            </div>
            <input type="search" v-model="searchQuery" placeholder="Search" class="block w-full p-4 ps-10 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50"/>
        </div>
        <div class="relative">
            <div class="absolute inset-y-0 start-0 flex items-center ps-3 pointer-events-none">
              <font-awesome-icon :icon="['fas', 'plus']" />
            </div>
            <input type="text" placeholder="Add your new task" v-model="newTodoText" @keyup.enter="handleAddToDo" class="block w-full mt-4 p-4 ps-10 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-blue-500 focus:border-blue-500">
        </div>
      </div>
    </div>
    <div class="flex-row flex">
      <div class="flex flex-col items-start p-4 border-black">
        <a href="#" :class="{ underline : filter === undefined }"
          @click="handleFilterChange()">All</a>
        <a href="#" :class="{ underline : filter === false }"
          @click="handleFilterChange(false)">Active</a>
        <a href="#" :class="{ underline : filter === true }"
          @click="handleFilterChange(true)">Completed</a>
      </div>
      <div class="w-full">
        <p class="m20" v-if="$fetchState.pending">Retrieving list of To Do ...</p>
        <p class="m20" v-else-if="$fetchState.error">Error retrieving list of To Do</p>
        <div v-else>
          <div class="toDoRow" v-for="todo of filteredItems" :key="todo.id">
            <Todo :todo="todo" @onChange="handleChange" @onDelete="handleDelete" />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { debounce } from 'lodash'
import Todo from './Todo.vue'

export default {
  data() {
    return {
    todos: [],
    newTodoText: '',
    filter: undefined,
    searchQuery: ''
  }},
  async fetch() {
    let path = 'todos'
    if (this.filter !== undefined) {
      path += `?completed=${this.filter}`
    }
    this.todos = await fetch(`${this.$config.apiURL}/${path}`)
      .then(res => res.json());
  },
  methods: {
    async handleAddToDo() {
      if(this.newTodoText !== '') {
        const todo = { description: this.newTodoText, complete: false };
        const res = await fetch(`${this.$config.apiURL}/todos`, {
          method: "POST",
          body: JSON.stringify(todo),
          headers: {
            'Content-Type': 'application/json'
          }
        });
        const json = await res.json();
        this.todos.push(json);
        this.newTodoText = ''
      }
    },
    handleChange: debounce(async function (todo) {
      await fetch(`${this.$config.apiURL}/todos/${todo.id}`, {
        method: "PUT",
        body: JSON.stringify(todo),
        headers: {
          'Content-Type': 'application/json'
        }
      });
    }, 500),
    async handleDelete(todo) {
      await fetch(`${this.$config.apiURL}/todos/${todo.id}`, {
        method: "DELETE"
      });
      const idx = this.todos.findIndex((t) => t.id === todo.id)
      const todosCopy = [...this.todos]
      todosCopy.splice(idx, 1)
      this.todos = todosCopy
    },
    handleFilterChange(value) {
      this.filter = value
      this.$fetch()
    }
  },
  computed: {
     filteredItems() {
      return this.todos.filter(todo =>todo.description.toLowerCase().includes(this.searchQuery.toLowerCase()))
    }
  },
  components: { Todo }
}
</script>
