
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
      params.self.$http.get('/api/sup/statuss/')
        .then(response => {
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
