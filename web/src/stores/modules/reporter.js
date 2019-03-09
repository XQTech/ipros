import axios from 'axios'

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
      axios.get('http://localhost:8000/api/sup/reporters/')
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
