<template>
  <el-dialog title="Support Log Details" :visible.sync="dialogFormVisible" center width="80%">
    <el-form :label-position="labelPosition" :model="suplog">
      <el-row>
        <el-col :span="10">
          <el-form-item label="Customer" :label-width="formLabelWidth">
            <el-select v-model="suplog.customer" @change="customerChange()" placeholder="------">
              <el-option v-for="cus in customers"
                v-bind:key="cus.id"
                :label="cus.name"
                :value="cus.id"></el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="System" :label-width="formLabelWidth">
            <el-select v-model="suplog.system" placeholder="------">
              <el-option v-for="cus in systems"
                v-bind:key="cus.id"
                :label="cus.name"
                :value="cus.id"></el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="Reporter" :label-width="formLabelWidth">
            <el-select v-model="suplog.reporter" placeholder="------">
              <el-option v-for="cus in reporters" v-if="cus.company == suplog.customer"
                v-bind:key="cus.id"
                :label="cus.name"
                :value="cus.id"></el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="Supporter" :label-width="formLabelWidth">
            <el-select v-model="suplog.assignee" placeholder="------">
              <el-option v-for="cus in users"
                v-bind:key="cus.id"
                :label="cus.username"
                :value="cus.id"></el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="Start Datetime" :label-width="formLabelWidth">
            <el-date-picker
              v-model="suplog.sup_st_time"
              type="datetime"
              value-format="yyyy-MM-dd HH:mm:ss"
              placeholder="Start Date Time">
            </el-date-picker>
          </el-form-item>
          <el-form-item label="End Datetime" :label-width="formLabelWidth">
            <el-date-picker
              v-model="suplog.sup_ed_time"
              type="datetime"
              value-format="yyyy-MM-dd HH:mm:ss"
              placeholder="End Date Time">
            </el-date-picker>
          </el-form-item>
          <el-form-item label="Issue Type" :label-width="formLabelWidth">
            <el-select v-model="suplog.issueType" placeholder="------">
              <el-option v-for="type in types"
                v-bind:key="type.id"
                :label="type.name"
                :value="type.id"></el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="Status" :label-width="formLabelWidth">
            <el-select v-model="suplog.status" placeholder="------">
              <el-option v-for="status in statuss"
                v-bind:key="status.id"
                :label="status.name"
                :value="status.id"></el-option>
            </el-select>
          </el-form-item>
        </el-col>
        <el-col :span="14">
          <el-form-item label="Description" :label-width="formLabelWidth">
            <el-input type="textarea" :rows="9" v-model="suplog.description"
              placeholder="Please input the issue details"></el-input>
          </el-form-item>
          <el-form-item label="Solution" :label-width="formLabelWidth">
            <el-input type="textarea" :rows="9" v-model="suplog.solution"
              placeholder="Please input the solution details"></el-input>
          </el-form-item>
        </el-col>
      </el-row>
    </el-form>
    <div slot="footer" class="dialog-footer">
      <el-button @click="dialogFormVisible = false">Cancel</el-button>
      <el-button type="primary" @click="handleSubmit()">Submit</el-button>
    </div>
  </el-dialog>
</template>

<script>
import { mapState } from 'vuex'

export default {
  name: 'SuplogDetail',
  data () {
    return {
      formLabelWidth: '120px',
      dialogFormVisible: false,
      suplog: {},
      isAdd: false,
      labelPosition: 'left'
    }
  },
  computed: {
    ...mapState({
      customers: state => state.customer.customers,
      users: state => state.user.users,
      reporters: state => state.reporter.reporters,
      systems: state => state.systemModule.modules,
      types: state => state.suptype.suptypes,
      statuss: state => state.suplogStatus.supStatusList
    })
  },
  methods: {
    updateSuplog (suplog) {
      this.isAdd = false
      this.dialogFormVisible = true
      this.suplog = suplog
      console.log(suplog)
    },
    customerChange () {
      let suplog = this.suplog
      suplog.reporter = this.reporters.filter(item => item.company === suplog.customer)[0]
    },
    addSuplog () {
      this.suplog = {
        status: 1,
        customer: 1,
        assignee: 4,
        description: '',
        reporter: 1,
        solution: '',
        issueType: 1,
        sup_st_time: null,
        sup_ed_time: null,
        system: null
      }
      this.isAdd = true
      this.dialogFormVisible = true
    },
    handleSubmit () {
      if (this.isAdd) {
        this.$emit('createSuplog', this.suplog)
      } else {
        this.$emit('updateSuplog', this.suplog)
      }
      this.dialogFormVisible = false
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.el-input-number{
  width: 80%;
}
.el-select {
  width: 80%;
}
.el-input {
  width: 80%;
}
.el-date-picker {
  width: 80%;
}
</style>
