<template>
  <div>
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item>Support Logs</el-breadcrumb-item>
      <el-breadcrumb-item>List (Total - {{totalCount}})</el-breadcrumb-item>
    </el-breadcrumb>
    <el-form :inline="true" style="display:flex;">
      <el-form-item>
        <el-select v-model="searchKeys.customer" placeholder="Customer">
          <el-option v-for="item in customers"
            v-bind:key="item.id"
            :label="item.name"
            :value="item.id"></el-option>
        </el-select>
      </el-form-item>
      <el-form-item>
        <el-select v-model="searchKeys.assignee" placeholder="Supporter">
          <el-option v-for="item in users"
            v-bind:key="item.id"
            :label="item.username"
            :value="item.id"></el-option>
        </el-select>
      </el-form-item>
      <el-form-item>
        <el-select v-model="searchKeys.system" placeholder="System">
          <el-option v-for="item in modules"
            v-bind:key="item.id"
            :label="item.name"
            :value="item.id"></el-option>
        </el-select>
      </el-form-item>
      <el-form-item>
        <el-input placeholder="Issue Detail" v-model="searchKeys.description__icontains" style="width:300px;"></el-input>
      </el-form-item>
      <el-form-item>
        <el-input placeholder="Solution" v-model="searchKeys.solution__icontains" style="width:300px;"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="loadSuplogs(1)" icon="fa fa-search"></el-button>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="handleReset()" icon="fa fa-undo"></el-button>
      </el-form-item>
      <el-form-item>
        <el-button
        type="primary"
        icon="fa fa-plus"
        @click="handleCreate()"></el-button>
      </el-form-item>
      <el-form-item>
        <el-button
        type="primary"
        icon="fa fa-bar-chart"
        @click="handleSummary()"></el-button>
      </el-form-item>
    </el-form>
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
import { isLoggedIn } from '../utils/auth'

export default {
  name: 'Suglogs',
  components: {
    SuplogDetail,
    SuplogSummary
  },
  data () {
    return {
      searchKeys: {
        customer: '',
        assignee: '',
        description__icontains: '',
        solution__icontains: '',
        system: ''
      },
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
      visible: [],
      params: {
        self: this,
        keys: null,
        page: 1,
        item: null,
        id: 0
      }
    }
  },
  created: function () {
    if (!isLoggedIn()) {
      this.$router.push({ name: 'Login' })
    }
    this.$store.dispatch('loadToken')
    this.$store.dispatch('loadReporter', this.params)
    this.$store.dispatch('loadSupStatus', this.params)
    this.$store.dispatch('loadCustomers', this.params)
    this.$store.dispatch('loadSupTypes', this.params)
    this.$store.dispatch('loadModules', this.params)
    this.$store.dispatch('loadUsers', this.params)
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
      this.params.page = page
      this.params.keys = this.searchKeys
      this.$store.dispatch('loadSupLogs', this.params)
    },
    handleCreate () {
      this.$refs.suplogform.addSuplog()
    },
    handleDelete (scope) {
      this.visible = []
      this.params.id = scope.row.id
      this.$store.dispatch('deleteSupLog', this.params)
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
      this.params.item = suplog
      this.$store.dispatch('createSuplog', this.params)
        .then(response => {
          this.$message.success('Created Successfully!')
          // this.loadSuplogs(1)
        })
        .catch(error => {
          this.$message.error(error.message)
        })
    },
    updateSuplog (suplog) {
      this.params.item = suplog
      this.$store.dispatch('updateSuplog', this.params)
        .then(response => {
          this.$message.success('Update Successfully!')
        })
        .catch(error => {
          this.$message.error(error.message)
        })
    },
    handleSummary () {
      this.$refs.summaryDialog.show()
    },
    handleReset () {
      for (var key in this.searchKeys) {
        this.searchKeys[key] = ''
      }
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
</style>
