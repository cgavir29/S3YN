<template>
  <div>
    <h1 class="title">Welcome to S3YN</h1>
    <div v-if="!getUser">
      Sign in to start detecting
    </div>
    <div v-else>
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
