<template>
  <el-main>
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/' }">Home</el-breadcrumb-item>
      <el-breadcrumb-item>Ticket List</el-breadcrumb-item>
    </el-breadcrumb>
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
        prop="customer.name"
        label="Customer"
        width="100">
      </el-table-column>
      <el-table-column
        prop="assigned_user.username"
        label="Assigned To"
        width="120">
      </el-table-column>
      <el-table-column
        prop="description"
        label="Description">
      </el-table-column>
      <el-table-column
        prop="status.code"
        label="Status"
        width="80">
      </el-table-column>
      <el-table-column
        prop="create_user"
        label="Created By"
        width="100">
      </el-table-column>
      <el-table-column label="Action" width="200">
        <template slot-scope="scope">
          <el-button
            size="mini"
            @click="handleBreakdown(scope.row)">Breakdown</el-button>
          <el-button
            size="mini"
            type="danger"
            @click="handleDelete(scope.row)">Delete</el-button>
        </template>
      </el-table-column>
    </el-table>
    <el-pagination
      background
      layout="prev, pager, next"
      :total="totalCount"
      @current-change="handleCurrentChange">
    </el-pagination>
  </el-main>
</template>

<script>
import { mapState } from 'vuex'

export default {
  name: 'Tickets',
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
    },
    handleBreakdown (ticket) {
      console.log('ticket no: ' + ticket.ticket_no)
      console.log('breakdown: ' + ticket.breakdowns)
      this.$store.dispatch('showBreakdown', ticket)
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
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
.el-breadcrumb {
  margin-bottom: 2vh;
}
</style>
