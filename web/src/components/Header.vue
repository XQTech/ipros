<template>
  <div>
    <el-menu :default-active="activeIndex" mode="horizontal">
      <div class="logo-container">
          <img :src="logoUrl"/>
      </div>
      <el-menu-item index="1" @click="loadTickets">Breakdown</el-menu-item>
      <el-menu-item index="2" @click="loadSuplogs">Support Log</el-menu-item>
      <el-menu-item index="5" @click="handleLogout" style="float:right;">Log Out</el-menu-item>
      <el-menu-item index="4" style="float:right;">
          <a href="http://localhost:8000/admin" target="_blank" style="text-decoration: none;">Admin</a>
      </el-menu-item>
      <span style="float:right;margin-top:18px;margin-right:15px;font-style:italic;">Welcome {{getLoginUser()}}</span>
    </el-menu>
  </div>
</template>

<script>
import { logout, isLoggedIn, getLoginUser } from '../../utils/auth'

export default {
  name: 'Header',
  data () {
    return {
      logoUrl: 'static/img/ipros.png',
      activeIndex: '1'
    }
  },
  created: function () {
    if (!isLoggedIn()) {
      this.$router.push({ name: 'Login' })
    }
    this.$store.dispatch('loadFuncGroup')
    this.$store.dispatch('loadStatus')
    this.$store.dispatch('loadCustomers')
    this.$store.dispatch('loadToken')
    this.loadTickets()
  },
  methods: {
    isLoggedIn () {
      return isLoggedIn()
    },
    getLoginUser () {
      return getLoginUser()
    },
    handleLogout () {
      logout()
      this.$router.push({ name: 'Login' })
    },
    loadTickets () {
      this.$router.push({ name: 'Home' })
    },
    loadSuplogs () {
      let params = {
        keys: null,
        page: 1
      }
      this.$store.dispatch('loadCustomers')
      this.$store.dispatch('loadReporter')
      this.$store.dispatch('loadSupStatus')
      this.$store.dispatch('loadSupTypes')
      this.$store.dispatch('loadModules')
      this.$store.dispatch('loadUsers')
      this.$store.dispatch('loadSupLogs', params)
      this.$router.push({ name: 'SupLog' })
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
</style>
