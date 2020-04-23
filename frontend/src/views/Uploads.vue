<template>
  <div class="container">
    <h1 class="title">Upload Logs to Analyze</h1>
    <LogUpload />
  </div>
</template>

<script>
import LogUpload from '@/components/LogUpload.vue'

export default {
  name: 'Uploads',
  components: {
    LogUpload
  }
}
</script>
