export default {

  state: {
    reporters: []
  },
  mutations: {
    SET_REPORTER (state, data) {
      state.reporters = data
    }
  },
  actions: {
    loadReporter ({commit}, params) {
      params.self.$http.get('/api/sup/reporters/')
        .then(response => {
          commit('SET_REPORTER', response.data)
        })
        .catch(error => {
          params.self.$message.error(error)
        })
    }
  },
  getters: {
    getReporterById: (state) => (id) => {
      if (!id) {
        return ''
      }
      return state.reporters.find(ct => ct.id === id).name
    }
  }
}
