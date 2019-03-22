import axios from 'axios'
import { getAccessToken } from './auth'
import store from '../stores/store'

const BASE_URL = process.env.URL_ROOT

export default {
  get (url) {
    return new Promise((resolve, reject) => {
      axios.get(BASE_URL + url, {
        headers: { 'Authorization': 'JWT ' + getAccessToken(),
          'X-CSRFToken': store.getters.csrTokenGetter
        }})
        .then(response => {
          resolve(response)
        })
        .catch(error => {
          if (error.response === undefined ||
            error.response.data === undefined ||
            error.response.data.detail === undefined) {
            reject(error.message)
          } else if (error.response.data.detail !== undefined) {
            reject(error.response.data.detail)
          } else if (error.response.data.solution !== undefined) {
            reject(error.response.data.solution)
          }
        })
    })
  },
  post (url, data) {
    return new Promise((resolve, reject) => {
      axios.post(BASE_URL + url, data, {
        headers: { 'Authorization': 'JWT ' + getAccessToken(),
          'X-CSRFToken': store.getters.csrTokenGetter
        }})
        .then(response => {
          resolve(response)
        })
        .catch(error => {
          if (error.response === undefined ||
            error.response.data === undefined ||
            (error.response.data.detail === undefined &&
              error.response.data.solution === undefined)) {
            reject(error.message)
          } else if (error.response.data.detail !== undefined) {
            reject(error.response.data.detail)
          } else if (error.response.data.solution !== undefined) {
            reject(error.response.data.solution)
          }
        })
    })
  },
  put (url, data) {
    return new Promise((resolve, reject) => {
      axios.put(BASE_URL + url, data, {
        headers: { 'Authorization': 'JWT ' + getAccessToken(),
          'X-CSRFToken': store.getters.csrTokenGetter
        }})
        .then(response => {
          resolve(response)
        })
        .catch(error => {
          if (error.response === undefined ||
            error.response.data === undefined ||
            (error.response.data.detail === undefined &&
              error.response.data.solution === undefined)) {
            reject(error.message)
          } else if (error.response.data.detail !== undefined) {
            reject(error.response.data.detail)
          } else if (error.response.data.solution !== undefined) {
            reject(error.response.data.solution)
          }
        })
    })
  },
  putfile (url, data) {
    return new Promise((resolve, reject) => {
      axios.put(BASE_URL + url, data, {
        headers: { 'Authorization': 'JWT ' + getAccessToken(),
          'X-CSRFToken': store.getters.csrTokenGetter,
          'Content-Type': 'multipart/form-data'
        }})
        .then(response => {
          resolve(response)
        })
        .catch(error => {
          if (error.response === undefined ||
            error.response.data === undefined ||
            (error.response.data.detail === undefined &&
              error.response.data.solution === undefined)) {
            reject(error.message)
          } else if (error.response.data.detail !== undefined) {
            reject(error.response.data.detail)
          } else if (error.response.data.solution !== undefined) {
            reject(error.response.data.solution)
          }
        })
    })
  },
  delete (url, data) {
    return new Promise((resolve, reject) => {
      axios.delete(BASE_URL + url, {
        params: data,
        headers: { 'Authorization': 'JWT ' + getAccessToken(),
          'X-CSRFToken': store.getters.csrTokenGetter
        }})
        .then(response => {
          resolve(response)
        })
        .catch(error => {
          if (error.response === undefined ||
            error.response.data === undefined ||
            (error.response.data.detail === undefined &&
              error.response.data.solution === undefined)) {
            reject(error.message)
          } else if (error.response.data.detail !== undefined) {
            reject(error.response.data.detail)
          } else if (error.response.data.solution !== undefined) {
            reject(error.response.data.solution)
          }
        })
    })
  }
}
