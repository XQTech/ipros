'use strict'
const merge = require('webpack-merge')
const prodEnv = require('./prod.env')

module.exports = merge(prodEnv, {
  NODE_ENV: '"development"',
  URL_ROOT: '"http://localhost:8000"',
  IMG_ROOT: '"../../static/img"'
})
