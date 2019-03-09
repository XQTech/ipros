<template>
  <el-dialog large title="Support Log Summary" :visible.sync="dialogFormVisible" center width="90%">
    <el-form :label-position="labelPosition" :inline="true">
      <el-form-item label="Start Date" :label-width="formLabelWidth">
        <el-date-picker
          v-model="startDate"
          type="date"
          value-format="yyyy-MM-dd"
          placeholder="Start Date">
        </el-date-picker>
      </el-form-item>
      <el-form-item label="End Date" :label-width="formLabelWidth">
        <el-date-picker
          v-model="endDate"
          type="date"
          value-format="yyyy-MM-dd"
          placeholder="End Date">
        </el-date-picker>
      </el-form-item>
      <el-button @click="refreshSummary()">Go!</el-button>
    </el-form>
    <el-row style="margin-top:20px;">
      <el-col :span="8">
        <div id="bysupporter" class="charts"></div>
      </el-col>
      <el-col :span="8">
        <div id="bycustomer" class="charts"></div>
      </el-col>
      <el-col :span="8">
        <div id="byWorkingHour" class="charts"></div>
      </el-col>
    </el-row>
    <el-row>
      <el-col :span="8">
        <div id="bystatus" class="charts"></div>
      </el-col>
      <el-col :span="8">
        <div id="bysystem" class="charts"></div>
      </el-col>
      <el-col :span="8">
        <div id="byreporter" class="charts"></div>
      </el-col>
    </el-row>
    <div slot="footer" class="dialog-footer">
      <span class="summary-total">Total: {{totalCount}}</span>
      <el-button type="primary" @click="dialogFormVisible = false">Close</el-button>
    </div>
  </el-dialog>
</template>

<script>
import { mapState } from 'vuex'
require('echarts/lib/chart/bar')
require('echarts/lib/component/tooltip')
require('echarts/lib/component/title')
import axios from 'axios'

export default {
  name: 'SuplogSummary',
  data () {
    return {
      formLabelWidth: '120px',
      dialogFormVisible: false,
      labelPosition: 'left',
      startDate: '',
      endDate: '',
      totalCount: 0,
      instance: this,
      suplogs: []
    }
  },
  computed: {
    ...mapState({
      customers: state => state.customer.customers,
      users: state => state.user.users,
      reporters: state => state.reporter.reporters,
      suplogStatusList: state => state.suplogStatus.supStatusList,
      suptypes: state => state.suptype.suptypes,
      modules: state => state.systemModule.modules
    })
  },
  methods: {
    show () {
      this.dialogFormVisible = true
    },
    refreshSummary () {
      console.log('>>>loading all sup logs....')
      let url = 'http://localhost:8000/api/sup/suplogs-all/?start-time=' + this.startDate + '&end-time=' + this.endDate
      axios.get(url)
        .then(response => {
          this.suplogs = response.data
          this.totalCount = this.suplogs.length
          // this.generateSummary('bysupporter', this.getPieChartData('issueType', this.getTypebyID()), 'Issue Type')
          this.generateSummary('bycustomer', this.getPieChartData('customer', this.getCustomerbyID()), 'Customer')
          this.generateSummary('byWorkingHour', this.getWorkingHourData(), 'Working Hour')
          this.generateSummary('bysupporter', this.getPieChartData('assignee', this.getUserbyID()), 'Supporter')
          this.generateSummary('bysystem', this.getPieChartData('system', this.getSystembyID()), 'System')
          this.generateSummary('bystatus', this.getPieChartData('status', this.getStatusbyID()), 'Issue Status')
          this.generateSummary('byreporter', this.getPieChartData('reporter', this.getReporterbyID()), 'Reporter')
        })
        .catch(error => {
          console.log(error)
        })
    },
    getPieChartData (field, f) {
      let result = []
      let group = this.groupBy(this.suplogs, function (item) {
        return [Reflect.get(item, field)]
      })
      group.forEach(element => {
        let data = {}
        data.value = element.length
        data.name = f(this, Reflect.get(element[0], field))
        result.push(data)
      })
      return result
    },
    getWorkingHourData () {
      let workinghour = {value: 0, name: 'Working Hour'}
      let nonworkinghour = {value: 0, name: 'NonWorking Hour'}
      this.suplogs.forEach(element => {
        if (this.inWorkingHour(element.sup_st_time) && this.inWorkingHour(element.sup_ed_time)) {
          workinghour.value = workinghour.value + element.hours
        } else {
          nonworkinghour.value = nonworkinghour.value + element.hours
        }
      })
      workinghour.value = (Number(workinghour.value.toFixed(2)))
      nonworkinghour.value = (Number(nonworkinghour.value.toFixed(2)))    
      return [workinghour, nonworkinghour]
    },
    inWorkingHour (supdate) {
      let compareTime = supdate.substring(11)
      if (compareTime < '08:30:00' || compareTime > '18:30:00') {
        return false
      }
      return true
    },
    generateSummary (docId, dataarr, title) {
      let myChart = this.$echarts.init(document.getElementById(docId))
      myChart.clear()
      let option = {
        title: {
          text: title,
          x: 'center'
        },
        series: [
          {
            name: 'name',
            type: 'pie',
            radius: '40%',
            center: ['50%', '50%'],
            data: dataarr,
            label: {
              normal: {
                formatter: '{b}\n{c}({d}%)',
                textStyle: {
                  fontWeight: 'normal',
                  fontSize: 10
                }
              }
            }
          }
        ]
      }
      myChart.setOption(option)
    },
    groupBy (array, f) {
      let groups = {}
      array.forEach(function (o) {
        let group = JSON.stringify(f(o))
        groups[group] = groups[group] || []
        groups[group].push(o)
      })
      return Object.keys(groups).map(function (group) {
        return groups[group]
      })
    },
    getCustomerbyID () {
      return function (instance, id) {
        return instance.$store.getters.getCustomerById(id)
      }
    },
    getUserbyID () {
      return function (instance, id) {
        return instance.$store.getters.getUserById(id)
      }
    },
    getTypebyID () {
      return function (instance, id) {
        return instance.$store.getters.getTypeById(id)
      }
    },
    getReporterbyID () {
      return function (instance, id) {
        return instance.$store.getters.getReporterById(id)
      }
    },
    getSystembyID () {
      return function (instance, id) {
        return instance.$store.getters.getModuleById(id)
      }
    },
    getStatusbyID () {
      return function (instance, id) {
        return instance.$store.getters.getSupStatusById(id)
      }
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.el-date-picker {
  width: 80%;
}
.charts {
  width: 300px;
  height: 300px;
}
.summary-total {
  float: left;
  font-size: small;
}
</style>
