export default {

  state: {
    categories: []
  },
  mutations: {
    SET_CATEGORY (state, data) {
      state.categories = data
    }
  },
  actions: {
    loadCustomers ({commit}, params) {
      params.self.$http.get('/api/categories/')
        .then(response => {
          commit('SET_CATEGORY', response.data)
        })
        .catch(error => {
          console.log(error)
        })
    }
  },
  getters: {
    getCategoryById: (state) => (id) => {
      if (!id) {
        return ''
      }
      return state.categories.find(ct => ct.id === id)
    }
  }
}
