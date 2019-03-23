
import Vue from 'vue'
export default {

  state: {
    envItems: []
  },
  mutations: {
    SET_ENVITEM (state, data) {
      state.envItems = data
    },
    DEL_ENVITEM (state, id) {
      state.envItems = state.envItems.filter(item => item.id !== id)
    },
    UPD_ENVITEM (state, envitem) {
      let index = state.envItems.findIndex(item => item.id === envitem.id)
      Vue.set(state.envItems, index, envitem)
    },
    ADD_ENVITEM (state, envitem) {
      state.envItems.unshift(envitem)
      state.envItems.sort(function (a, b) {
        if (a.customer < b.customer) {
          return -1
        } else if (a.customer > b.customer) {
          return 1
        } else if (a.envtype < b.envtype) {
          return -1
        } else if (a.envtype > b.envtype) {
          return 1
        } else if (a.name < b.name) {
          return -1
        } else if (a.name > b.name) {
          return 1
        }
        return 0
      })
    }
  },
  actions: {
    loadEnvItems ({commit}, params) {
      let url = '/api/envs/items/'
      if (params.keys) {
        let i = 0
        for (var key in params.keys) {
          i += 1
          if (i === 1) {
            url += '?'
          } else {
            url += '&'
          }
          url += key + '=' + params.keys[key]
        }
      }
      params.self.$http.get(url)
        .then(response => {
          commit('SET_ENVITEM', response.data)
        })
        .catch(error => {
          params.self.$message.error(error)
        })
    },
    createEnvItem ({commit}, params) {
      return new Promise((resolve, reject) => {
        params.self.$http.post('/api/envs/items/', params.item)
          .then(response => {
            commit('ADD_ENVITEM', response.data)
            resolve(response)
          })
          .catch(error => {
            reject(error)
          })
      })
    },
    deleteEnvItem ({commit}, params) {
      return new Promise((resolve, reject) => {
        params.self.$http.delete('/api/envs/items/' + params.id + '/')
          .then(response => {
            commit('DEL_ENVITEM', params.id)
            resolve(response)
          })
          .catch(error => {
            reject(error)
          })
      })
    },
    updateEnvItem ({commit}, params) {
      return new Promise((resolve, reject) => {
        params.self.$http.put('/api/envs/items/' + params.item.id + '/', params.item)
          .then(response => {
            commit('UPD_ENVITEM', response.data)
            resolve(response)
          })
          .catch(error => {
            reject(error)
          })
      })
    }
  }
}
