<template>
  <div>
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item>Breakdown</el-breadcrumb-item>
      <el-breadcrumb-item>Ticket List (Total - {{totalCount}})</el-breadcrumb-item>
    </el-breadcrumb>
    <el-form :inline="true" style="display:flex;">
      <el-form-item>
        <el-input placeholder="Ticket" v-model="searchKeys.ticket_no__iexact"></el-input>
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
        prop="ticket_no"
        :label="columns[0]"
        width="120">
      </el-table-column>
      <el-table-column
        prop="customer"
        :label="columns[1]"
        width="120">
        <!-- <template slot-scope="scope">
          <span>{{getCustomerbyID(scope.row.customer)}}</span>
        </template> -->
      </el-table-column>
      <el-table-column
        prop="summary"
        :label="columns[3]">
      </el-table-column>
      <el-table-column
        prop="status"
        :label="columns[4]"
        width="100">
        <!-- <template slot-scope="scope">
          <span>{{getStatusbyID(scope.row.status)}}</span>
        </template> -->
      </el-table-column>
      <el-table-column
        prop="assignee"
        :label="columns[2]"
        width="130">
        <!-- <template slot-scope="scope">
          <span>{{getUserbyID(scope.row.assigned_user)}}</span>
        </template> -->
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
      <el-table-column label="Action" width="160">
        <template slot-scope="scope">
          <el-badge :value="scope.row.bkcount" class="item" type="info">
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
import { getAccessToken } from '../utils/auth'
import { api } from '../utils/api'
import axios from 'axios'
const BASE_URL = process.env.URL_ROOT

export default {
  name: 'Tickets',
  mounted: function () {
    this.loadTicket(1)
  },
  data () {
    return {
      searchKeys: {
        ticket_no__iexact: '',
        customer__icontains: '',
        assignee__icontains: '',
        summary__icontains: '',
        status__icontains: '',
        gn_no__icontains: ''
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
      generating: []
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
      let params = {
        keys: this.searchKeys,
        page: page
      }
      this.$store.dispatch('loadDocs', this)
      this.$store.dispatch('loadTickets', this, params)
    },
    handleGenerateDoc (ticket, index) {
      this.generating[index] = true
      axios.get(BASE_URL + '/api/breakdowns/doc/' + ticket.id + '/')
        .then(response => {
          this.generating = []
          console.log(response.data)
          if (response.data === 'NO_BREAKDOWN_FOUND') {
            this.$message.error('No breakdown found !')
          } else {
            this.$store.dispatch('loadDocs', this)
            this.$message.success('Documents created !')
          }
        })
        .catch(error => {
          this.generating = []
          this.$message.error(error.message)
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
      return './static/media/breakdown/' + ticket.ticket_no + '/FD-' + ticket.ticket_no + '.docx'
    },
    getXlxPath (ticket) {
      return './static/media/breakdown/' + ticket.ticket_no + '/Breakdown-' + ticket.ticket_no + '.xlsx'
    },
    handleBreakdown (ticket) {
      this.$store.dispatch('showBreakdown', this, ticket)
    },
    handleReset () {
      for (var key in this.searchKeys) {
        this.searchKeys[key] = ''
      }
    },
    async handleSyncTicket () {
      this.progressVisible = true
      this.oldCount = 0
      this.newCount = 0
      let url = '/api/jira/'
      let res = await api.get(url)
      console.log(res)
      let ticketUrl = '/api/tickets/'
      let header = { 'X-Authorization': 'JWT ' + getAccessToken(),
        'X-CSRFToken': this.$store.state.constants.csrToken
      }
      res.issues.forEach(issue => {
        this.retreiveTicket(issue)
          .then(response => {
            if (response) {
              let ticket = this.getUpdatedTicket(issue, response)
              let putUrl = ticketUrl + ticket.id + '/'
              api.put(putUrl, ticket, header)
                .catch(error => {
                  console.log(error)
                })
              this.oldCount++
            } else {
              api.post(ticketUrl, this.getNewTicket(issue), header)
                .catch(error => {
                  console.log(error)
                })
              this.newCount++
            }
          })
          .catch(error => {
            console.log(error)
          })
      })
      setTimeout(() => {
        this.loadTicket(1)
        this.progressVisible = false
        this.$message.success('Updated ' + this.oldCount + ' Tickets, Created ' + this.newCount + ' Tickets')
      }, 5000)
    },
    async retreiveTicket (jiraIssue) {
      let url = '/api/tickets/?page=1'
      this.handleReset()
      this.searchKeys.ticket_no__iexact = jiraIssue.key
      this.searchKeys.ticket_no__iexact = jiraIssue.key
      for (var key in this.searchKeys) {
        url += '&' + key + '=' + this.searchKeys[key]
      }
      console.log('retreive existing tickets.....................' + url)
      let res = await api.get(url)
      if (res.count > 0) {
        return res.results[0]
      } else {
        return null
      }
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
      ticket.customer = jiraIssue.fields.fixVersions.name
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
