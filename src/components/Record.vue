<template>
  <span class="record">
    <button @click="createGame({score: 10, level: 1})">HI</button>
  </span>
</template>

<script>
import {  createGame } from '../utils/users';
export default {
  setup() {
    return { createGame };
  },
};
</script>
