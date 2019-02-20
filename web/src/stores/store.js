import Vue from 'vue'
import Vuex from 'vuex'
import 'es6-promise/auto'
import axios from 'axios'
import getters from './getters'
import actions from './actions'
import mutations from './mutations'
import ticket from './modules/ticket'
import ticketStatus from './modules/ticket-status'
import funcGroups from './modules/func-group'
import customer from './modules/customer'
import user from './modules/user'
import constants from './constants'

Vue.prototype.$ajax = axios
Vue.use(Vuex)

export default new Vuex.Store({
  getters,
  actions,
  mutations,
  modules: {
    ticket,
    ticketStatus,
    funcGroups,
    customer,
    user,
    constants
  }
})
