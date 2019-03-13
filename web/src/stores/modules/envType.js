export default {

  state: {
    envTypes: []
  },
  mutations: {
    SET_ENVTYPE (state, data) {
      state.envTypes = data
    }
  },
  actions: {
    loadEnvTypes ({commit}, params) {
      params.self.$http.get('/api/envs/types/')
        .then(response => {
          commit('SET_ENVTYPE', response.data)
        })
        .catch(error => {
          console.log(error)
        })
    }
  },
  getters: {
    getEnvTypeById: (state) => (id) => {
      if (!id) {
        return ''
      }
      return state.envTypes.find(ct => ct.id === id).name
    }
  }
}
