<template>
  <el-main>
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/' }" @click.native="goHome">Home</el-breadcrumb-item>
      <el-breadcrumb-item>Ticket List</el-breadcrumb-item>
      <el-breadcrumb-item>Breakdown</el-breadcrumb-item>
      <el-breadcrumb-item>{{ selectedTicket.ticket_no }}</el-breadcrumb-item>
    </el-breadcrumb>
    <div class="button-bar">
      <el-button
        type="primary"
        icon="el-icon-plus"
        @click="handleCreate()"></el-button>
    </div>
    <el-table
      ref="filterTable"
      :data="breakdowns"
      style="width: 100%">
      <el-table-column
        label="Function"
        sortable
        width="180">
        <template slot-scope="scope">
          <span>{{getFuncGroupbyID(scope.row.function_group)}}</span>
        </template>
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
        label="Status"
        width="100">
        <template slot-scope="scope">
          <span>{{getStatusbyID(scope.row.status)}}</span>
        </template>
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
            type="primary"
            icon="el-icon-edit"
            @click="handleUpdate(scope.row)"></el-button>
          <el-popover
            placement="top"
            width="160"
            v-model="visible[scope.$index]">
            <p>Are you sure to delete?</p>
            <div style="text-align: right; margin: 0">
              <el-button size="mini" type="text" @click="visible = []">Cancel</el-button>
              <el-button type="primary" size="mini" @click="handleDelete(scope)">Yes</el-button>
            </div>
            <el-button
                size="mini"
                type="danger"
                slot="reference"
                icon="el-icon-delete"></el-button>
          </el-popover>
        </template>
      </el-table-column>
    </el-table>
    <Breakdown
      ref="breakdownForm"
      v-on:createBreakdown="createBreakdown"
      v-on:updateBreakdown="updateBreakdown"
      v-on:deleteBreakdown="deleteBreakdown"></Breakdown>
  </el-main>
</template>

<script>
import Breakdown from './Breakdown'
import axios from 'axios'

export default {
  name: 'Breakdowns',
  components: {
    Breakdown
  },
  props: ['selectedTicket'],
  data () {
    return {
      visible: [],
      breakdowns: []
    }
  },
  mounted: function () {
    console.log('breakdown mounted...')
    this.loadBreakdowns()
  },
  computed: {
    getStatusbyID () {
      return function (id) {
        return this.$store.getters.getStatusById(id)
      }
    },
    getFuncGroupbyID () {
      return function (id) {
        return this.$store.getters.getFuncGroupById(id)
      }
    }
  },
  methods: {
    goHome () {
      this.$store.dispatch('loadTickets', 1)
    },
    loadBreakdowns () {
      axios.get('http://localhost:8000/breakdown/breakdowns/' + this.selectedTicket.id + '/breakdowns/')
        .then(response => {
          console.log('printing result from api.....')
          console.log(response)
          console.log(response.data)
          this.breakdowns = response.data
        })
        .catch(error => {
          console.log(error)
        })
    },
    handleDelete (scope) {
      this.visible = []
      console.log(scope.row)
      this.deleteBreakdown(scope.row.id)
      this.breakdowns = this.breakdowns.filter(item => item.id !== scope.row.id)
    },
    handleUpdate (breakdown) {
      this.$refs.breakdownForm.updateBreakdown(breakdown)
      console.log(breakdown.description)
    },
    handleCreate () {
      console.log('creating breakdown.....open form....')
      this.$refs.breakdownForm.addBreakdown(this.selectedTicket)
    },
    createBreakdown (breakdown) {
      console.log('>>>create breakdown....')
      console.log(breakdown)
      axios.post('http://localhost:8000/breakdown/breakdowns/', breakdown)
        .then(response => {
          console.log('posting the data to api....')
          console.log(response)
          console.log(response.data)
          this.loadBreakdowns()
        })
        .catch(error => {
          console.log(error)
        })
    },
    updateBreakdown (breakdown) {
      console.log('>>>update breakdown....')
      axios.put('http://localhost:8000/breakdown/breakdowns/' + breakdown.id + '/', breakdown)
        .then(response => {
          console.log(response)
          console.log(response.data)
        })
        .catch(error => {
          console.log(error)
        })
    },
    deleteBreakdown (breakdownId) {
      console.log('>>>delete breakdown....' + breakdownId)
      axios.delete('http://localhost:8000/breakdown/breakdowns/' + breakdownId + '/')
        .then(response => {
          console.log(response)
          console.log(response.data)
        })
        .catch(error => {
          console.log(error)
        })
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
