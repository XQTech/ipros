<template>
  <el-container>
    <el-container>
      <el-header>
        <el-menu :default-active="activeIndex" mode="horizontal">
          <div class="logo-container">
            <img :src="logoUrl"/>
          </div>
          <el-menu-item index="1" @click="loadTickets">Ticket/Breakdown</el-menu-item>
          <el-menu-item index="2">Support Log</el-menu-item>
          <el-menu-item index="4" @click="handleLogout" style="float:right;">Log Out</el-menu-item>
          <el-menu-item index="3" style="float:right;">
            <a href="http://localhost:8000/admin" target="_blank" style="text-decoration: none;">Admin</a>
          </el-menu-item>
        </el-menu>
      </el-header>
      <Breakdowns v-if="showBreakdown" :selectedTicket="selectedTicket"></Breakdowns>
      <Tickets v-else></Tickets>
    </el-container>
  </el-container>
</template>

<script>
import Tickets from './Tickets'
import Breakdowns from './Breakdowns'
import { mapState } from 'vuex'
import { logout, isLoggedIn, getLoginUser } from '../../utils/auth'

export default {
  name: 'Home',
  components: {
    Tickets,
    Breakdowns
  },
  data () {
    return {
      logoUrl: './static/img/ipros.png',
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
  },
  computed: {
    ...mapState({
      showBreakdown: state => state.ticket.showBreakdown,
      selectedTicket: state => state.ticket.selectedTicket
    })
  },
  methods: {
    handleSelect () {
      console.log('handle select')
    },
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
      let params = {
        keys: null,
        page: this.page
      }
      this.$store.dispatch('loadTickets', params)
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
</style>
