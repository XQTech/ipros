import axios from 'axios'
const BASE_URL = process.env.URL_ROOT
export default {

  state: {
    supStatusList: []
  },
  mutations: {
    SET_SUP_STATUS (state, data) {
      state.supStatusList = data
    }
  },
  actions: {
    loadSupStatus ({commit}) {
      console.log('>>>loading status....')
      axios.get(BASE_URL + '/api/sup/statuss/')
        .then(response => {
          console.log(response)
          console.log(response.data)
          commit('SET_SUP_STATUS', response.data)
        })
        .catch(error => {
          console.log(error)
        })
    }
  },
  getters: {
    getSupStatusById: (state) => (id) => {
      if (!id) {
        return ''
      }
      return state.supStatusList.find(status => status.id === id).name
    }
  }
}
