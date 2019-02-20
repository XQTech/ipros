import axios from 'axios'

export default {

  state: {
    customers: []
  },
  mutations: {
    SET_CUSTOMER (state, data) {
      state.customers = data.results
    }
  },
  actions: {
    loadCustomers ({commit}) {
      console.log('>>>loading customers....')
      axios.get('http://localhost:8000/api/customers/')
        .then(response => {
          console.log(response)
          console.log(response.data)
          commit('SET_CUSTOMER', response.data)
        })
        .catch(error => {
          console.log(error)
        })
    }
  },
  getters: {
    getCustomerById: (state) => (id) => {
      return state.customers.find(ct => ct.id === id).name
    }
  }
}
