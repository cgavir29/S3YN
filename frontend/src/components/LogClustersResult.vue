<template>
  <section></section>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "AnomalyDetectionResults",
  computed: {
    ...mapGetters(["getClusters"])
  }
};
</script>
