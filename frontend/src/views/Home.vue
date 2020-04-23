<template>
  <div>
    <h1 class="title">Welcome to S3YN</h1>
    <div v-if="!getUser">
      Sign in to start detecting
    </div>
    <div v-else>
      <LogsList />
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import LogsList from "@/components/LogsList.vue";

export default {
  name: "Home",
  components: {
    LogsList
  },
  computed: {
    ...mapGetters(["getUser"])
  }
};
</script>
