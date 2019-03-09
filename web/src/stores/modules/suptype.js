import axios from 'axios'

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
    loadSupTypes ({commit}) {
      console.log('>>>loading sup types....')
      axios.get('http://localhost:8000/api/sup/types/')
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
