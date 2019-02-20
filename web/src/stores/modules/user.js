import axios from 'axios'

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
    loadFuncGroup ({commit}) {
      console.log('>>>loading users....')
      axios.get('http://localhost:8000/api/users/')
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
      return state.users.find(user => user.id === id).username
    }
  }
}
