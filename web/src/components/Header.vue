<template>
  <el-header>
    <el-menu :default-active="activeIndex" mode="horizontal">
      <el-menu-item index="1" @select="handleSelect">My Tasks</el-menu-item>
      <el-menu-item index="2" @select="handleSelect">Messages</el-menu-item>
      <el-menu-item index="3"><a href="http://localhost:8000/admin" target="_blank">Admin</a></el-menu-item>
      <el-menu-item index="4" class="profile"><a href="http://localhost:8000/admin/password_change/" target="_blank">Change Password</a></el-menu-item>
    </el-menu>
  </el-header>
</template>

<script>
export default {
  name: 'Header'
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.el-menu-item {
  text-align: left;
}
</style>
