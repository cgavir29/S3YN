<template>
  <div class="container has-text-centered">
    <h1 class="title">Charts</h1>
    <LogEventsResult />
    <br />
    <LogClustersResult />
    <br />
  </div>
</template>

<script>
import LogEventsResult from "@/components/LogEventsResult.vue";
import LogClustersResult from "@/components/LogClustersResult.vue";

export default {
  name: "Charts",
  components: {
    LogEventsResult,
    LogClustersResult
  }
};
</script>
