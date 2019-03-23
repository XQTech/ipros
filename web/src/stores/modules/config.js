export default {

  state: {
    configs: []
  },
  mutations: {
    SET_CONFIG (state, data) {
      state.configs = data
    }
  },
  actions: {
    loadConfigs ({commit}, params) {
      params.self.$http.get('/api/common/configs/')
        .then(response => {
          commit('SET_CONFIG', response.data)
        })
        .catch(error => {
          params.self.$message.error(error)
        })
    }
  },
  getters: {
    getConfigByKey: (state) => (id) => {
      if (!id) {
        return ''
      }
      return state.configs.find(ct => ct.key === id).value
    }
  }
}
