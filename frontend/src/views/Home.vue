<template>
  <div>
    <div v-if="!getUser">
      <h1 class="title">Welcome to S3YN</h1>
      Sign in to start detecting
    </div>
    <div v-else>
      <h1 class="title">My Logs</h1>
      <LogList />
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import LogList from "@/components/LogList.vue";

export default {
  name: "Home",
  components: {
    LogList
  },
  computed: {
    ...mapGetters(["getUser"])
  }
};
</script>
