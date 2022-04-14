<template>
  <div class="row justify-content-center">
    <div class="col-lg-5 col-md-7">
      <div class="card bg-secondary shadow border-0">
        <div class="card-body px-lg-5 py-lg-5">
          <div class="text-center text-muted mb-4">
            <small>Log in with credentials</small>
          </div>
          <form name="loginform" role="form">
            <base-input
                class="input-group-alternative mb-3"
                placeholder="Username"
                addon-left-icon="fas fa-user"
                v-model="model.user"
            >
            </base-input>

            <base-input
                class="input-group-alternative"
                placeholder="Password"
                type="password"
                addon-left-icon="ni ni-lock-circle-open"
                v-model="model.password"
            >
            </base-input>

            <div class="text-center text-warning" v-if="errormessage">
              <small>Username or password are incorrect.</small>
            </div>

            <div class="text-center">
              <base-button type="primary" class="my-4" @click="signin"
              >Log in
              </base-button
              >
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { defaultPage } from "../../dashboard/entry/router";

export default {

  name: "login",
  data() {
    return {
      model: {
        user: "",
        password: "",
      },
      errormessage: false,
    };
  },
  methods: {

    sleep(milliseconds) {
      return new Promise(resolve => setTimeout(resolve, milliseconds));
    },

    async signin() {
      this.errormessage = false;
      this.$store.dispatch("signin", {user: this.model.user, pw: this.model.password}).then((response) => {

        if (response === 200) {
          this.sleep(1000);
          // window.location.reload();
          this.$store.dispatch("enableNotifications", true);
          this.$router.push(defaultPage).catch((e) => {
            console.log(e)
          });
        }
      }).catch((e) => {
        if (e === 400) {
          this.errormessage = true;
        }
      })
    },
  },
  mounted() {
    document.forms.namedItem("loginform").addEventListener("keypress", (evt) => {
      if (evt.key === 'Enter') {
        this.signin();
      }
    })
  },
};
</script>
<style></style>
