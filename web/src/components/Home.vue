<template>
  <Breakdowns v-if="showBreakdown" :selectedTicket="selectedTicket"></Breakdowns>
  <Tickets v-else></Tickets>
</template>

<script>
import Tickets from './Tickets'
import Breakdowns from './Breakdowns'
import { mapState } from 'vuex'
import { logout, isLoggedIn, getLoginUser } from '../utils/auth'

export default {
  name: 'Home',
  components: {
    Tickets,
    Breakdowns
  },
  data () {
    return {
      logoUrl: './static/img/ipros.png',
      activeIndex: '1',
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
    this.$store.dispatch('loadUsers', this.params)
  },
  computed: {
    ...mapState({
      showBreakdown: state => state.ticket.showBreakdown,
      selectedTicket: state => state.ticket.selectedTicket
    })
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
      this.$store.dispatch('loadDocs', this.params)
      this.$store.dispatch('loadTickets', this.params)
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
