import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Login from '@/components/Login'
import SupLog from '@/components/Suplogs'
import Envs from '@/components/EnvItems'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/breakdown',
      name: 'Home',
      component: Home,
      meta: {
        keepAlive: true
      }
    },
    {
      path: '/',
      name: 'Home',
      component: Home,
      meta: {
        keepAlive: true
      }
    },
    {
      path: '/login',
      name: 'Login',
      component: Login,
      meta: {
        keepAlive: false
      }
    },
    {
      path: '/suplog',
      name: 'SupLog',
      component: SupLog,
      meta: {
        keepAlive: true
      }
    },
    {
      path: '/envs',
      name: 'Envs',
      component: Envs,
      meta: {
        keepAlive: true
      }
    }
  ]
})
