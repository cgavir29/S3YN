<template>
  <div class="modal-card" style="width: auto">
    <header class="modal-card-head">
      <p class="modal-card-title">{{ logFilename }}</p>
    </header>
    <section class="modal-card-body has-text-black">
      <div class="has-text-black" v-if="lines.length == 0">
        <p>This file is empty</p>
      </div>
      <div class="content" v-else>
        <ol class="is-upper-roman">
          <li v-for="(line, index) in lines" :key="index">
            {{ line }}
          </li>
        </ol>
      </div>
    </section>
    <footer class="modal-card-foot has-text-centered has-right-right">
      <button class="button is-danger" @click="$parent.close()">
        Close
      </button>
    </footer>
  </div>
</template>

<script>
import axios from "axios";
import { mapGetters } from "vuex";

export default {
  name: "LogPreview",
  props: ["logSystem", "logFilename"],
  data() {
    return {
      lines: []
    };
  },
  computed: {
    ...mapGetters(["getUser"])
  },
  beforeMount() {
    axios
      .get("/users/" + this.getUser._id.$oid + "/systems/" + this.logSystem + "/files/" + this.logFilename)
      .then(res => {
        this.lines = res.data.lines;
      })
      .catch(err => console.log(err.response.data.msg));
  }
};
</script>
