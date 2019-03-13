import axios from 'axios'
const BASE_URL = process.env.URL_ROOT
export default {

  state: {
    statusList: []
  },
  mutations: {
    SET_STATUS (state, data) {
      state.statusList = data.results
    }
  },
  actions: {
    loadStatus ({commit}) {
      console.log('>>>loading status....')
      axios.get(BASE_URL + '/api/status/')
        .then(response => {
          console.log(response)
          console.log(response.data)
          commit('SET_STATUS', response.data)
        })
        .catch(error => {
          console.log(error)
        })
    }
  },
  getters: {
    getStatusById: (state) => (id) => {
      if (!id) {
        return ''
      }
      return state.statusList.find(status => status.id === id).code
    }
  }
}
