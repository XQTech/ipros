<template>
  <div>
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item>Support Logs</el-breadcrumb-item>
      <el-breadcrumb-item>List</el-breadcrumb-item>
    </el-breadcrumb>
    <div class="button-bar">
      <el-button
        type="primary"
        icon="el-icon-view"
        @click="handleSummary()"></el-button>
      <el-button
        type="primary"
        icon="el-icon-plus"
        @click="handleCreate()"></el-button>
    </div>
    <el-table
      :data="suplogs"
      style="width: 100%">
      <el-table-column
        prop="customer"
        :label="columns[0]"
        width="100">
        <template slot-scope="scope">
          <span>{{getCustomerbyID(scope.row.customer)}}</span>
        </template>
      </el-table-column>
      <el-table-column
        :label="columns[1]"
        width="80">
        <template slot-scope="scope">
          <span>{{getSystembyID(scope.row.system)}}</span>
        </template>
      </el-table-column>
      <el-table-column
        prop="sup_st_time"
        :label="columns[2]"
        width="100">
      </el-table-column>
      <el-table-column
        prop="sup_ed_time"
        :label="columns[3]"
        width="100">
      </el-table-column>
      <el-table-column
        prop="hours"
        :label="columns[4]"
        width="70">
      </el-table-column>
      <el-table-column
        prop="description"
        :label="columns[5]">
      </el-table-column>
      <el-table-column
        prop="solution"
        :label="columns[6]">
      </el-table-column>
      <el-table-column
        :label="columns[7]"
        width="120">
        <template slot-scope="scope">
          <span>{{getUserbyID(scope.row.assignee)}}</span>
        </template>
      </el-table-column>
      <el-table-column
        :label="columns[8]"
        width="100">
        <template slot-scope="scope">
          <span>{{getReporterbyID(scope.row.reporter)}}</span>
        </template>
      </el-table-column>
      <el-table-column
        :label="columns[9]"
        width="120">
        <template slot-scope="scope">
          <span>{{getStatusbyID(scope.row.status)}}</span>
        </template>
      </el-table-column>
      <el-table-column
        :label="columns[10]"
        width="100">
        <template slot-scope="scope">
          <span>{{getTypebyID(scope.row.issueType)}}</span>
        </template>
      </el-table-column>
      <el-table-column label="Action" width="150">
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
    <el-pagination
      background
      layout="prev, pager, next"
      :total="totalCount"
      @current-change="loadSuplogs">
    </el-pagination>
    <SuplogDetail
      ref="suplogform"
      v-on:createSuplog="createSuplog"
      v-on:updateSuplog="updateSuplog"></SuplogDetail>
    <SuplogSummary ref="summaryDialog"></SuplogSummary>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import SuplogDetail from './SuplogDetail'
import SuplogSummary from './SuplogSummary'
import { isLoggedIn } from '../../utils/auth'
// import axios from 'axios'

export default {
  name: 'Suglogs',
  components: {
    SuplogDetail,
    SuplogSummary
  },
  data () {
    return {
      columns: [
        'Customer',
        'System',
        'Time From',
        'Time To',
        'Hours',
        'Description',
        'Solution',
        'Supporter',
        'Reporter',
        'Status',
        'Type'
      ],
      visible: []
    }
  },
  created: function () {
    if (!isLoggedIn()) {
      this.$router.push({ name: 'Login' })
    }
    this.$store.dispatch('loadReporter')
    this.$store.dispatch('loadSupStatus')
    this.$store.dispatch('loadCustomers')
    this.$store.dispatch('loadSupTypes')
    this.$store.dispatch('loadToken')
    this.$store.dispatch('loadModules')
    this.$store.dispatch('loadUsers')
  },
  computed: {
    ...mapState({
      suplogs: state => state.suplog.suplogs,
      customers: state => state.customer.customers,
      users: state => state.user.users,
      reporters: state => state.reporter.reporters,
      suplogStatusList: state => state.suplogStatus.supStatusList,
      suptypes: state => state.suptype.suptypes,
      modules: state => state.systemModule.modules,
      totalCount: state => state.suplog.totalCount
    }),
    getStatusbyID () {
      return function (id) {
        return this.$store.getters.getSupStatusById(id)
      }
    },
    getCustomerbyID () {
      return function (id) {
        return this.$store.getters.getCustomerById(id)
      }
    },
    getReporterbyID () {
      return function (id) {
        return this.$store.getters.getReporterById(id)
      }
    },
    getSystembyID () {
      return function (id) {
        return this.$store.getters.getModuleById(id)
      }
    },
    getUserbyID () {
      return function (id) {
        return this.$store.getters.getUserById(id)
      }
    },
    getTypebyID () {
      return function (id) {
        return this.$store.getters.getTypeById(id)
      }
    }
  },
  methods: {
    loadSuplogs (page) {
      let params = {
        keys: null,
        page: page
      }
      this.$store.dispatch('loadSupLogs', params)
    },
    handleCreate () {
      this.$refs.suplogform.addSuplog()
    },
    handleDelete (scope) {
      this.visible = []
      this.$store.dispatch('deleteSupLog', scope.row.id)
        .then(response => {
          this.$message.success('Deleted Successfully!')
        })
        .catch(error => {
          this.$message.error(error.message)
        })
    },
    handleUpdate (suplog) {
      this.$refs.suplogform.updateSuplog(suplog)
    },
    createSuplog (suplog) {
      this.$store.dispatch('createSuplog', suplog)
        .then(response => {
          this.$message.success('Created Successfully!')
          // this.loadSuplogs(1)
        })
        .catch(error => {
          this.$message.error(error.message)
        })
    },
    updateSuplog (suplog) {
      this.$store.dispatch('updateSuplog', suplog)
        .then(response => {
          this.$message.success('Update Successfully!')
        })
        .catch(error => {
          this.$message.error(error.message)
        })
    },
    handleSummary () {
      this.$refs.summaryDialog.show()
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
</style>
