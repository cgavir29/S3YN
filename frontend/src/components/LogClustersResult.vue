<template>
  <section>
    <p class="subtitle has-text-weight-bold">Clusters</p>
    <div v-if="this.getClusters.length > 0">
      <div v-for="(cluster, index) in this.getClusters" :key="index">
        <LogCluster
          :index="index + 1"
          :numPossibleAbnormalEvents="cluster.num_possible_abnormal_events"
          :possibleAbnormalEvents="cluster.possible_abnormal_events"
        />
        <br />
      </div>
    </div>
    <div v-else>
      <div>
        <span class="tag is-warning is-medium">No anomalies detected</span>
      </div>
    </div>
  </section>
</template>

<script>
import { mapGetters } from "vuex";
import LogCluster from "@/components/LogCluster.vue";

export default {
  name: "LogClustersResult",
  components: {
    LogCluster
  },
  computed: {
    ...mapGetters(["getClusters"])
  }
};
</script>
