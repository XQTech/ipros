<template>
  <div>
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item>Breakdown</el-breadcrumb-item>
      <el-breadcrumb-item :to="{ path: '/breakdown' }" @click.native="goHome">Ticket List</el-breadcrumb-item>
      <el-breadcrumb-item>{{ selectedTicket.ticket_no }}</el-breadcrumb-item>
    </el-breadcrumb>
    <div class="button-bar">
      <el-button
        type="primary"
        icon="fa fa-plus"
        @click="handleCreate()"></el-button>
    </div>
    <el-table
      :data="breakdowns"
      style="width: 100%">
      <el-table-column
        prop="sequence"
        label="SN"
        width="50">
      </el-table-column>
      <el-table-column
        label="Category"
        width="180">
        <template slot-scope="scope">
          <span>{{getParentCategory(scope.row.category)}}</span>
        </template>
      </el-table-column>
      <el-table-column
        label="Sub Category"
        width="180">
        <template slot-scope="scope">
          <span>{{getSubCategory(scope.row.category)}}</span>
        </template>
      </el-table-column>
      <el-table-column
        label="Function"
        width="120">
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
        label="Assigned To"
        width="120">
        <template slot-scope="scope">
          <span>{{getUserbyID(scope.row.assigned_user)}}</span>
        </template>
      </el-table-column>
      <el-table-column
        prop="due_date"
        label="Due Date"
        width="100">
      </el-table-column>
      <el-table-column label="Action" width="200">
        <template slot-scope="scope">
          <el-button
            size="mini"
            type="primary"
            icon="el-icon-edit"
            @click="handleUpdate(scope.row)"></el-button>
          <el-button
            size="mini"
            type="primary"
            icon="el-icon-picture"
            @click="handleUpdateImage(scope.row)"></el-button>
          <el-popover
            placement="top"
            width="160"
            v-model="visible[scope.$index]">
            <p>Are you sure to delete?</p>
            <div style="text-align: right; margin: 0">
              <el-button size="mini" type="text" @click="visible = []">Cancel</el-button>
              <el-button type="primary" size="mini" @click="handleDelete(scope)"
                style="margin-left:10px;">Yes</el-button>
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
      v-on:updateBreakdown="updateBreakdown"></Breakdown>
    <UploadImage
      ref="imageForm"></UploadImage>
  </div>
</template>

<script>
import Breakdown from './Breakdown'
import UploadImage from './UploadImage'
import { mapState } from 'vuex'

export default {
  name: 'Breakdowns',
  components: {
    Breakdown,
    UploadImage
  },
  props: ['selectedTicket'],
  data () {
    return {
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
  mounted: function () {
    this.params.id = this.selectedTicket.id
    this.$store.dispatch('loadBreakdowns', this.params)
  },
  computed: {
    ...mapState({
      breakdowns: state => state.breakdown.breakdowns
    }),
    getStatusbyID () {
      return function (id) {
        return this.$store.getters.getStatusById(id)
      }
    },
    getFuncGroupbyID () {
      return function (id) {
        return this.$store.getters.getFuncGroupById(id)
      }
    },
    getSubCategory () {
      return function (id) {
        if (id === null) {
          return ''
        }
        let cat = this.$store.getters.getCategoryById(id)
        if (cat.parent === null) {
          return ''
        } else {
          return cat.code
        }
      }
    },
    getParentCategory () {
      return function (id) {
        if (id === null) {
          return ''
        }
        let cat = this.$store.getters.getCategoryById(id)
        if (cat.parent === null) {
          return cat.code
        } else {
          let parent = this.$store.getters.getCategoryById(cat.parent)
          return parent.code
        }
      }
    },
    getUserbyID () {
      return function (id) {
        return this.$store.getters.getUserById(id)
      }
    }
  },
  methods: {
    goHome () {
      this.$store.dispatch('loadDocs', this.params)
      this.$store.dispatch('loadTickets', this.params)
    },
    handleDelete (scope) {
      this.visible = []
      this.params.id = scope.row.id
      this.$store.dispatch('deleteBreakdown', this.params)
        .then(response => {
          this.$message.success('Delete successfully')
        })
        .catch(error => {
          this.$message.error(error.message)
        })
    },
    handleUpdate (breakdown) {
      this.$refs.breakdownForm.updateBreakdown(breakdown)
    },
    handleCreate () {
      this.$refs.breakdownForm.addBreakdown(this.selectedTicket)
    },
    handleUpdateImage (breakdown) {
      this.$refs.imageForm.showImageForm(breakdown)
    },
    createBreakdown (breakdown) {
      this.params.item = breakdown
      this.$store.dispatch('createBreakdown', this.params)
        .then(response => {
          this.$message.success('Create successfully')
        })
        .catch(error => {
          this.$message.error(error.message)
        })
    },
    updateBreakdown (breakdown) {
      let tempBreakdown = {
        id: breakdown.id,
        ticket: breakdown.ticket,
        sequence: breakdown.sequence,
        category: breakdown.category,
        function_group: breakdown.function_group,
        description: breakdown.description,
        status: breakdown.status,
        effort: breakdown.effort,
        assigned_user: breakdown.assigned_user,
        due_date: breakdown.due_date,
        create_user: breakdown.create_user
      }
      this.params.item = tempBreakdown
      this.$store.dispatch('updateBreakdown', this.params)
        .then(response => {
          this.$message.success('Update successfully')
        })
        .catch(error => {
          this.$message.error(error.message)
        })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.el-button {
    margin-left: 0;
}
</style>
