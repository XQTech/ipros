export default {

  state: {
    functionGroups: []
  },
  mutations: {
    SET_FUNC_GROUP (state, data) {
      state.functionGroups = data
    }
  },
  actions: {
    loadFuncGroup ({commit}, params) {
      params.self.$http.get('/api/funcgroups/')
        .then(response => {
          commit('SET_FUNC_GROUP', response.data)
        })
        .catch(error => {
          params.self.$message.error(error)
        })
    }
  },
  getters: {
    getFuncGroupById: (state) => (id) => {
      if (!id) {
        return ''
      }
      return state.functionGroups.find(fg => fg.id === id).description
    }
  }
}
