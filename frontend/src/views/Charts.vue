<template>
  <div class="container has-text-centered">
    <h1 class="title">Charts</h1>
    <LogParserResults />
    <br />
    <!-- <FeatureExtractorResults /> -->
  </div>
</template>

<script>
import LogParserResults from "@/components/LogParserResults.vue";
// import FeatureExtractorResults from "@/components/FeatureExtractorResults.vue";

export default {
  name: "Charts",
  components: {
    LogParserResults,
    // FeatureExtractorResults
  }
};
</script>
