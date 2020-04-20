<template>
  <div>
    <h2 class="subtitle">Events</h2>
    <div v-if="this.getEvents">
      <table class="table">
        <thead>
          <tr>
            <th>ID</th>
            <th>Event</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(event, index) in this.getEvents" v-bind:key="index">
            <th>{{ index }}</th>
            <th>{{ event }}</th>
          </tr>
        </tbody>
      </table>
    </div>
    <div v-else>
      <p>No results yet</p>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "ParserEvents",
  computed: {
    ...mapGetters(["getEvents"])
  }
};
</script>
