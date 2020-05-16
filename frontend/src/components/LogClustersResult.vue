<template>
  <section></section>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "LogClustersResult",
  computed: {
    ...mapGetters(["getClusters"])
  }
};
</script>
