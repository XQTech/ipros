<template>
  <el-dialog title="Breakdown Details" :visible.sync="dialogFormVisible" center width="80%">
    <el-form :label-position="labelPosition" :model="selectedBreakdown">
      <el-row>
        <el-col :span="12">
          <el-form-item label="Sequence" :label-width="formLabelWidth">
            <el-input-number v-model="selectedBreakdown.sequence"></el-input-number>
          </el-form-item>
          <el-form-item label="Category" :label-width="formLabelWidth">
            <el-select v-model="selectedBreakdown.category" placeholder="------">
              <el-option v-for="cat in categories"
                v-bind:key="cat.id"
                :label="cat.code"
                :value="cat.id"></el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="Function Group" :label-width="formLabelWidth">
            <el-select v-model="selectedBreakdown.function_group" placeholder="------">
              <el-option v-for="func in funcGroups"
                v-bind:key="func.id"
                :label="func.description"
                :value="func.id"></el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="Description" :label-width="formLabelWidth">
            <el-input type="textarea" :rows="6" v-model="selectedBreakdown.description" style="width:80%;"
            placeholder="Add short description between '{' and '}' to be used in effort excel"></el-input>
          </el-form-item>
        </el-col>
        <el-col :span="12">
          <el-form-item label="Status" :label-width="formLabelWidth">
            <el-select v-model="selectedBreakdown.status" placeholder="------">
              <el-option v-for="status in statusList"
                v-bind:key="status.id"
                :label="status.code"
                :value="status.id"></el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="Assigned To" :label-width="formLabelWidth">
            <el-select v-model="selectedBreakdown.assigned_user" placeholder="------">
              <el-option v-for="user in users"
                v-bind:key="user.id"
                :label="user.username"
                :value="user.id"></el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="Effort" :label-width="formLabelWidth">
            <el-input-number v-model="selectedBreakdown.effort"></el-input-number>
          </el-form-item>
          <el-form-item label="Due Date" :label-width="formLabelWidth">
            <el-date-picker
              v-model="selectedBreakdown.due_date"
              type="date"
              value-format="yyyy-MM-dd"
              placeholder="Due Date">
            </el-date-picker>
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
import { getLoginUser } from '../../utils/auth'

export default {
  name: 'Breakdown',
  data () {
    return {
      formLabelWidth: '120px',
      dialogFormVisible: false,
      selectedBreakdown: {},
      selectedTicket: null,
      isAdd: false,
      labelPosition: 'left'
    }
  },
  computed: {
    ...mapState({
      statusList: state => state.ticketStatus.statusList,
      funcGroups: state => state.funcGroups.functionGroups,
      categories: state => state.category.categories,
      users: state => state.user.users
    })
  },
  methods: {
    updateBreakdown (selectedBreakdown) {
      this.isAdd = false
      this.dialogFormVisible = true
      this.selectedBreakdown = selectedBreakdown
      console.log(selectedBreakdown)
    },
    addBreakdown (selectedTicket) {
      this.selectedBreakdown = {
        ticket: selectedTicket.id,
        sequence: 1,
        category: 1,
        function_group: 1,
        description: '',
        status: 1,
        effort: 0,
        assigned_user: 1,
        image1: null,
        image2: null,
        image3: null,
        due_date: null,
        create_user: getLoginUser()
      }
      this.isAdd = true
      this.dialogFormVisible = true
      this.selectedTicket = selectedTicket
    },
    handleSubmit () {
      if (this.isAdd) {
        this.$emit('createBreakdown', this.selectedBreakdown)
      } else {
        this.$emit('updateBreakdown', this.selectedBreakdown)
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
