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
      <el-main>
        <el-breadcrumb separator-class="el-icon-arrow-right">
          <el-breadcrumb-item :to="{ path: '/' }">Home</el-breadcrumb-item>
          <el-breadcrumb-item>Breakdown</el-breadcrumb-item>
          <el-breadcrumb-item>Ticket List</el-breadcrumb-item>
        </el-breadcrumb>
        <div class="button-bar">
          <el-button @click="openBreakdown" type="primary">Breakdown</el-button>
          <el-button @click="editTicket" type="primary">Edit</el-button>
          <el-button @click="deleteTicket" type="danger">Delete</el-button>
        </div>
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
        <el-pagination
          background
          layout="prev, pager, next"
          :total="totalCount"
          @current-change="handleCurrentChange">
        </el-pagination>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
import Aside from './Aside'
import Header from './Header'
import { mapState } from 'vuex'

export default {
  name: 'Home',
  components: {
    Aside,
    Header
  },
  data () {
    return {
      msg: 'Welcome to iPROS management system.',
      logoUrl: './static/img/ipros.png'
    }
  },
  mounted: function () {
    this.$store.dispatch('loadTickets', 1)
  },
  computed: {
    ...mapState({
      ticketList: state => state.ticket.ticketList,
      totalCount: state => state.ticket.totalCount
    })
  },
  methods: {
    handleCurrentChange (page) {
      this.$store.dispatch('loadTickets', page)
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.el-main {
  background-color: #EEF1F4;
}
.button-bar {
  float: right;
  padding-top: 2vh;
  padding-bottom: 1vh;
}
.el-pagination {
  margin-top: 2vh;
}
</style>
