import axios from 'axios'
const BASE_URL = process.env.URL_ROOT
export default {

  state: {
    users: []
  },
  mutations: {
    SET_USERS (state, data) {
      state.users = data.results
    }
  },
  actions: {
    loadUsers ({commit}) {
      console.log('>>>loading users....')
      axios.get(BASE_URL + '/api/users/')
        .then(response => {
          console.log(response)
          console.log(response.data)
          commit('SET_USERS', response.data)
        })
        .catch(error => {
          console.log(error)
        })
    }
  },
  getters: {
    getUserById: (state) => (id) => {
      if (!id) {
        return ''
      }
      return state.users.find(user => user.id === id).username
    }
  }
}
