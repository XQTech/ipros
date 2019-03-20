/*
 * This file is based on:
 * https://auth0.com/blog/vuejs2-authentication-tutorial/
 * Rewritten by Stein Roald Bolle, December 2017, for Django REST and JWT.
*/

import decode from 'jwt-decode'
import axios from 'axios'
const ACCESS_TOKEN_KEY = 'access_token'
const USER_NAME = 'username'
const USER_ID = 'user_id'

const BACKEND_URL = process.env.URL_ROOT
// const REDIRECT_URL_AFTER_LOGIN = '/'

export function login (username, password) {
  const url = `${BACKEND_URL}/api-token-auth/`
  axios.post(url, { username: username, password: password })
    .then(function (response) {
      console.log(response)
      localStorage.setItem(ACCESS_TOKEN_KEY, response.data.token)
      localStorage.setItem(USER_NAME, response.data.username)
      localStorage.setItem(USER_ID, response.data.user_id)
    })
    .catch(function (error) {
      console.log(error)
    })
}

export function logout () {
  clearAccessToken()
}

export function requireAuth (to, from, next) {
  if (!isLoggedIn()) {
    next({
      path: '/',
      query: { redirect: to.fullPath }
    })
  } else {
    next()
  }
}

export function getAccessToken () {
  return localStorage.getItem(ACCESS_TOKEN_KEY)
}

export function getLoginUser () {
  return {
    'username': localStorage.getItem(USER_NAME),
    'id': parseInt(localStorage.getItem(USER_ID))
  }
}

function clearAccessToken () {
  localStorage.removeItem(ACCESS_TOKEN_KEY)
}

export function isLoggedIn () {
  const accessToken = getAccessToken()
  return !!accessToken && !isTokenExpired(accessToken)
}

function getTokenExpirationDate (encodedToken) {
  const token = decode(encodedToken)
  if (!token.exp) { return null }

  const date = new Date(0)
  date.setUTCSeconds(token.exp)

  return date
}

function isTokenExpired (token) {
  const expirationDate = getTokenExpirationDate(token)
  return expirationDate < new Date()
}
