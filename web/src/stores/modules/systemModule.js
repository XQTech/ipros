import axios from 'axios'

export default {

  state: {
    modules: []
  },
  mutations: {
    SET_MODULE (state, data) {
      state.modules = data
    }
  },
  actions: {
    loadModules ({commit}) {
      console.log('>>>loading modules....')
      axios.get('http://localhost:8000/api/sup/systems/')
        .then(response => {
          console.log(response.data)
          commit('SET_MODULE', response.data)
        })
        .catch(error => {
          console.log(error)
        })
    }
  },
  getters: {
    getModuleById: (state) => (id) => {
      if (!id) {
        return ''
      }
      return state.modules.find(ct => ct.id === id).name
    }
  }
}
