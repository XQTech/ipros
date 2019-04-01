<template>
  <div>
    <el-menu :default-active="activeIndex" mode="horizontal">
      <div class="logo-container">
          <img :src="logoUrl"/>
      </div>
      <el-menu-item index="1" @click="loadTickets">
        <template>
          <i class="el-icon-tickets"></i>
          <span>Breakdown</span>
        </template>
      </el-menu-item>
      <el-menu-item index="2" @click="loadSuplogs">
        <template>
          <i class="el-icon-phone-outline"></i>
          <span>Support Log</span>
        </template>
      </el-menu-item>
      <el-menu-item index="3" @click="loadEnvs">
        <template>
          <i class="fa fa-server"></i>
          <span>Environment</span>
        </template>
      </el-menu-item>
      <el-menu-item index="5" @click="handleLogout" style="float:right;">Log Out</el-menu-item>
      <el-menu-item index="4" style="float:right;">
          <a :href="admin_rul" target="_blank" style="text-decoration: none;">Admin</a>
      </el-menu-item>
      <span class="welcome">Welcome {{getLoginUser()}}</span>
    </el-menu>
  </div>
</template>

<script>
import { logout, isLoggedIn, getLoginUser } from '../utils/auth'
const BASE_URL = process.env.URL_ROOT
export default {
  name: 'Header',
  data () {
    return {
      logoUrl: './static/img/ipros.png',
      activeIndex: '1',
      admin_rul: BASE_URL + '/admin',
      params: {
        self: this,
        keys: null,
        page: 1
      }
    }
  },
  created: function () {
    if (!isLoggedIn()) {
      this.$router.push({ name: 'Login' })
    }
    this.$store.dispatch('loadToken')
    this.$store.dispatch('loadFuncGroup', this.params)
    this.$store.dispatch('loadStatus', this.params)
    this.$store.dispatch('loadCustomers', this.params)
    this.$store.dispatch('loadUsers', this.params)
    this.$store.dispatch('loadConfigs', this.params)
    this.loadTickets()
  },
  methods: {
    isLoggedIn () {
      return isLoggedIn()
    },
    getLoginUser () {
      return getLoginUser().username
    },
    handleLogout () {
      logout()
      this.$router.push({ name: 'Login' })
    },
    loadTickets () {
      this.$router.push({ name: 'Home' })
    },
    loadSuplogs () {
      this.$store.dispatch('loadCustomers', this.params)
      this.$store.dispatch('loadReporter', this.params)
      this.$store.dispatch('loadSupStatus', this.params)
      this.$store.dispatch('loadSupTypes', this.params)
      this.$store.dispatch('loadModules', this.params)
      this.$store.dispatch('loadUsers', this.params)
      this.$store.dispatch('loadSupLogs', this.params)
      this.$router.push({ name: 'SupLog' })
    },
    loadEnvs () {
      this.$store.dispatch('loadCustomers', this.params)
      this.$store.dispatch('loadEnvItems', this.params)
      this.$store.dispatch('loadEnvTypes', this.params)
      this.$router.push({ name: 'Envs' })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
.logo-container {
  float: left;
  margin-right:30px;
}
.button-bar {
  float: right;
  padding-bottom: 1vh;
}
.el-pagination {
  margin-top: 2vh;
  float: right;
}
.el-breadcrumb {
  margin-bottom: 2vh;
}
.welcome {
  float:right;
  margin-top:20px;
  margin-right:20px;
  font-size: 14px;
  color: #606266;
}
.el-textarea__inner {
  word-break: keep-all;
  word-wrap: break-word;
}
</style>
