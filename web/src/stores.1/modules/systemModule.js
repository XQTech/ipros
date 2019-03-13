import axios from 'axios'
const BASE_URL = process.env.URL_ROOT
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
      axios.get(BASE_URL + '/api/sup/systems/')
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
