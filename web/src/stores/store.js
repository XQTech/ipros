import Vue from 'vue'
import Vuex from 'vuex'
import 'es6-promise/auto'
import axios from 'axios'
import getters from './getters'
import actions from './actions'
import mutations from './mutations'
import modules from './modules'

Vue.prototype.$ajax = axios
Vue.use(Vuex)

export default new Vuex.Store({
  getters,
  actions,
  mutations,
  modules
})
