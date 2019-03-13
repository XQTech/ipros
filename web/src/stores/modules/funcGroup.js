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
      console.log('>>>loading function group....')
      console.log(self.$http)
      params.self.$http.get('/api/funcgroups/')
        .then(response => {
          console.log(response)
          console.log(response.data)
          commit('SET_FUNC_GROUP', response.data)
        })
        .catch(error => {
          console.log(error)
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
