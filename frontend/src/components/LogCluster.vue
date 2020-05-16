<template>
  <div>
    <div v-if="possibleAbnormal > 0">
      <b-message
        title="Danger with icon"
        type="is-danger"
        has-icon
        aria-close-label="Close message"
      >
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce id
        fermentum quam. Proin sagittis, nibh id hendrerit imperdiet, elit sapien
        laoreet elit
      </b-message>
    </div>
    <div v-else>
      <b-message
        title="Success with icon"
        type="is-success"
        has-icon
        aria-close-label="Close message"
      >
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce id
        fermentum quam. Proin sagittis, nibh id hendrerit imperdiet, elit sapien
        laoreet elit
      </b-message>
    </div>
  </div>
</template>

<script>
export default {
  name: "LogCluster",
  props: ["possibleAbnormal", "eventBlks"]
};
</script>
