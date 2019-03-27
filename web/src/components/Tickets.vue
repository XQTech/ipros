<template>
  <div>
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item>Breakdown</el-breadcrumb-item>
      <el-breadcrumb-item>Ticket List (Total - {{totalCount}})</el-breadcrumb-item>
    </el-breadcrumb>
    <el-form :inline="true" style="display:flex;">
      <el-form-item>
        <el-input placeholder="Ticket" v-model="searchKeys.ticket_no__icontains"></el-input>
      </el-form-item>
      <el-form-item>
        <el-input placeholder="Customer" v-model="searchKeys.customer__icontains"></el-input>
      </el-form-item>
      <el-form-item>
        <el-input placeholder="Assigned to" v-model="searchKeys.assignee__icontains"></el-input>
      </el-form-item>
      <el-form-item>
        <el-input placeholder="Status" v-model="searchKeys.status__icontains"></el-input>
      </el-form-item>
      <el-form-item>
        <el-input placeholder="Description" v-model="searchKeys.summary__icontains" style="width:300px;"></el-input>
      </el-form-item>
      <el-form-item>
        <el-input placeholder="GN" v-model="searchKeys.gn_no__icontains"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="loadTicket(1)" icon="fa fa-search"></el-button>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="handleReset()" icon="fa fa-undo"></el-button>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="handleSyncTicket()" :loading="progressVisible"
         icon="fa fa-refresh"> JIRA</el-button>
      </el-form-item>
    </el-form>
    <el-table
      :data="ticketList"
      style="width: 100%">
      <el-table-column
        :label="columns[0]"
        width="120">
        <template slot-scope="scope">
          <a :href="getJiraPath(scope.row)"
            target="_blank"
            class="buttonText">{{scope.row.ticket_no}}</a>
        </template>
      </el-table-column>
      <el-table-column
        prop="customer"
        :label="columns[1]"
        width="120">
      </el-table-column>
      <el-table-column
        prop="summary"
        :label="columns[3]"
        min-width="260"
        :show-overflow-tooltip="true">
      </el-table-column>
      <el-table-column
        prop="status"
        :label="columns[4]"
        width="100">
      </el-table-column>
      <el-table-column
        prop="assignee"
        :label="columns[2]"
        width="130">
      </el-table-column>
      <el-table-column
        prop="gn_no"
        :label="columns[5]"
        width="120">
      </el-table-column>
      <el-table-column
        label="Documents"
        width="220">
        <template slot-scope="scope">
          <a :href="getDocPath(scope.row)"
            class="buttonText" download>{{getDocName(scope.row)[0]}}</a><br>
          <a :href="getXlxPath(scope.row)"
            class="buttonText" download>{{getDocName(scope.row)[1]}}</a>
        </template>
      </el-table-column>
      <el-table-column label="Action" width="200">
        <template slot-scope="scope">
          <el-badge :value="scope.row.bkcount" class="item" :type="getBadgeType(scope.row.restdays)">
            <el-button
            size="mini"
            type="primary"
            icon="el-icon-more"
            @click="handleBreakdown(scope.row)"></el-button>
          </el-badge>
          <el-button
          size="mini"
          type="primary"
          icon="fa fa-file-word-o"
          @click="handleGenerateDoc(scope.row, scope.$index)"
          :loading="generating[scope.$index]"></el-button>
          <el-button
          size="mini"
          type="primary"
          icon="fa fa-upload"
          @click="handleUploadDoc(scope.row, scope.$index)"
          :loading="uploading[scope.$index]"></el-button>
        </template>
      </el-table-column>
    </el-table>
    <el-pagination
      background
      layout="prev, pager, next"
      :total="totalCount"
      @current-change="loadTicket">
    </el-pagination>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import Vue from 'vue'
export default {
  name: 'Tickets',
  mounted: function () {
    this.loadTicket(1)
  },
  data () {
    return {
      searchKeys: {
        ticket_no__icontains: '',
        customer__icontains: '',
        assignee__icontains: '',
        summary__icontains: '',
        status__icontains: '',
        gn_no__icontains: '',
        jira_id__iexact: ''
      },
      columns: [
        'Ticket No',
        'Customer',
        'Assigned To',
        'Description',
        'Status',
        'GN'
      ],
      progressVisible: false,
      oldCount: 0,
      newCount: 0,
      generating: [],
      uploading: [],
      params: {
        self: this,
        keys: [],
        page: 1,
        item: null,
        id: 0
      }
    }
  },
  computed: {
    ...mapState({
      ticketList: state => state.ticket.ticketList,
      totalCount: state => state.ticket.totalCount,
      customers: state => state.customer.customers,
      users: state => state.user.users,
      statusList: state => state.ticketStatus.statusList,
      docList: state => state.ticket.docList
    })
  },
  methods: {
    loadTicket (page) {
      this.params.page = page
      this.params.keys = this.searchKeys
      this.$store.dispatch('loadDocs', this.params)
      this.$store.dispatch('loadTickets', this.params)
    },
    handleUploadDoc (ticket, index) {
      Vue.set(this.uploading, index, true)
      this.$http.get('/api/jira/upload/' + ticket.id + '/')
        .then(response => {
          Vue.set(this.uploading, index, false)
          if (response.data === 'failed') {
            this.$message.error('Failed to Upload !')
          } else {
            this.$message.success('Documents uploaded to JIRA !')
          }
        })
        .catch(error => {
          Vue.set(this.uploading, index, false)
          this.$message.error(error)
        })
    },
    handleGenerateDoc (ticket, index) {
      Vue.set(this.generating, index, true)
      this.$http.get('/api/breakdowns/doc/' + ticket.id + '/')
        .then(response => {
          Vue.set(this.generating, index, false)
          this.$store.dispatch('loadDocs', this.params)
          this.$message.success('Documents created !')
        })
        .catch(error => {
          Vue.set(this.generating, index, false)
          this.$message.error(error)
        })
    },
    getDocName (ticket) {
      var i
      for (i in this.docList) {
        let doc = this.docList[i]
        if (doc.ticket === ticket.ticket_no) {
          return doc.docs
        }
      }
      return ''
    },
    getDocPath (ticket) {
      let docName = this.$store.getters.getConfigByKey('DOC_FD_NAME')
      return '../media/breakdown/' + ticket.ticket_no + '/' + docName.replace('{0}', ticket.ticket_no) + '.docx'
    },
    getXlxPath (ticket) {
      let docName = this.$store.getters.getConfigByKey('DOC_BK_NAME')
      return '../media/breakdown/' + ticket.ticket_no + '/' + docName.replace('{0}', ticket.ticket_no) + '.xlsx'
    },
    getJiraPath (ticket) {
      let jiraurl = this.$store.getters.getConfigByKey('JIRA_SERVER')
      return jiraurl + '/browse/' + ticket.ticket_no
    },
    handleBreakdown (ticket) {
      this.params.item = ticket
      this.$store.dispatch('showBreakdown', this.params)
    },
    handleReset () {
      for (var key in this.searchKeys) {
        this.searchKeys[key] = ''
      }
    },
    getBadgeType (restdays) {
      let warndays = this.$store.getters.getConfigByKey('WARN_DUE_DAYS')
      if (restdays > 0 && restdays <= warndays) {
        return 'warning'
      } else if (restdays <= 0) {
        return 'danger'
      }
      return 'info'
    },
    handleSyncTicket () {
      this.progressVisible = true
      this.oldCount = 0
      this.newCount = 0
      this.$http.get('/api/jira/')
        .then(response => {
          response.data.issues.forEach(issue => {
            this.retreiveTicket(issue)
              .then(resp => {
                if (resp) {
                  let ticket = this.getUpdatedTicket(issue, resp)
                  this.$http.put('/api/tickets/' + ticket.id + '/', ticket)
                    .catch(error => {
                      this.$message.error(error)
                    })
                  this.oldCount++
                } else {
                  this.$http.post('/api/tickets/', this.getNewTicket(issue))
                    .catch(error => {
                      this.$message.error(error)
                    })
                  this.newCount++
                }
              })
              .catch(error => {
                this.progressVisible = false
                this.$message.error(error)
              })
          })
          setTimeout(() => {
            this.handleReset()
            this.loadTicket(1)
            this.progressVisible = false
            this.$message.success('Updated ' + this.oldCount + ' Tickets, Created ' + this.newCount + ' Tickets')
          }, 5000)
        })
        .catch(error => {
          this.progressVisible = false
          this.$message.error(error)
        })
    },
    retreiveTicket (jiraIssue) {
      let url = '/api/tickets/?page=1'
      this.handleReset()
      this.searchKeys.jira_id__iexact = jiraIssue.id
      for (var key in this.searchKeys) {
        url += '&' + key + '=' + this.searchKeys[key]
      }
      return new Promise((resolve, reject) => {
        this.$http.get(url)
          .then(response => {
            if (response.data.count > 0) {
              resolve(response.data.results[0])
            } else {
              resolve(null)
            }
          })
      })
    },
    getUpdatedTicket (jiraIssue, ticket) {
      return this.setTicket(jiraIssue, ticket)
    },
    getNewTicket (jiraIssue) {
      let ticket = {
        status: '',
        customer: '',
        assignee: '',
        ticket_no: '',
        summary: '',
        due_date: '',
        gn_no: '',
        jira_id: ''
      }
      return this.setTicket(jiraIssue, ticket)
    },
    setTicket (jiraIssue, ticket) {
      ticket.status = jiraIssue.fields.status.name
      ticket.customer = jiraIssue.fields.fixVersions[0].name
      ticket.assignee = jiraIssue.fields.assignee.name
      ticket.ticket_no = jiraIssue.key
      ticket.summary = jiraIssue.fields.summary
      ticket.due_date = jiraIssue.fields.duedate
      ticket.gn_no = jiraIssue.fields.customfield_10112
      ticket.jira_id = jiraIssue.id
      return ticket
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
.item {
  margin-top: 10px;
  margin-right: 15px;
  margin-bottom: 7px;
}
</style>
