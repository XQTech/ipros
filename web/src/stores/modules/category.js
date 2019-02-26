import axios from 'axios'

export default {

  state: {
    categories: []
  },
  mutations: {
    SET_CATEGORY (state, data) {
      state.categories = data.results
    }
  },
  actions: {
    loadCustomers ({commit}) {
      console.log('>>>loading category....')
      axios.get('http://localhost:8000/api/categories/')
        .then(response => {
          console.log(response)
          console.log(response.data)
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
      return state.categories.find(ct => ct.id === id).code
    }
  }
}
