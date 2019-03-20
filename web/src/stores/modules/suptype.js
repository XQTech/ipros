export default {

  state: {
    suptypes: []
  },
  mutations: {
    SET_TYPE (state, data) {
      state.suptypes = data
    }
  },
  actions: {
    loadSupTypes ({commit}, params) {
      params.self.$http.get('/api/sup/types/')
        .then(response => {
          commit('SET_TYPE', response.data)
        })
        .catch(error => {
          params.self.$message.error(error)
        })
    }
  },
  getters: {
    getTypeById: (state) => (id) => {
      if (!id) {
        return ''
      }
      return state.suptypes.find(ct => ct.id === id).name
    }
  }
}
