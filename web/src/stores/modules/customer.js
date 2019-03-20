export default {

  state: {
    customers: []
  },
  mutations: {
    SET_CUSTOMER (state, data) {
      state.customers = data
    }
  },
  actions: {
    loadCustomers ({commit}, params) {
      params.self.$http.get('/api/common/customers/')
        .then(response => {
          commit('SET_CUSTOMER', response.data)
        })
        .catch(error => {
          params.self.$message.error(error)
        })
    }
  },
  getters: {
    getCustomerById: (state) => (id) => {
      if (!id) {
        return ''
      }
      return state.customers.find(ct => ct.id === id).name
    }
  }
}
