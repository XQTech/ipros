<template>
    <div class="login-wrap">
        <div class="ms-title">Log In</div>
        <div class="ms-login">
            <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="0px">
                <el-form-item prop="username">
                    <el-input v-model="ruleForm.username" placeholder="Username"></el-input>
                </el-form-item>
                <el-form-item prop="password">
                    <el-input type="password" placeholder="Password" v-model="ruleForm.password" @keyup.enter.native="submitForm('ruleForm')"></el-input>
                </el-form-item>
                <div class="login-btn">
                    <el-button type="primary" @click="handleLogin">Login</el-button>
                </div>
                <p v-show="state" style="font-size:12px;line-height:30px;color:#ff1800;">Invalid Username or Passowrd</p>
            </el-form>
        </div>
    </div>
</template>

<script>
import { login, isLoggedIn } from '../../utils/auth'

export default {
  name: 'Login',
  components: {},
  data: function () {
    return {
      ruleForm: {
        username: '',
        password: ''
      },
      rules: {
        username: [
          { required: true, message: 'Please input username', trigger: 'blur' }
        ],
        password: [
          { required: true, message: 'Please input password', trigger: 'blur' }
        ]
      },
      state: false
    }
  },
  methods: {
    handleLogin () {
      login(this.ruleForm.username, this.ruleForm.password)
      setTimeout(() => {
        if (isLoggedIn()) {
          this.$router.push({ name: 'Home' })
        } else {
          this.$message.error('Invalid username or password')
        }
      }, 1000)
      // TODO: read https://stackoverflow.com/questions/35664550/vue-js-redirection-to-another-page
    },
    isLoggedIn () {
      console.log('isLoggedIn: ', isLoggedIn())
      return isLoggedIn()
    }
  },
  created () {
    if (isLoggedIn()) {
      this.$router.push({ name: 'Home' })
    }
  },
  mounted () {
    console.log('mounted')
  },
  beforeUpdate () {},
  updated () {}
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.login-wrap {
  position: relative;
  width: 100%;
  height: 100%;
}
.ms-title {
  position: absolute;
  top: 50%;
  width: 100%;
  margin-top: -230px;
  text-align: center;
  font-size: 30px;
}
.ms-login {
  position: absolute;
  left: 50%;
  top: 50%;
  width: 300px;
  height: 160px;
  margin: -200px 0 0 -190px;
  padding: 40px;
  border-radius: 5px;
}
.login-btn {
  text-align: center;
}
.login-btn button {
  width: 100%;
  height: 36px;
}
</style>
