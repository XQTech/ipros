import Vue from 'vue'

export default {

  state: {
    breakdowns: []
  },
  mutations: {
    SET_BREAKDOWNS (state, data) {
      state.breakdowns = data
    },
    DEL_BREAKDOWN (state, id) {
      state.breakdowns = state.breakdowns.filter(item => item.id !== id)
    },
    UPD_BREAKDOWN (state, breakdown) {
      let index = state.breakdowns.findIndex(item => item.id === breakdown.id)
      Vue.set(state.breakdowns, index, breakdown)
    },
    ADD_BREAKDOWN (state, breakdown) {
      state.breakdowns.unshift(breakdown)
      state.breakdowns.sort(function (a, b) {
        return a.sequence - b.sequence
      })
    }
  },
  actions: {
    loadBreakdowns ({commit}, params) {
      params.self.$http.get('/api/breakdowns/' + params.id + '/breakdowns/')
        .then(response => {
          commit('SET_BREAKDOWNS', response.data)
        })
        .catch(error => {
          this.$message.error(error)
        })
    },
    deleteBreakdown ({commit}, params) {
      return new Promise((resolve, reject) => {
        params.self.$http.delete('/api/breakdowns/' + params.id + '/')
          .then(response => {
            commit('DEL_BREAKDOWN', params.id)
            resolve(response)
          })
          .catch(error => {
            reject(error)
          })
      })
    },
    updateBreakdown ({commit}, params) {
      return new Promise((resolve, reject) => {
        params.self.$http.put('/api/breakdowns/' + params.item.id + '/', params.item)
          .then(response => {
            commit('UPD_BREAKDOWN', response.data)
            resolve(response)
          })
          .catch(error => {
            reject(error)
          })
      })
    },
    createBreakdown ({commit}, params) {
      return new Promise((resolve, reject) => {
        params.self.$http.post('/api/breakdowns/', params.item)
          .then(response => {
            commit('ADD_BREAKDOWN', response.data)
            resolve(response)
          })
          .catch(error => {
            reject(error)
          })
      })
    }
  }
}
