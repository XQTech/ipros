<template>
  <el-container>
    <Aside></Aside>
    <el-container>
      <el-header>
        <el-menu :default-active="activeIndex" mode="horizontal">
          <el-menu-item index="1" @select="handleSelect">My Tasks</el-menu-item>
          <el-menu-item index="2" @select="handleSelect">Messages</el-menu-item>
          <el-menu-item index="3"><a href="http://localhost:8000/admin" target="_blank">Admin</a></el-menu-item>
          <el-menu-item index="4" class="profile"><a href="http://localhost:8000/admin/password_change/" target="_blank">Change Password</a></el-menu-item>
        </el-menu>
      </el-header>
      <Breakdowns v-if="showBreakdown" :selectedTicket="selectedTicket"></Breakdowns>
      <Tickets v-else></Tickets>
    </el-container>
  </el-container>
</template>

<script>
import Aside from './Aside'
import Tickets from './Tickets'
import Breakdowns from './Breakdowns'
import { mapState } from 'vuex'

export default {
  name: 'Home',
  components: {
    Aside,
    Tickets,
    Breakdowns
  },
  data () {
    return {
      msg: 'Welcome to iPROS management system.',
      logoUrl: './static/img/ipros.png',
      activeIndex: '1'
    }
  },
  created: function () {
    this.$store.dispatch('loadFuncGroup')
    this.$store.dispatch('loadStatus')
    this.$store.dispatch('loadCustomers')
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
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
</style>
