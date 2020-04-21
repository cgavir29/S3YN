<template>
  <div>
    <p class="subtitle has-text-weight-bold">Features</p>
    <div v-if="this.getFeatures">
      <b-table
        :data="this.getFeatures"
        ref="table"
        paginated
        per-page="5"
        detail-key="id"
        aria-next-label="Next page"
        aria-previous-label="Previous page"
        aria-page-label="Page"
        aria-current-label="Current page"
      >
        <template slot-scope="props">
          <b-table-column field="id" label="#" width="40" numeric>
            {{ props.row.id }}
          </b-table-column>

          <b-table-column field="blk" label="Block" width="40">
            {{ props.row.blk }}
          </b-table-column>

          <b-table-column field="feature" label="Feature">
            {{ props.row.feature }}
          </b-table-column>
        </template>
      </b-table>
    </div>
    <div v-else>
      <p>No results yet</p>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "FeatureExtractorResults",
  computed: {
    ...mapGetters(["getFeatures"])
  }
};
</script>
