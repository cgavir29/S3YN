<template>
  <div class="home">
    <section class="hero is-fullheight is-warning">
      <div class="hero-body">
        <div class="container">
          <h1 class="title">S3YN</h1>
            <DatabaseForm />
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import DatabaseForm from '@/components/DatabaseForm.vue'

export default {
  name: 'Home',
  components: {
    DatabaseForm
  }
}
</script>
