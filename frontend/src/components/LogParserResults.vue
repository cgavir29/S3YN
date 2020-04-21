<template>
  <div>
    <p class="subtitle has-text-weight-bold">Events</p>
    <div v-if="this.getEvents">
      <b-table
        :data="this.getEvents"
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

          <b-table-column field="event" label="Event">
            {{ props.row.event }}
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
  name: "LogParserResults",
  computed: {
    ...mapGetters(["getEvents"])
  }
};
</script>
