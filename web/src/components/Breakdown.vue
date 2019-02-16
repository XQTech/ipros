<template>
  <el-dialog title="Breakdown Details" :visible.sync="dialogFormVisible">
    <el-form :label-position="labelPosition" :model="selectedBreakdown">
      <el-form-item label="Function Group" :label-width="formLabelWidth">
        <el-select v-model="selectedBreakdown.function_group" placeholder="------">
          <el-option v-for="func in funcGroups"
            v-bind:key="func.id"
            :label="func.description"
            :value="func.id"></el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="Description" :label-width="formLabelWidth">
        <el-input type="textarea" :rows="5" v-model="selectedBreakdown.description" style="width:400px"></el-input>
      </el-form-item>
      <el-form-item label="Status" :label-width="formLabelWidth">
        <el-select v-model="selectedBreakdown.status" placeholder="------">
          <el-option v-for="status in statusList"
            v-bind:key="status.id"
            :label="status.code"
            :value="status.id"></el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="Effort" :label-width="formLabelWidth">
        <el-input-number v-model="selectedBreakdown.effort"></el-input-number>
      </el-form-item>
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
      funcGroups: state => state.funcGroups.functionGroups
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
        function_group: 1,
        description: '',
        status: 1,
        effort: 0
      }
      this.isAdd = true
      this.dialogFormVisible = true
      this.selectedTicket = selectedTicket
    },
    handleSubmit () {
      if (this.isAdd) {
        this.$emit('createBreakdown', this.selectedBreakdown)
      } else {
        // this.$store.dispatch('updateBreakdown', this.selectedBreakdown)
        this.$emit('updateBreakdown', this.selectedBreakdown)
      }
      this.dialogFormVisible = false
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.el-form-item {
  display: flex;
}
.el-select, .el-input-number {
  width: 400px;
}
.el-form {
  margin-left: 10px;
}
</style>
