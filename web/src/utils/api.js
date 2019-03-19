import axios from 'axios'
import { getAccessToken } from './auth'
import store from '../stores/store'

const BASE_URL = process.env.URL_ROOT

export default {
  get (url) {
    return new Promise((resolve, reject) => {
      axios.get(BASE_URL + url, {
        headers: { 'X-Authorization': 'JWT ' + getAccessToken(),
          'X-CSRFToken': store.getters.csrTokenGetter
        }})
        .then(response => {
          console.log(response)
          resolve(response)
        })
        .catch(error => {
          if (error.response === undefined ||
            error.response.data === undefined ||
            error.response.data.detail === undefined) {
            reject(error.message)
          } else if (error.response.data.detail !== undefined) {
            reject(error.response.data.detail)
          }
        })
    })
  },
  post (url, data) {
    return new Promise((resolve, reject) => {
      axios.post(BASE_URL + url, data, {
        headers: { 'X-Authorization': 'JWT ' + getAccessToken(),
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
          }
        })
    })
  },
  put (url, data) {
    return new Promise((resolve, reject) => {
      axios.put(BASE_URL + url, data, {
        headers: { 'X-Authorization': 'JWT ' + getAccessToken(),
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
          }
        })
    })
  },
  putfile (url, data) {
    return new Promise((resolve, reject) => {
      axios.put(BASE_URL + url, data, {
        headers: { 'X-Authorization': 'JWT ' + getAccessToken(),
          'X-CSRFToken': store.getters.csrTokenGetter,
          'Content-Type': 'multipart/form-data'
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
          }
        })
    })
  },
  delete (url) {
    return new Promise((resolve, reject) => {
      axios.delete(BASE_URL + url, {
        headers: { 'X-Authorization': 'JWT ' + getAccessToken(),
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
          }
        })
    })
  }
}
