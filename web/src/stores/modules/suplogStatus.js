import axios from 'axios'

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
      axios.get('http://localhost:8000/api/sup/statuss/')
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
