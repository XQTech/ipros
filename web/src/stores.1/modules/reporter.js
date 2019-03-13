import axios from 'axios'
const BASE_URL = process.env.URL_ROOT
export default {

  state: {
    reporters: []
  },
  mutations: {
    SET_REPORTER (state, data) {
      state.reporters = data
    }
  },
  actions: {
    loadReporter ({commit}) {
      console.log('>>>loading reporter....')
      axios.get(BASE_URL + '/api/sup/reporters/')
        .then(response => {
          console.log(response)
          console.log(response.data)
          commit('SET_REPORTER', response.data)
        })
        .catch(error => {
          console.log(error)
        })
    }
  },
  getters: {
    getReporterById: (state) => (id) => {
      if (!id) {
        return ''
      }
      return state.reporters.find(ct => ct.id === id).name
    }
  }
}
