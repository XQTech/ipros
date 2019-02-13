<template>
  <el-main>
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/' }" @click.native="goHome">Home</el-breadcrumb-item>
      <el-breadcrumb-item>Ticket List</el-breadcrumb-item>
      <el-breadcrumb-item>Breakdown</el-breadcrumb-item>
      <el-breadcrumb-item>{{ selectedTicket.ticket_no }}</el-breadcrumb-item>
    </el-breadcrumb>
    <el-table
      ref="filterTable"
      :data="selectedTicket.breakdowns"
      style="width: 100%">
      <el-table-column
        prop="function_group.description"
        label="Function"
        sortable
        width="150">
      </el-table-column>
      <el-table-column
        prop="description"
        label="Description">
      </el-table-column>
      <el-table-column
        prop="effort"
        label="Effort"
        width="100">
      </el-table-column>
      <el-table-column
        prop="status.code"
        label="Status"
        width="100">
      </el-table-column>
      <el-table-column
        prop="create_user"
        label="Created By"
        width="100">
      </el-table-column>
    </el-table>
  </el-main>
</template>

<script>

export default {
  name: 'Breakdowns',
  props: ['selectedTicket'],
  methods: {
    goHome () {
      this.$store.dispatch('loadTickets', 1)
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.el-main {
  background-color: #EEF1F4;
}
</style>
