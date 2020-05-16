<template>
  <div class="container has-text-centered">
    <h1 class="title">Charts</h1>
    <LogEventsResult />
    <br />
    <!-- <FeatureExtractorResults /> -->
  </div>
</template>

<script>
import LogEventsResult from "@/components/LogEventsResult.vue";
// import LogClustersResult from "@/components/LogClustersResult.vue";
// import FeatureExtractorResults from "@/components/FeatureExtractorResults.vue";

export default {
  name: "Charts",
  components: {
    LogEventsResult,
    // LogClustersResult
    // FeatureExtractorResults
  }
};
</script>
