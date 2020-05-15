<template>
  <div class="container has-text-centered">
    <h1 class="title">Charts</h1>
    <LogEventsResult />
    <br />
    <!-- <FeatureExtractorResults /> -->
  </div>
</template>

<script>
import LogEventsResult from "@/components/LogEventsResults.vue";
import LogClustersResult from "@/components/LogClustersResults.vue";
// import FeatureExtractorResults from "@/components/FeatureExtractorResults.vue";

export default {
  name: "Charts",
  components: {
    LogEventsResult,
    LogClustersResult
    // FeatureExtractorResults
  }
};
</script>
