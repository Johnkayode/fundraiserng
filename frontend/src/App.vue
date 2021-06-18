<template>
  <div>
    <div class="nav-item">
          <router-link to="/" class="nav-link">
            Home
          </router-link>
          <router-link to="/login" class="nav-link">
            Login
          </router-link>
          <div class="container">
            <router-view></router-view>
          </div>
    </div>
  </div>
</template>


<script>



export default {
  name: 'App',
  components: {
 
  }
}
</script>

<style>
  #app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
  }
</style>
