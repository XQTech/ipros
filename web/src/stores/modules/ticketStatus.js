export default {

  state: {
    statusList: []
  },
  mutations: {
    SET_STATUS (state, data) {
      state.statusList = data
    }
  },
  actions: {
    loadStatus ({commit}, params) {
      params.self.$http.get('/api/status/')
        .then(response => {
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
