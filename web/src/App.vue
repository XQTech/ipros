<template>
  <el-container v-if="$route.meta.keepAlive" id='App'>
    <el-header>
      <Header></Header>
    </el-header>
    <el-main>
      <router-view></router-view>
    </el-main>
    <!-- <el-footer>
      <Footer></Footer>
    </el-footer> -->
  </el-container>
  <div v-else id='App'>
    <router-view/>
  </div>
</template>

<script>
import Header from '@/components/Header'
import Footer from '@/components/Footer'
import { isLoggedIn } from './utils/auth'
export default {
  name: 'App',
  components: {
    Header,
    Footer
  },
  created: function () {
    if (!isLoggedIn()) {
      this.$router.push({ name: 'Login' })
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  position: absolute;
  top: 0;
  bottom: 0;
  right: 0;
  left: 0;
}
.el-main {
  background-color: #EEF1F4;
}
body {
  margin: 0px;
}
</style>
