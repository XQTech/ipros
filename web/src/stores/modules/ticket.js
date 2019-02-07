import axios from 'axios'

export default {

  state: {
    ticketList: []
  },
  mutations: {
    SET_TICKETS (state, ticketList) {
      state.ticketList = ticketList
    }
  },
  actions: {
    loadTickets ({ commit }) {
      axios.get('http://localhost:8000/breakdown/tickets/')
        .then(response => {
          console.log(response)
          console.log(response.data)
          let ticketList = response.data.results
          commit('SET_TICKETS', ticketList)
        })
        .catch(error => {
          console.log(error)
        })
    }
  }
}
