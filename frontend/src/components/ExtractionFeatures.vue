<template>
  <div>
    <h2 class="subtitle">Features</h2>
    <div v-if="this.getFeatures">
      <table class="table">
        <thead>
          <tr>
            <th>ID</th>
            <th>Feature</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(feature, index) in this.getFeatures" v-bind:key="index">
            <th>{{ index }}</th>
            <th>{{ feature }}</th>
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
  name: "ExtractionFeatures",
  computed: {
    ...mapGetters(["getFeatures"])
  }
};
</script>
