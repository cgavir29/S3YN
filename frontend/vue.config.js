module.exports = {
  devServer: {
    disableHostCheck: true
  },
  css: {
    loaderOptions: {
      sass: {
        data: `
          @import '@/scss/_variables.scss'
        `
      }
    }
  }
}
