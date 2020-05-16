<template>
    <b-message :title="'Cluster ' + index" type="is-danger" :closable="false">
      Dispositivos IoT
      <!-- Eventos y sus dispositivos -->
    </b-message>
</template>

<script>
export default {
  name: "LogCluster",
  props: ["index", "numPossibleAbnormalEvents", "possibleAbnormalEvents"]
};
</script>
