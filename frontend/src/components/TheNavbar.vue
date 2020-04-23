<template>
  <div class="hero-head">
    <header class="navbar">
      <div class="container">
        <div class="navbar-brand">
          <router-link
            class="navbar-item title has-text-warning"
            :to="{ name: 'Home' }"
            >S3YN</router-link
          >
          <!-- <span class="navbar-burger burger" data-target="navbarMenuHeroC">
            <span></span>
            <span></span>
            <span></span>
          </span>-->
        </div>
        <div id="navbarMenuHeroC" class="navbar-menu">
          <div class="navbar-end">
            <router-link
              class="navbar-item"
              :to="{ name: 'Home' }"
              active-class="is-active"
              exact
              >Home</router-link
            >
            <router-link
              class="navbar-item"
              :to="{ name: 'About' }"
              active-class="is-active"
              exact
              >About</router-link
            >

            <div class="navbar-item" v-if="!this.getUser">
              <span clas="navbar-item">
                <a
                  class="button is-success is-inverted"
                  @click="isSignInModalActive = true"
                >
                  <span class="icon">
                    <i class="fas fa-sign-in-alt"></i>
                  </span>
                  <span>Sign In</span>
                </a>
              </span>
              <b-modal
                :active.sync="isSignInModalActive"
                has-modal-card
                trap-focus
                aria-role="dialog"
                aria-modal
              >
                <SignInModal />
              </b-modal>

              <span class="navbar-item">
                <a
                  class="button is-success is-inverted"
                  @click="isSignUpModalActive = true"
                >
                  <span class="icon">
                    <i class="fas fa-user"></i>
                  </span>
                  <span>Sign Up</span>
                </a>
              </span>
              <b-modal
                :active.sync="isSignUpModalActive"
                has-modal-card
                trap-focus
                aria-role="dialog"
                aria-modal
              >
                <SignUpModal />
              </b-modal>
            </div>

            <div class="navbar-item" v-else>
              <span class="navbar-item">
                <router-link class="navbar-item" :to="{ name: 'Home' }">
                  <a
                    href
                    class="button is-success is-inverted"
                    @click="this.clearAll"
                  >
                    <span class="icon">
                      <i class="fas fa-sign-out-alt"></i>
                    </span>
                    <span>
                      Sign Out
                    </span>
                  </a>
                </router-link>
              </span>
            </div>
          </div>
        </div>
      </div>
    </header>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
import SignInModal from "@/components/SignInModal.vue";
import SignUpModal from "@/components/SignUpModal.vue";

export default {
  name: "Navbar",
  components: {
    SignInModal,
    SignUpModal
  },
  data() {
    return {
      isSignInModalActive: false,
      isSignUpModalActive: false
    };
  },
  computed: {
    ...mapGetters(["getUser"])
  },
  methods: {
    ...mapActions(["logoutUser", "clearLogs", "clearAnomalyDetectionData"]),
    clearAll() {
      this.logoutUser();
      this.clearLogs();
      this.clearAnomalyDetectionData();
    }
  }
};
</script>
