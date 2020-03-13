<template>
  <section class="hero is-success is-fullheight">
    <TheNavbar />

    <!-- Hero content: will be in the middle -->
    <div class="hero-body">
      <div class="container has-text-centered">
        <router-view />
      </div>
    </div>

    <TheFooter />
  </section>
</template>

<script>
import TheNavbar from '@/components/TheNavbar.vue'
import TheFooter from '@/components/TheFooter.vue'

export default {
  components: {
    TheNavbar,
    TheFooter
  }
}
</script>
