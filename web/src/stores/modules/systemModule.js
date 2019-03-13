export default {

  state: {
    modules: []
  },
  mutations: {
    SET_MODULE (state, data) {
      state.modules = data
    }
  },
  actions: {
    loadModules ({commit}, params) {
      params.self.$http.get('/api/common/systems/')
        .then(response => {
          commit('SET_MODULE', response.data)
        })
        .catch(error => {
          console.log(error)
        })
    }
  },
  getters: {
    getModuleById: (state) => (id) => {
      if (!id) {
        return ''
      }
      return state.modules.find(ct => ct.id === id).name
    }
  }
}
