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
      console.log('>>>loading sup types....')
      params.self.$http.get('/api/sup/types/')
        .then(response => {
          console.log(response)
          console.log(response.data)
          commit('SET_TYPE', response.data)
        })
        .catch(error => {
          console.log(error)
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
