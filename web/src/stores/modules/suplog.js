
import Vue from 'vue'
export default {

  state: {
    suplogs: [],
    totalCount: 0
  },
  mutations: {
    SET_SUPLOG (state, data) {
      state.suplogs = data.results
      state.totalCount = data.count
    },
    DEL_SUPLOG (state, id) {
      state.suplogs = state.suplogs.filter(item => item.id !== id)
      state.totalCount = state.totalCount - 1
    },
    UPD_SUPLOG (state, suplog) {
      let index = state.suplogs.findIndex(item => item.id === suplog.id)
      Vue.set(state.suplogs, index, suplog)
    },
    ADD_SUPLOG (state, suplog) {
      state.suplogs.unshift(suplog)
      state.totalCount = state.totalCount + 1
    }
  },
  actions: {
    loadSupLogs ({commit}, params) {
      let url = '/api/sup/suplogs/?page=' + params.page
      if (params.keys) {
        for (var key in params.keys) {
          url += '&' + key + '=' + params.keys[key]
        }
      }
      params.self.$http.get(url)
        .then(response => {
          commit('SET_SUPLOG', response.data)
        })
        .catch(error => {
          console.log(error)
        })
    },
    createSuplog ({commit}, params) {
      return new Promise((resolve, reject) => {
        params.self.$http.post('/api/sup/suplogs/', params.item)
          .then(response => {
            commit('ADD_SUPLOG', response.data)
            resolve(response)
          })
          .catch(error => {
            reject(error)
          })
      })
    },
    deleteSupLog ({commit}, params) {
      return new Promise((resolve, reject) => {
        params.self.$http.delete('/api/sup/suplogs/' + params.id + '/')
          .then(response => {
            commit('DEL_SUPLOG', params.id)
            resolve(response)
          })
          .catch(error => {
            console.log(error)
            reject(error)
          })
      })
    },
    updateSuplog ({commit}, params) {
      return new Promise((resolve, reject) => {
        params.self.$http.put('/api/sup/suplogs/' + params.item.id + '/', params.item)
          .then(response => {
            commit('UPD_SUPLOG', response.data)
            resolve(response)
          })
          .catch(error => {
            reject(error)
          })
      })
    }
  }
}
