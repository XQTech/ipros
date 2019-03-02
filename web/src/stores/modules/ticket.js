import axios from 'axios'

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
      console.log('total Tickets: ' + state.totalCount)
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
      console.log('>>>loading ticket....')
      let url = 'http://localhost:8000/api/tickets/?page=' + params.page
      if (params.keys) {
        for (var key in params.keys) {
          url += '&' + key + '=' + params.keys[key]
        }
      }
      axios.get(url)
        .then(response => {
          console.log(response)
          console.log(response.data)
          commit('SET_TICKETS', response.data)
        })
        .catch(error => {
          console.log(error)
        })
    },
    loadDocs ({commit}, params) {
      console.log('>>>loading docs....')
      axios.get('http://localhost:8000/api/docs/')
        .then(response => {
          console.log('docs list.............')
          console.log(response)
          console.log(response.data)
          commit('SET_DOCS', response.data)
        })
        .catch(error => {
          console.log(error)
        })
    },
    showBreakdown ({commit}, selectedTicket) {
      commit('SHOW_BREAKDOWN', selectedTicket)
    }
  }
}
