import axios from 'axios'

export default {

  state: {
    functionGroups: []
  },
  mutations: {
    SET_FUNC_GROUP (state, data) {
      state.functionGroups = data.results
    }
  },
  actions: {
    loadFuncGroup ({commit}) {
      console.log('>>>loading function group....')
      axios.get('http://localhost:8000/api/funcgroups/')
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
      return state.functionGroups.find(fg => fg.id === id).description
    }
  }
}
