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
      console.log('>>>loading reporter....')
      params.self.$http.get('/api/sup/reporters/')
        .then(response => {
          console.log(response)
          console.log(response.data)
          commit('SET_REPORTER', response.data)
        })
        .catch(error => {
          console.log(error)
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
