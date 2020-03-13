<template>
    <div class="container is-fluid">
    <b-field label="Database Name">
      <b-input v-model="db.name" type="text" required></b-input>
    </b-field>

    <b-field label="Database URL">
      <b-input v-model="db.url" type="text" required></b-input>
    </b-field>

    <b-field label="Database Username">
      <b-input v-model="db.username" type="text" required></b-input>
    </b-field>

    <b-field label="Database Password">
      <b-input v-model="db.password" type="password" password-reveal required></b-input>
    </b-field>

    <b-button v-on:click="handleSubmit" type="is-warning">Add</b-button>
    </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'DatabaseForm',
  data() {
    return {
      db: {
        name: '',
        url: '',
        username: '',
        password: ''
      }
    }
  },
  methods: {
    handleSubmit() {
      if (this.db.name === '' || this.db.url === '' || this.db.username === '' || this.db.password === '') return
      axios.post('/api/databases', this.db)
        .then(res => {
          console.log(res.data)
        })
        .catch(error => {
          this.$buefy.dialog.alert({
            title: 'Error',
            message: error.response.data.error,
            type: 'is-danger',
            hasIcon: true,
            icon: 'times-circle',
            iconPack: 'fa',
            ariaRole: 'alertdialog',
            ariaModal: true
          })
        })
    }
  }
}
</script>
