
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
    loadSupStatus ({commit}, params) {
      console.log('>>>loading status....')
      params.self.$http.get('/api/sup/statuss/')
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
