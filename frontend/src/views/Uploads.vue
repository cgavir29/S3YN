<template>
  <div class="container">
    <h1 class="title">Upload Logs to Analyze</h1>
    <UploadLog />
  </div>
</template>

<script>
import UploadLog from '@/components/UploadLog.vue'

export default {
  name: 'Uploads',
  components: {
    UploadLog
  }
}
</script>
