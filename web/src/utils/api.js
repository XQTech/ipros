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
          resolve(response)
        })
        .catch(error => {
          reject(error)
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
          reject(error)
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
          reject(error)
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
          reject(error)
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
          reject(error)
        })
    })
  }
}
