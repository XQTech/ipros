<template>
  <div>
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item>Environment</el-breadcrumb-item>
      <el-breadcrumb-item>List</el-breadcrumb-item>
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
        <el-select v-model="searchKeys.envtype" placeholder="Env Type">
          <el-option v-for="item in envTypes"
            v-bind:key="item.id"
            :label="item.name"
            :value="item.id"></el-option>
        </el-select>
      </el-form-item>
      <el-form-item>
        <el-input placeholder="Remarks" v-model="searchKeys.remark__icontains" style="width:400px;"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="loadEnvItems()" icon="fa fa-search"></el-button>
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
    </el-form>
    <el-table
      :data="envItems"
      style="width: 100%">
      <el-table-column
        :label="columns[0]"
        width="100">
        <template slot-scope="scope">
          <span>{{getCustomerbyID(scope.row.customer)}}</span>
        </template>
      </el-table-column>
      <el-table-column
        :label="columns[1]"
        width="100">
        <template slot-scope="scope">
          <span>{{getEnvTypeById(scope.row.envtype)}}</span>
        </template>
      </el-table-column>
      <el-table-column
        prop="name"
        :label="columns[2]"
        width="150">
      </el-table-column>
      <el-table-column
        prop="url"
        :label="columns[3]"
        width="200">
      </el-table-column>
      <el-table-column
        prop="username"
        :label="columns[4]"
        width="120">
      </el-table-column>
      <el-table-column
        prop="password"
        :label="columns[5]"
        width="120">
      </el-table-column>
      <el-table-column
        prop="remark"
        :label="columns[6]">
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
    <EnvItemDetail
      ref="detailForm"
      v-on:createEnvItem="createEnvItem"
      v-on:updateEnvItem="updateEnvItem"></EnvItemDetail>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import EnvItemDetail from './EnvItemDetail'
import { isLoggedIn } from '../utils/auth'

export default {
  name: 'EnvItems',
  components: {
    EnvItemDetail
  },
  data () {
    return {
      searchKeys: {
        customer: '',
        envtype: '',
        remark__icontains: ''
      },
      columns: [
        'Customer',
        'Env Type',
        'Item Name',
        'URL/IP/HOST',
        'User Name',
        'Password',
        'Remarks'
      ],
      visible: [],
      params: {
        self: this,
        keys: null,
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
    this.$store.dispatch('loadEnvTypes', this.params)
  },
  computed: {
    ...mapState({
      envTypes: state => state.envType.envTypes,
      customers: state => state.customer.customers,
      envItems: state => state.envItem.envItems
    }),
    getEnvTypeById () {
      return function (id) {
        return this.$store.getters.getEnvTypeById(id)
      }
    },
    getCustomerbyID () {
      return function (id) {
        return this.$store.getters.getCustomerById(id)
      }
    }
  },
  methods: {
    loadEnvItems () {
      this.params.keys = this.searchKeys
      this.$store.dispatch('loadEnvItems', this.params)
    },
    handleCreate () {
      this.$refs.detailForm.addEnvItem()
    },
    handleDelete (scope) {
      this.visible = []
      this.params.id = scope.row.id
      this.$store.dispatch('deleteEnvItem', this.params)
        .then(response => {
          this.$message.success('Deleted Successfully!')
        })
        .catch(error => {
          this.$message.error(error.message)
        })
    },
    handleUpdate (envitem) {
      this.$refs.detailForm.updateEnvItem(envitem)
    },
    createEnvItem (envitem) {
      this.params.item = envitem
      this.$store.dispatch('createEnvItem', this.params)
        .then(response => {
          this.$message.success('Created Successfully!')
        })
        .catch(error => {
          this.$message.error(error.message)
        })
    },
    updateEnvItem (envitem) {
      this.params.item = envitem
      this.$store.dispatch('updateEnvItem', this.params)
        .then(response => {
          this.$message.success('Update Successfully!')
        })
        .catch(error => {
          this.$message.error(error.message)
        })
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
