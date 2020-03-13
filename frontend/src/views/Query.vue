<template>
  <div>
    <h1 class="title">Select Database to Query</h1>
    <DatabaseQuery />
  </div>
</template>

<script>
import DatabaseQuery from '@/components/DatabaseQuery.vue'

export default {
  components: {
    DatabaseQuery
  }
}
</script>
