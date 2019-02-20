import axios from 'axios'

export default {

  state: {
    ticketList: [],
    totalCount: 0,
    showBreakdown: false,
    selectedTicket: null
  },
  mutations: {
    SET_TICKETS (state, data) {
      state.ticketList = data.results
      state.totalCount = data.count
      console.log('total Tickets: ' + state.totalCount)
      state.showBreakdown = false
      state.selectedTicket = null
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
    showBreakdown ({commit}, selectedTicket) {
      commit('SHOW_BREAKDOWN', selectedTicket)
    }
  }
}
