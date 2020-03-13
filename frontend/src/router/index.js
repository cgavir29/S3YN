import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import About from '../views/About.vue'
import Databases from '../views/Databases.vue'
import Queries from '../views/Queries.vue'
import Visualizations from '../views/Visualizations.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    component: About
  },
  {
    path: '/databases',
    name: 'Databases',
    component: Databases
  },
  {
    path: '/queries',
    name: 'Queries',
    component: Queries
  },
  {
    path: '/visualizations',
    name: 'Visualizations',
    component: Visualizations
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
