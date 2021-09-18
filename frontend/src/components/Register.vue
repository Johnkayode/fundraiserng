<template>
    <div class="my-container">
        <div class="row">
          <div class="col-lg-12">
            <div class="bg-white rounded px-3 form-card mx-auto">
                <Form @submit="handleRegister" :validation-schema="schema">
                    <div>
                    <div class="form-group">
                        <div class="alert mt-2" :class="message.status" role="alert" v-if="message">
                            {{ message.text }}
                        </div>
                    </div>
                    <div class="form-group mb-4">
                        <label for="first_name" class='text-small text-muted mb-2'>First Name</label>
                        <Field name="first_name" type="text" class="form-control" />
                        <ErrorMessage name="first_name" class="error-feedback text-danger small" />
                    </div>
                    <div class="form-group mb-4">
                        <label for="last_name" class='text-small text-muted mb-2'>Last Name</label>
                        <Field name="last_name" type="text" class="form-control" />
                        <ErrorMessage name="last_name" class="error-feedback text-danger small" />
                    </div>
                    <div class="form-group mb-4">
                        <label for="email" class='text-small text-muted mb-2'>Email</label>
                        <Field name="email" type="email" class="form-control" />
                        <ErrorMessage name="email" class="error-feedback text-danger small" />
                    </div>
                    <div class="form-group mb-4">
                        <label for="password" class='text-small text-muted mb-2'>Password</label>
                        <Field name="password" type="password" class="form-control" />
                        <ErrorMessage name="password" class="error-feedback text-danger small" />
                    </div>

                    <div class="form-group text-start">
                        <button class="btn btn-success btn-sm btn-block px-4 py-2" :disabled="loading">
                            <span
                            v-show="loading"
                            class="spinner-border spinner-border-sm me-2">
                            </span>
                            <span>Create your account</span>
                        </button>
                    </div>

                    </div>
                </Form>
                
                <div class='row'>
                    <div class="col-lg-12">
                        <p class='text-muted text-start mt-4 small'>Already have an account? 
                            <router-link to="/" class="text-success">Sign in</router-link></p>
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
  name: "Register",
  components: {
    Form,
    Field,
    ErrorMessage,
  },
  data() {
    const schema = yup.object().shape({
      first_name: yup
        .string()
        .required("First name is required!")
        .min(2, "Must be at least 2 characters!")
        .max(20, "Must be maximum 20 characters!"),
      last_name: yup
        .string()
        .required("Last name is required!")
        .min(2, "Must be at least 2 characters!")
        .max(20, "Must be maximum 20 characters!"),
      email: yup
        .string()
        .required("Email is required!")
        .email("Email is invalid!")
        .max(50, "Must be maximum 50 characters!"),
      password: yup
        .string()
        .required("Password is required!")
        .min(6, "Must be at least 6 characters!")
        .max(40, "Must be maximum 40 characters!"),
    });

    return {
      successful: false,
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
  mounted() {
    if (this.loggedIn) {
      this.$router.push("/profile");
    }
  },
  methods: {
    handleRegister(user) {
      this.message = "";
      this.successful = false;
      this.loading = true;

      this.$store.dispatch("auth/register", user).then(
        () => {
          this.message = "";
          this.successful = true;
          this.$router.push("/confirm");
        },
        (error) => {
          this.message = {"text":(error.response.data.email.toString() ||
              error.response ||
              error.response.data ||
              error.response.data.message ||
            error.message ||
            error.toString()),"status":'alert-danger'};
          this.successful = false;
          this.loading = false;
        }
      );
    },
  },
};
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