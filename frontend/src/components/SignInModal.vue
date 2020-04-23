<template>
  <form @submit.prevent>
    <div class="modal-card" style="width: auto">
      <header class="modal-card-head">
        <p class="modal-card-title">Sign In</p>
      </header>
      <section class="modal-card-body">
        <b-field label="Email">
          <b-input
            type="email"
            v-model="user.email"
            placeholder="Your email"
            required
          ></b-input>
        </b-field>

        <b-field label="Password">
          <b-input
            type="password"
            v-model="user.password"
            password-reveal
            placeholder="Your password"
            required
          ></b-input>
        </b-field>
      </section>
      <footer class="modal-card-foot">
        <button class="button is-warning" @click="handleSubmit">Login</button>
        <button class="button" type="button" @click="$parent.close()">
          Close
        </button>
      </footer>
    </div>
  </form>
</template>

<script>
import { mapActions } from "vuex";
import axios from "axios";

export default {
  name: "SignIn",
  data() {
    return {
      user: {
        email: "",
        password: ""
      }
    };
  },
  methods: {
    ...mapActions(["logUser", "fetchLogs"]),
    handleSubmit() {
      if (this.user.email === "" || this.user.password === "") return;

      axios
        .post("/login", this.user)
        .then(res => {
          this.logUser(res.data);
          this.$parent.close();
          this.$router.push({ name: "Home" });
        })
        .catch(err => {
          this.$buefy.dialog.alert({
            title: "Error",
            message: err.response.data.msg,
            type: "is-danger",
            hasIcon: true,
            icon: "times-circle",
            iconPack: "fa",
            ariaRole: "alertdialog",
            ariaModal: true
          });
        });
    }
  }
};
</script>
