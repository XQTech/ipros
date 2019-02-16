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
    loadTickets ({commit}, page) {
      console.log('>>>loading ticket....')
      axios.get('http://localhost:8000/breakdown/tickets/?page=' + page)
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
