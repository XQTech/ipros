import axios from 'axios'
import { getAccessToken } from './auth'

const BASE_URL = 'http://localhost:8000'

export function getPrivateUsers () {
  var token = getAccessToken()
  const url = `${BASE_URL}/users/`
  axios.defaults.headers.common['Authorization'] = 'JWT ' + token
  return axios.get(url)
    .then(response => response.data)
}
