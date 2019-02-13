<template>
  <el-aside width="180px">
      <div class="logo-container">
        <img :src="logoUrl"/>
      </div>
      <div>
        <el-menu
          default-active="1"
          background-color="#545c64"
          text-color="#fff"
          active-text-color="#ffd04b">
          <el-menu-item index="1">
            <span slot="title" @click="loadTickets">Ticket List</span>
          </el-menu-item>
          <el-menu-item index="2">
            <span slot="title">Support Log</span>
          </el-menu-item>
          <el-menu-item index="3">
            <span slot="title">Todo List</span>
          </el-menu-item>
          <el-menu-item index="4">
            <span slot="title">Reports</span>
          </el-menu-item>
        </el-menu>
      </div>
    </el-aside>
</template>

<script>

export default {
  name: 'Aside',
  data () {
    return {
      logoUrl: './static/img/ipros.png'
    }
  },
  methods: {
    loadTickets () {
      this.$store.dispatch('loadTickets', 1)
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.el-aside {
  background-color: #545c64;
  color: white;
  min-height: 100vh;
}
.el-menu {
  border-right: 0 !important;
}
.logo-container {
  background-color: #003781;
  min-height:12vh;
}
</style>
