<template>
  <el-dialog title="Environment Item Details" :visible.sync="dialogFormVisible" center width="60%">
    <el-form :label-position="labelPosition" :model="envitem">
      <el-row>
        <el-col :span="12">
          <el-form-item label="Customer" :label-width="formLabelWidth">
            <el-select v-model="envitem.customer" placeholder="------">
              <el-option v-for="cus in customers"
                v-bind:key="cus.id"
                :label="cus.name"
                :value="cus.id"></el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="Env Type" :label-width="formLabelWidth">
            <el-select v-model="envitem.envtype" placeholder="------">
              <el-option v-for="cus in envTypes"
                v-bind:key="cus.id"
                :label="cus.name"
                :value="cus.id"></el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="Item Name" :label-width="formLabelWidth">
            <el-input v-model="envitem.name"></el-input>
          </el-form-item>
          <el-form-item label="URL/IP/HOST" :label-width="formLabelWidth">
            <el-input v-model="envitem.url"></el-input>
          </el-form-item>
          <el-form-item label="User Name" :label-width="formLabelWidth">
            <el-input v-model="envitem.username"></el-input>
          </el-form-item>
          <el-form-item label="Password" :label-width="formLabelWidth">
            <el-input v-model="envitem.password"></el-input>
          </el-form-item>
        </el-col>
        <el-col :span="12">
          <el-form-item label="Remarks" :label-width="formLabelWidth">
            <el-input type="textarea" :rows="16" v-model="envitem.remark"></el-input>
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
  name: 'EnvItemDetail',
  data () {
    return {
      formLabelWidth: '120px',
      dialogFormVisible: false,
      envitem: {},
      isAdd: false,
      labelPosition: 'left'
    }
  },
  computed: {
    ...mapState({
      customers: state => state.customer.customers,
      envTypes: state => state.envType.envTypes
    })
  },
  methods: {
    updateEnvItem (envitem) {
      this.isAdd = false
      this.dialogFormVisible = true
      this.envitem = envitem
    },
    addEnvItem () {
      this.envitem = {
        customer: 1,
        envtype: 1,
        url: '',
        username: '',
        password: '',
        remark: ''
      }
      this.isAdd = true
      this.dialogFormVisible = true
    },
    handleSubmit () {
      if (this.isAdd) {
        this.$emit('createEnvItem', this.envitem)
      } else {
        this.$emit('updateEnvItem', this.envitem)
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
