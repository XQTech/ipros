export default {
  state: {
    csrToken: ''
  },
  mutations: {
    SET_TOKEN (state, data) {
      state.csrToken = data
      console.log(data)
    }
  },
  actions: {
    loadToken ({commit}) {
      console.log('load token..............')
      var value = '; ' + document.cookie
      var parts = value.split('; csrftoken=')
      if (parts.length === 2) {
        commit('SET_TOKEN', parts.pop().split(';').shift())
      }
    }
  },
  getters: {
    csrTokenGetter: state => state.csrToken
  }
}
