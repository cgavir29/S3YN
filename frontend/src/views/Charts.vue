<template>
  <div class="container has-text-centered">
    <h1 class="title">Charts</h1>
    <ParserEvents />
    <br />
    <ExtractionFeatures />
  </div>
</template>

<script>
import ParserEvents from "@/components/ParserEvents.vue";
import ExtractionFeatures from "@/components/ExtractionFeatures.vue";

export default {
  name: "Charts",
  components: {
    ParserEvents,
    ExtractionFeatures
  }
};
</script>
