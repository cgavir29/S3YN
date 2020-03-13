<template>
    <div>
      <h1 class="title">Add Database Credentials</h1>
      <DatabaseForm />
    </div>
</template>

<script>
import DatabaseForm from '@/components/DatabaseForm.vue'

export default {
  name: 'Databases',
  components: {
    DatabaseForm
  }
}
</script>
