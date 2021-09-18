<template>
    <div class="my-container">
        <div class="row">
          <div class="col-lg-12">
            <div class="bg-white rounded px-3 form-card mx-auto">
                <Form @submit="handleLogin" :validation-schema="schema">
                    <div class="form-group">
                        <div class="alert alert-danger mt-2" role="alert" v-if="message">
                            {{ message }}
                        </div>
                    </div>

                    <div class="form-group mb-5">
                        <label for="email" class='text-small text-muted mb-2'>Email address</label>
                        <Field name="email" type="email" class="form-control" />
                        <ErrorMessage name="email" class="error-feedback" />
                    </div>
                    <div class="form-group mb-3">
                        <label for="password" class='text-small text-muted mb-2'>Password</label>
                        <Field name="password" type="password" class="form-control" />
                        <ErrorMessage name="password" class="error-feedback" />
                    </div>

                    <div class='row mb-5 text-start'>
                      <div class="col-lg-12">
                          <a href='#' class='small text-success'>Forgot your password?</a>
                      </div>
                    </div>

                    <div class="form-group text-start">
                        <button class="btn btn-success btn-sm btn-block px-4 py-2" :disabled="loading">
                            <span
                            v-show="loading"
                            class="spinner-border spinner-border-sm me-2">
                            </span>
                            <span>Sign in to your account</span>
                        </button>
                    </div>

                    
                </Form>
                
                <div class='row'>
                    <div class="col-lg-12">
                        <p class='text-muted text-start mt-4 small'>Don't have an account yet? <a href='#' class='text-success'>Register</a></p>
                    </div>
                </div>

            </div>
          </div>
        </div>
    </div>
    
</template>


<script>
import { Form, Field, ErrorMessage } from "vee-validate";
import * as yup from "yup";

export default {
  name: "Login",
  components: {
    Form,
    Field,
    ErrorMessage,
  },
  data() {
    const schema = yup.object().shape({
      email: yup.string().required("Email is required!"),
      password: yup.string().required("Password is required!"),
    });

    return {
      loading: false,
      message: "",
      schema,
    };

  },
  computed: {
    loggedIn() {
      return this.$store.state.auth.status.loggedIn;
    },
  },
  created() {
    if (this.loggedIn) {
      this.$router.push("/dashboard");
    }
  },
   methods: {
        handleLogin(user) {
            this.loading = true;

            this.$store.dispatch("auth/login", user).then(
            () => {
                this.$router.push("/dashboard");
            },
            (error) => {
                this.loading = false;
                this.message = 'Email or password is incorrect'
                this.error_mssg = (error.response &&
                    error.response.data &&
                    error.response.data.message) ||
                error.message ||
                error.toString();
            }
            );
        },
  },
}



</script>


<style scoped>
.my-container{
  margin: 70px 0px 0px;
  padding: 0px 80px;
}

.body-text{
  font-size: 50px;
  font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
  font-weight: 800;
  text-align: left;
}

.form-card{
  padding: 50px 0px 50px 0px;
  max-width: 500px;
}

label{
  text-align: left;
  float: left;
}


@media screen and (max-width: 450px) {
  .my-container{
    margin: 70px 0px;
    padding: 0px 10px;
  }

  .body-text{
    margin-bottom: 50px;
  }

}


</style>
