import axios from 'axios'
import { getAccessToken } from '../../../utils/auth'

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
      console.log('updating index : ' + index)
      state.suplogs[index] = suplog
    },
    ADD_SUPLOG (state, suplog) {
      state.suplogs.unshift(suplog)
      console.log('add log id : ' + suplog.id)      
      state.totalCount = state.totalCount + 1
    }
  },
  actions: {
    loadSupLogs ({commit}, params) {
      console.log('>>>loading sup logs....')
      let url = 'http://localhost:8000/api/sup/suplogs/?page=' + params.page
      if (params.keys) {
        for (var key in params.keys) {
          url += '&' + key + '=' + params.keys[key]
        }
      }
      axios.get(url)
        .then(response => {
          console.log(response)
          console.log(response.data)
          commit('SET_SUPLOG', response.data)
        })
        .catch(error => {
          console.log(error)
        })
    },
    createSuplog ({commit, rootState}, suplog) {
      return new Promise((resolve, reject) => {
        console.log('>>>create sup log....')
        axios.post('http://localhost:8000/api/sup/suplogs/', suplog, {
          headers: { 'X-Authorization': 'JWT ' + getAccessToken(),
            'X-CSRFToken': rootState.constants.csrToken
          }})
          .then(response => {
            console.log(response)
            commit('ADD_SUPLOG', response.data)
            resolve()
            // this.loadSuplogs(1)
          })
          .catch(error => {
            reject(error)
          })
      })
    },
    deleteSupLog ({commit, rootState}, id) {
      return new Promise((resolve, reject) => {
        console.log('>>>delete suplog....' + id)
        axios.delete('http://localhost:8000/api/sup/suplogs/' + id + '/', {
          headers: { 'X-Authorization': 'JWT ' + getAccessToken(),
            'X-CSRFToken': rootState.constants.csrToken
          }})
          .then(response => {
            commit('DEL_SUPLOG', id)
            resolve()
          })
          .catch(error => {
            console.log(error.message)
            reject(error)
          })
      })
    },
    updateSuplog ({commit, rootState}, suplog) {
      return new Promise((resolve, reject) => {
        console.log('>>>update sup log....')
        axios.put('http://localhost:8000/api/sup/suplogs/' + suplog.id + '/', suplog, {
          headers: { 'X-Authorization': 'JWT ' + getAccessToken(),
            'X-CSRFToken': rootState.constants.csrToken
          }})
          .then(response => {
            commit('UPD_SUPLOG', suplog)
            resolve()
          })
          .catch(error => {
            reject(error)
          })
      })
    }
  }
}
