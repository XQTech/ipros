<template>
  <el-container>
    <el-aside width="180px">
      <div class="logo-container">
        <img :src="logoUrl"/>
      </div>
      <div>
        <el-menu
          default-active="2"
          background-color="#545c64"
          text-color="#fff"
          active-text-color="#ffd04b">
          <el-menu-item index="1">
            <span slot="title">FD & Breakdown</span>
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
    <el-container>
      <el-header>
        <el-menu :default-active="activeIndex" mode="horizontal">
          <el-menu-item index="1" @select="handleSelect">My Tasks</el-menu-item>
          <el-menu-item index="2" @select="handleSelect">Messages</el-menu-item>
          <el-menu-item index="3"><a href="http://localhost:8000/admin" target="_blank">Admin</a></el-menu-item>
          <el-menu-item index="4" class="profile"><a href="http://localhost:8000/admin/password_change/" target="_blank">Change Password</a></el-menu-item>
        </el-menu>
        <div class="line"></div>
      </el-header>
      <el-main>
        <el-breadcrumb separator-class="el-icon-arrow-right">
          <el-breadcrumb-item :to="{ path: '/' }">Home</el-breadcrumb-item>
          <el-breadcrumb-item>Breakdown</el-breadcrumb-item>
          <el-breadcrumb-item>Ticket List</el-breadcrumb-item>
        </el-breadcrumb>
        <el-button @click="resetDateFilter">清除日期过滤器</el-button>
        <el-button @click="clearFilter">清除所有过滤器</el-button>
        <el-table
          ref="filterTable"
          :data="ticketList"
          style="width: 100%">
          <el-table-column
            prop="ticket_no"
            label="Ticket No"
            sortable
            width="120">
          </el-table-column>
          <el-table-column
            prop="customer"
            label="Customer"
            width="100">
          </el-table-column>
          <el-table-column
            prop="assigned_user"
            label="Assigned To"
            width="120">
          </el-table-column>
          <el-table-column
            prop="description"
            label="Description">
          </el-table-column>
          <el-table-column
            prop="create_user"
            label="Created By"
            width="100">
          </el-table-column>
        </el-table>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
import { mapState } from 'vuex'

export default {
  name: 'Home',
  data () {
    return {
      msg: 'Welcome to iPROS management system.',
      logoUrl: './static/img/ipros.png'
    }
  },
  mounted: function () {
    this.$store.dispatch('loadTickets')
  },
  computed: {
    ...mapState({
      ticketList: state => state.ticket.ticketList
    })
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
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
.el-main {
  background-color: #EEF1F4;
}
.el-menu-item {
  text-align: left;
}
.profile {
  align-content: flex-end;
}
</style>
