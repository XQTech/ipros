export default {

  state: {
    ticketList: [],
    totalCount: 0,
    showBreakdown: false,
    selectedTicket: null,
    docList: {}
  },
  mutations: {
    SET_TICKETS (state, data) {
      state.ticketList = data.results
      state.totalCount = data.count
      state.showBreakdown = false
      state.selectedTicket = null
    },
    SET_DOCS (state, data) {
      state.docList = data
    },
    SHOW_BREAKDOWN (state, data) {
      state.showBreakdown = true
      state.selectedTicket = data
    }
  },
  actions: {
    loadTickets ({commit}, params) {
      let url = '/api/tickets/?page=' + params.page
      if (params.keys) {
        for (var key in params.keys) {
          url += '&' + key + '=' + params.keys[key]
        }
      }
      params.self.$http.get(url)
        .then(response => {
          commit('SET_TICKETS', response.data)
        })
        .catch(error => {
          console.log(error)
        })
    },
    loadDocs ({commit}, params) {
      params.self.$http.get('/api/docs/')
        .then(response => {
          commit('SET_DOCS', response.data)
        })
        .catch(error => {
          console.log(error)
        })
    },
    showBreakdown ({commit}, params) {
      commit('SHOW_BREAKDOWN', params.item)
    }
  }
}
