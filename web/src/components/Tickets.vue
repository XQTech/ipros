<template>
  <el-main>
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/' }">Home</el-breadcrumb-item>
      <el-breadcrumb-item>Ticket List</el-breadcrumb-item>
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
        <el-button type="primary" @click="loadTicket(1)">Search</el-button>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="handleReset()">Reset</el-button>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="handleSyncTicket()" :loading="progressVisible">Sync JIRA</el-button>
      </el-form-item>
    </el-form>
    <el-table
      ref="filterTable"
      :data="ticketList"
      style="width: 100%">
      <el-table-column
        prop="ticket_no"
        :label="columns[0]"
        sortable
        width="120">
      </el-table-column>
      <el-table-column
        prop="customer"
        :label="columns[1]"
        width="120"
        sortable>
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
        width="100"
        sortable>
        <!-- <template slot-scope="scope">
          <span>{{getStatusbyID(scope.row.status)}}</span>
        </template> -->
      </el-table-column>
      <el-table-column
        prop="assignee"
        :label="columns[2]"
        width="130"
        sortable>
        <!-- <template slot-scope="scope">
          <span>{{getUserbyID(scope.row.assigned_user)}}</span>
        </template> -->
      </el-table-column>
      <el-table-column
        prop="gn_no"
        :label="columns[5]"
        width="100"
        sortable>
      </el-table-column>
      <el-table-column label="Action" width="100">
        <template slot-scope="scope">
          <el-button
            size="mini"
            type="primary"
            icon="el-icon-more"
            @click="handleBreakdown(scope.row)"></el-button>
        </template>
      </el-table-column>
    </el-table>
    <el-pagination
      background
      layout="prev, pager, next"
      :total="totalCount"
      @current-change="loadTicket">
    </el-pagination>
  </el-main>
</template>

<script>
import { mapState } from 'vuex'
import { getAccessToken } from '../../utils/auth'
import { api } from '../../utils/api'

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
        gn_no__icontains: ''
      },
      columns: [
        'Ticket No',
        'Customer',
        'Assigned To',
        'description',
        'Status',
        'GN'
      ],
      progressVisible: false,
      oldCount: 0,
      newCount: 0
    }
  },
  computed: {
    ...mapState({
      ticketList: state => state.ticket.ticketList,
      totalCount: state => state.ticket.totalCount,
      customers: state => state.customer.customers,
      users: state => state.user.users,
      statusList: state => state.ticketStatus.statusList
    })
  },
  methods: {
    loadTicket (page) {
      let params = {
        keys: this.searchKeys,
        page: page
      }
      this.$store.dispatch('loadTickets', params)
    },
    handleBreakdown (ticket) {
      this.$store.dispatch('showBreakdown', ticket)
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
      let url = 'http://localhost:8000/api/jira/'
      let res = await api.get(url)
      console.log(res)
      // let updatedTickets = []
      // let newTickets = []
      let ticketUrl = 'http://localhost:8000/api/tickets/'
      let header = { 'X-Authorization': 'JWT ' + getAccessToken(),
        'X-CSRFToken': this.$store.state.constants.csrToken
      }
      res.issues.forEach(issue => {
        this.retreiveTicket(issue)
          .then(response => {
            if (response) {
              // updatedTickets.push(this.getUpdatedTicket(issue, response))
              let ticket = this.getUpdatedTicket(issue, response)
              let putUrl = ticketUrl + ticket.id + '/'
              api.put(putUrl, ticket, header)
                .catch(error => {
                  console.log(error)
                })
              this.oldCount++
            } else {
              // newTickets.push(this.getNewTicket(issue))
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
        // this.syncTicket(updatedTickets, newTickets)
        this.loadTicket(1)
        this.progressVisible = false
        this.$message.success('Updated ' + this.oldCount + ' Tickets, Created ' + this.newCount + ' Tickets')
      }, 5000)
    },
    async retreiveTicket (jiraIssue) {
      let url = 'http://localhost:8000/api/tickets/?ticket_no__icontains=' + jiraIssue.key
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
    // async syncTicket (updatedTickets, newTickets) {
    //   let url = 'http://localhost:8000/api/tickets/'
    //   let header = { 'X-Authorization': 'JWT ' + getAccessToken(),
    //     'X-CSRFToken': this.$store.state.constants.csrToken
    //   }
    //   if (updatedTickets && updatedTickets.length > 0) {
    //     await api.put(url, updatedTickets, header)
    //   }
    //   if (newTickets && newTickets.length > 0) {
    //     await api.post(url, newTickets, header)
    //   }
    // },
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
.el-main {
  background-color: #EEF1F4;
}
.button-bar {
  float: right;
  padding-top: 2vh;
  padding-bottom: 1vh;
}
.el-pagination {
  margin-top: 2vh;
}
.el-breadcrumb {
  margin-bottom: 2vh;
}
</style>
