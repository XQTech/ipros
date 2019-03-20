<template>
  <div class="footer-panel">
    <el-row>
        <el-col :span="span" v-for="item in groupLink" v-bind:key="item.index">
            <p class="title">{{item[0].group}}</p>
            <li v-for="link in item" v-bind:key="link.index">
                {{link.name}}
            </li>
        </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  name: 'Footer',
  data () {
    return {
      links: [
        {id: 1, group: 'MIP', name: 'Website', link: 'http://mersinport.com.tr'},
        {id: 2, group: 'MIP', name: 'Website', link: 'http://mersinport.com.tr'},
        {id: 3, group: 'MIP', name: 'Website', link: 'http://mersinport.com.tr'},
        {id: 4, group: 'LIMAK', name: 'Website', link: 'http://mersinport.com.tr'},
        {id: 5, group: 'LIMAK', name: 'Website', link: 'http://mersinport.com.tr'},
        {id: 6, group: 'LIMAK', name: 'Website', link: 'http://mersinport.com.tr'}
      ]
    }
  },
  created: function () {
  },
  computed: {
    span () {
      return Math.floor(24 / this.groupLink.length)
    },
    groupLink () {
      let group = this.groupBy(this.links, function (item) {
        return [Reflect.get(item, 'group')]
      })
      return group
    }
  },
  methods: {
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
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.title {
    font-weight: bold;
    font-size: 10px;
    font-family: "Source Sans Pro", "Arial", sans-serif;
    color: #606266;
    padding: 3px;
}
ul, li {
    list-style:none;
    font-family: "Source Sans Pro", "Arial", sans-serif;
    font-size: 6px;
    padding: 3px;
    color: #606266;
}
.footer-panel {
    margin-top: 5px;
    margin-bottom: 20px;
}
</style>
