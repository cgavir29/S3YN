<template>
  <div v-if="possibleAbnormalEvents > 0">
    <b-message :title="'Cluster ' + index" type="is-danger" :closable="false">
      Dispositivos IoT
      <!-- Eventos y sus dispositivos -->
    </b-message>
    <br />
  </div>
</template>

<script>
export default {
  name: "LogCluster",
  props: ["index", "possibleAbnormalEvents", "abnormalEvents"]
};
</script>
