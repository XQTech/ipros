import axios from 'axios'
const api = {
  async get (url, data, header) {
    try {
      let res = await axios.get(url, JSON.stringify(data), {headers: header})
      res = res.data
      console.log('in api, geting data....')
      console.log(header)
      return new Promise((resolve) => {
        resolve(res)
      })
    } catch (err) {
      console.log(err)
    }
  },
  async post (url, data, header) {
    try {
      console.log('posting data...............')
      console.log(JSON.stringify(data))
      let res = await axios.post(url, data, {headers: header})
      res = res.data
      return new Promise((resolve, reject) => {
        if (res.code === 0) {
          resolve(res)
        } else {
          reject(res)
        }
      })
    } catch (err) {
      console.log(err)
    }
  },
  async put (url, data, header) {
    try {
      console.log('putting data...............')
      console.log(JSON.stringify(data))
      let res = await axios.put(url, data, {headers: header})
      res = res.data
      console.log(res)
      return new Promise((resolve, reject) => {
        if (res.code === 0) {
          resolve(res)
        } else {
          reject(res)
        }
      })
    } catch (err) {
      console.log(err)
    }
  }
}
export { api }
