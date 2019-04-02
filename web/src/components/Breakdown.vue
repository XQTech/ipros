<template>
  <el-dialog title="Breakdown Details" :visible.sync="dialogFormVisible" center width="80%">
    <el-form :label-position="labelPosition" :model="selectedBreakdown">
      <el-row>
        <el-col :span="12">
          <el-form-item label="Sequence" :label-width="formLabelWidth">
            <el-input-number v-model="selectedBreakdown.sequence"></el-input-number>
          </el-form-item>
          <el-form-item label="Category" :label-width="formLabelWidth">
            <!-- <el-select v-model="selectedBreakdown.category" placeholder="------">
              <el-option v-for="cat in categories"
                v-bind:key="cat.id"
                :label="cat.code"
                :value="cat.id"></el-option>
            </el-select> -->
            <el-cascader
              :options="getCategoryOptions(categories)"
              v-model="selectedOptions"
              @change="handleChange"
              placeholder="---------"
              style="width:80%;">
            </el-cascader>
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
            <el-input type="textarea" :rows="7" v-model="selectedBreakdown.description" style="width:80%;"
            :placeholder="getCategoryTips()"
            :maxlength=1000></el-input>
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
            <el-input-number v-model="selectedBreakdown.effort" :precision="1" :step="0.5"></el-input-number>
          </el-form-item>
          <el-form-item label="Due Date" :label-width="formLabelWidth">
            <el-date-picker
              v-model="selectedBreakdown.due_date"
              type="date"
              value-format="yyyy-MM-dd"
              placeholder="Due Date">
            </el-date-picker>
          </el-form-item>
          <el-form-item label="in FD" :label-width="formLabelWidth">
            <el-switch
              v-model="selectedBreakdown.in_fd"
              active-color="#13ce66"
              inactive-color="#ff4949">
            </el-switch>
          </el-form-item>
          <el-form-item label="in Breakdown" :label-width="formLabelWidth">
            <el-switch
              v-model="selectedBreakdown.in_bk"
              active-color="#13ce66"
              inactive-color="#ff4949">
            </el-switch>
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
import { getLoginUser } from '../utils/auth'
export default {
  name: 'Breakdown',
  data () {
    return {
      formLabelWidth: '120px',
      dialogFormVisible: false,
      selectedBreakdown: {},
      selectedTicket: null,
      isAdd: false,
      labelPosition: 'left',
      selectedOptions: [],
      value3: true
    }
  },
  computed: {
    ...mapState({
      statusList: state => state.ticketStatus.statusList,
      funcGroups: state => state.funcGroup.functionGroups,
      categories: state => state.category.categories,
      users: state => state.user.users
    })
  },
  methods: {
    handleChange () {
      this.selectedBreakdown.category = this.selectedOptions.slice(-1)[0]
    },
    getCategoryOptions (elements) {
      let options = []
      elements.forEach(element => {
        if (element.parent !== null && element.sub_category != null) {
          return false
        }
        let option = this.convertCategory(element)
        if (element.sub_category && element.sub_category.length > 0) {
          option.children = this.getCategoryOptions(element.sub_category)
        }
        options.push(option)
      })
      return options
    },
    convertCategory (element) {
      return {
        value: element.id,
        label: element.code
      }
    },
    getCategoryTips () {
      let tips = this.$store.getters.getCategoryById(this.selectedBreakdown.category).tips
      if (tips === null) {
        tips = ''
      } else {
        tips = tips + '\n\n'
      }
      return tips + "Add short description between '{' and '}' to be used in effort excel \n"
    },
    updateBreakdown (selectedBreakdown) {
      this.isAdd = false
      this.dialogFormVisible = true
      this.selectedBreakdown = selectedBreakdown
      if (this.selectedBreakdown.category != null) {
        let parent = this.$store.getters.getCategoryById(this.selectedBreakdown.category).parent
        if (parent != null) {
          this.selectedOptions = [parent, this.selectedBreakdown.category]
        } else {
          this.selectedOptions = [this.selectedBreakdown.category]
        }
      }
    },
    addBreakdown (selectedTicket) {
      this.selectedBreakdown = {
        ticket: selectedTicket.id,
        sequence: 1,
        category: 1,
        function_group: 22,
        description: '',
        status: 1,
        effort: 0,
        assigned_user: getLoginUser().id,
        image1: null,
        image2: null,
        image3: null,
        due_date: selectedTicket.due_date,
        in_fd: true,
        in_bk: true,
        create_user: getLoginUser().username
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
