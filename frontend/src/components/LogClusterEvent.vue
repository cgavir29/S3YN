<template>
  <div class="columns is-multiline">
    <div class="column">
      <b-collapse class="card" animation="slide" aria-id="contentIdForA11y3">
        <div
          slot="trigger"
          slot-scope="props"
          class="card-header"
          role="button"
          aria-controls="contentIdForA11y3"
        >
          <p class="card-header-title">Event - {{ event }}</p>
          <a class="card-header-icon">
            <b-icon :icon="props.open ? 'fas fa-angle-down' : 'fas fa-angle-up'"> </b-icon>
          </a>
        </div>
        <div class="card-content">
          <div class="content">
            <div class="content" v-for="(blk, index) in eventBlks" :key="index">
              <p>{{ blk }}</p>
            </div>
          </div>
        </div>
      </b-collapse>
    </div>
    <!-- <div class="column">
    Second column
  </div>
  <div class="column">
    Third column
  </div> -->
    <!-- <div class="column">
    Fourth column
  </div> -->
  </div>
</template>

<script>
export default {
  name: "LogClusterEvent",
  props: ["event", "eventBlks"]
};
</script>
