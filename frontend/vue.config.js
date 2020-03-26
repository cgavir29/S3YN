module.exports = {
  devServer: {
    disableHostCheck: true,
    proxy: 'http://localhost:5000'
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
