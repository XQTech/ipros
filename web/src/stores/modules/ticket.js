import axios from 'axios'

export default {

  state: {
    ticketList: [],
    totalCount: 0
  },
  mutations: {
    SET_TICKETS (state, data) {
      state.ticketList = data.results
      state.totalCount = data.count
      console.log('total Tickets: ' + state.totalCount)
    }
  },
  actions: {
    loadTickets ({commit}, page) {
      axios.get('http://localhost:8000/breakdown/tickets/?page=' + page)
        .then(response => {
          console.log(response)
          console.log(response.data)
          commit('SET_TICKETS', response.data)
        })
        .catch(error => {
          console.log(error)
        })
    }
  }
}
