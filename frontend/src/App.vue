<template>
  <div class='overflow-hidden'>
    <nav class="navbar navbar-expand-lg navbar-light bg-light justify-content-between fixed-top">
      <a class="navbar-brand" href="#">
        <img :src="require(`@/assets/logo.png`)" class="d-inline-block brand-image" alt="logo">
      </a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav ml-auto">
          <li class="nav-item active" data-toggle="collapse" data-target=".navbar-collapse.show">
            <router-link to="/" class="nav-link sr-only">
              Home
            </router-link>
          </li>
          <li class="nav-item dropdown" data-toggle="collapse" data-target=".navbar-collapse.show">
            <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
              Fundraise For
            </a>
            <div class="dropdown-menu" aria-labelledby="navbarDropdown">
              <a class="dropdown-item" href="#">Health</a>
              <a class="dropdown-item" href="#">Emergency</a>
              <a class="dropdown-item" href="#">Education</a>
              <a class="dropdown-item" href="#">Charity</a>
            </div>
          </li>
          <li class="nav-item" data-toggle="collapse" data-target=".navbar-collapse.show">
            <a class="nav-link" href="#">How It Works</a>
          </li>
        </ul>
        <span class="form-inline my-2 my-lg-0 mt-2">
          <router-link to="/register" class="btn btn-outline-success px-4 my-2 my-sm-0 mr-4 signup mt-4" data-toggle="collapse" data-target=".navbar-collapse.show">
            Sign Up
          </router-link>
          <router-link to="/login" class="btn btn-success px-4 my-2 my-sm-0 ml-4 signin mt-4" data-toggle="collapse" data-target=".navbar-collapse.show">
            Sign In
          </router-link>
        </span>
      </div>
    </nav>
    <div class="">
      <router-view></router-view>
    </div>
  </div>
</template>


<script>



import { library } from '@fortawesome/fontawesome-svg-core'
import { faUserSecret } from '@fortawesome/free-solid-svg-icons'




library.add(faUserSecret);

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

  textarea:focus,
  input[type='text']:focus,
  input[type='email']:focus,
  input[type='password']:focus{
    outline:0 none;
    border: 1px solid green;
    /* box-shadow: 0 0 0 0.2rem rgba(40, 167, 69, 0.25); */
    box-shadow: none;
    transition: 0.2s ease;
  }

  .btn{
    border-radius: 2px !important;
    padding: 5px 20px !important;
  }



  .navbar{
    padding: 0 20px;
    margin: 0;
    width: 100%;
  }

  .brand-image{
      height: auto;
      width: 250px;
  }


  .navbar-nav{
    margin-left: auto;
    margin-right: 20px;
  }

  .signup{
    margin-right: 15px;
  }

  .navbar-light .navbar-toggler{
    border: none;
    outline: none;
  }
  
  .navbar-light .navbar-toggler:focus{
    border: none;
    outline: none;
    box-shadow: none;
  }

  .navbar-light .navbar-toggler-icon{
    background-image: none;
    height: 2px;
    width: 24px;
    position: relative;
    background-color: green;
  }

  .navbar-light .navbar-toggler-icon::before{
    content:'';
    position: absolute;
    height: 2px;
    width: 100%;
    left: 0;
    top: -6px;
    background-color: green;
  }

  .navbar-light .navbar-toggler-icon::after{
    content:'';
    position: absolute;
    height: 2px;
    width: 100%;
    left: 0;
    top: 6px;
    background-color: green;
}

  .navbar-toggler {
      background-color: green;
      margin-right: 10px;
      padding: 7px;
      
  }

  .navbar-toggler:focus{
      box-shadow: none;
      outline: none;
      border: none;
  }

  .navbar-nav .nav-item{
    text-align: left;
  }

  .navbar-nav .dropdown .dropdown-menu{
    border: none;
  }

  @media screen and (max-width: 370px){
    .brand-image{
      width: 200px;
    }
  }

  @media screen and (max-width: 450px){
    .navbar-nav .nav-item{
      padding: 12px 0px 0px 12px;
    }

    .signin
    .signup{
      margin-top: 20px;
    }
  }
</style>
