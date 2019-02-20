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
      <!-- <el-form-item>
        <el-select v-model="searchKeys.customer__icontains" placeholder="Customer">
          <el-option value=""></el-option>
          <el-option v-for="(customer,index) in customers"
            v-bind:key="index"
            :label="customer.name"
            :value="customer.id"></el-option>
        </el-select>
      </el-form-item> -->
      <el-form-item>
        <el-input placeholder="Customer" v-model="searchKeys.customer__icontains"></el-input>
      </el-form-item>
      <!-- <el-form-item>
        <el-select v-model="searchKeys.assignee__icontains" placeholder="Assigned To">
          <el-option value=""></el-option>
          <el-option v-for="(user,index) in users"
            v-bind:key="index"
            :label="user.username"
            :value="user.id"></el-option>
        </el-select>
      </el-form-item> -->
      <el-form-item>
        <el-input placeholder="Assigned to" v-model="searchKeys.assignee__icontains"></el-input>
      </el-form-item>
      <!-- <el-form-item>
        <el-select v-model="searchKeys.status__icontains" placeholder="Status">
          <el-option value=""></el-option>
          <el-option v-for="(status,index) in statusList"
            v-bind:key="index"
            :label="status.code"
            :value="status.id"></el-option>
        </el-select>
      </el-form-item> -->
      <el-form-item>
        <el-input placeholder="Status" v-model="searchKeys.status__icontains"></el-input>
      </el-form-item>
      <el-form-item>
        <el-input placeholder="Description" v-model="searchKeys.summary__icontains" style="width:300px;"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="handleSearch()">Search</el-button>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="handleReset()">Reset</el-button>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="handleSyncTicket()" :loading="progressVisible">Sync Tickets</el-button>
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
        width="100"
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
        width="120"
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
      <el-table-column label="Action" width="200">
        <template slot-scope="scope">
          <el-button
            size="mini"
            type="primary"
            icon="el-icon-more"
            @click="handleBreakdown(scope.row)"></el-button>
          <el-button
            size="mini"
            type="danger"
            icon="el-icon-delete"
            @click="handleDelete(scope.row)"></el-button>
        </template>
      </el-table-column>
    </el-table>
    <el-pagination
      background
      layout="prev, pager, next"
      :total="totalCount"
      @current-change="handleCurrentChange">
    </el-pagination>
  </el-main>
</template>

<script>
import { mapState } from 'vuex'
// import axios from 'axios'
import { getAccessToken } from '../../utils/auth'
import { api } from '../../utils/api'

export default {
  name: 'Tickets',
  mounted: function () {
    this.$store.dispatch('loadTickets', 1)
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
      progressVisible: false
    }
  },
  computed: {
    ...mapState({
      ticketList: state => state.ticket.ticketList,
      totalCount: state => state.ticket.totalCount,
      customers: state => state.customer.customers,
      users: state => state.user.users,
      statusList: state => state.ticketStatus.statusList
    }),
    getStatusbyID () {
      return function (id) {
        return this.$store.getters.getStatusById(id)
      }
    },
    getCustomerbyID () {
      return function (id) {
        return this.$store.getters.getCustomerById(id)
      }
    },
    getUserbyID () {
      return function (id) {
        return this.$store.getters.getUserById(id)
      }
    }
  },
  methods: {
    handleCurrentChange (page) {
      this.$store.dispatch('loadTickets', page)
    },
    handleBreakdown (ticket) {
      console.log('ticket no: ' + ticket.ticket_no)
      console.log('breakdown: ' + ticket.breakdowns)
      console.log('customer: ' + ticket.customer)
      this.$store.dispatch('showBreakdown', ticket)
    },
    handleSearch () {
      console.log(this.searchKeys)
      this.$store.dispatch('searchTickets', this.searchKeys)
    },
    handleReset () {
      for (var key in this.searchKeys) {
        this.searchKeys[key] = ''
      }
    },
    async handleSyncTicket () {
      this.progressVisible = true
      this.current_step = 0
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
            } else {
              // newTickets.push(this.getNewTicket(issue))
              api.post(ticketUrl, this.getNewTicket(issue), header)
                .catch(error => {
                  console.log(error)
                })
            }
          })
          .catch(error => {
            console.log(error)
          })
      })
      setTimeout(() => {
        // this.syncTicket(updatedTickets, newTickets)
        this.handleSearch()
        this.progressVisible = false
      }, 5000)
      // axios.get('http://localhost:8000/api/jira/')
      //   .then(response => {
      //     let updatedTickets = []
      //     let newTickets = []
      //     console.log('1111111111111111111111')
      //     response.data.issues.forEach(issue => {
      //       let ticket = this.retreiveTicket(issue)
      //       if (ticket) {
      //         updatedTickets.push(this.getUpdatedTicket(issue, ticket))
      //       } else {
      //         newTickets.push(this.getNewTicket(issue))
      //       }
      //     })
      //     console.log('222222222222222222')
      //     this.syncTicket(updatedTickets, newTickets)
      //     console.log('33333333333333333333333')
      //     this.handleSearch()
      //     console.log('44444444444444444444444444')
      //     this.progressVisible = false
      //   })
      //   .catch(error => {
      //     console.log(error)
      //     this.progressVisible = false
      //   })
    },
    async retreiveTicket (jiraIssue) {
      let url = 'http://localhost:8000/api/tickets/?ticket_no__icontains=' + jiraIssue.key
      let res = await api.get(url)
      if (res.count > 0) {
        return res.results[0]
      } else {
        return null
      }
      // axios.get(url)
      //   .then(response => {
      //     if (response.data.count > 0) {
      //       return response.data[0]
      //     } else {
      //       return null
      //     }
      //   })
      //   .catch(error => {
      //     console.log(error)
      //   })
    },
    getUpdatedTicket (jiraIssue, ticket) {
      return this.setTicket(jiraIssue, ticket)
    },
    async syncTicket (updatedTickets, newTickets) {
      let url = 'http://localhost:8000/api/tickets/'
      let header = { 'X-Authorization': 'JWT ' + getAccessToken(),
        'X-CSRFToken': this.$store.state.constants.csrToken
      }
      if (updatedTickets && updatedTickets.length > 0) {
        await api.put(url, updatedTickets, header)
      }
      if (newTickets && newTickets.length > 0) {
        await api.post(url, newTickets, header)
      }
      // axios.put('http://localhost:8000/api/tickets/', updatedTickets, {
      //   headers: { 'X-Authorization': 'JWT ' + getAccessToken(),
      //     'X-CSRFToken': this.$store.state.constants.csrToken
      //   }})
      //   .then(response => {
      //     console.log(' updated ' + updatedTickets.count + ' tickets')
      //   })
      //   .catch(error => {
      //     console.log(error)
      //   })
      // axios.post('http://localhost:8000/api/tickets/', newTickets, {
      //   headers: { 'X-Authorization': 'JWT ' + getAccessToken(),
      //     'X-CSRFToken': this.$store.state.constants.csrToken
      //   }})
      //   .then(response => {
      //     console.log(' created ' + newTickets.count + ' tickets')
      //   })
      //   .catch(error => {
      //     console.log(error)
      //   })
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
