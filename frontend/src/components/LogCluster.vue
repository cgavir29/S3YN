<template>
  <b-message
    :title="'IoT Devices by Event in Cluster ' + index"
    type="is-danger"
    :closable="false"
  >
    <div
      v-for="(value, key, index) in this.possibleAbnormalEvents"
      :key="index"
    >
      <LogClusterEvent :event="key" :eventBlks="value" />
    </div>
  </b-message>
</template>

<script>
import LogClusterEvent from "@/components/LogClusterEvent.vue";

export default {
  name: "LogCluster",
  props: ["index", "numPossibleAbnormalEvents", "possibleAbnormalEvents"],
  components: {
    LogClusterEvent
  }
};
</script>
