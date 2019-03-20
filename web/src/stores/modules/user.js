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
      params.self.$http.get('/api/users/')
        .then(response => {
          commit('SET_USERS', response.data)
        })
        .catch(error => {
          params.self.$message.error(error)
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
