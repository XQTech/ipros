export default {

  state: {
    users: []
  },
  mutations: {
    SET_USERS (state, data) {
      state.users = data
    }
  },
  actions: {
    loadUsers ({commit}, params) {
      console.log('>>>loading users....')
      params.self.$http.get('/api/users/')
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
