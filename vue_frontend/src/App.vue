<template>
  <div id="app">
    <notifications></notifications>
    <router-view/>
  </div>
</template>

<script>
import {mapGetters} from "vuex";

export default {
  name: "App",
  data() {
    return {
      showNotifications: false,
      notificationModal: false,
    }

  },
  methods: {
    notify(title, message) {
      this.notificationModal = true;
      this.$notify({
        title: "" + title + "",
        message: "" + message + "",
        closeOnClick: true,
        timeout: 50000,
        icon: "fa fa-exclamation-triangle",
      });
    },
  },
  watch: {
    ownNotifications() {
      console.debug('App.vue ownNotifications this');
      for (var i = 0; i < this.ownNotifications.length; i++) {
        let title, message;
        if (this.ownNotifications[i].message && this.ownNotifications[i].title){
          // TODO only show these messages in dev/debug. Otherwise show more user friendly error.
          title = this.ownNotifications[i].title;
          message = this.ownNotifications[i].message;
        } else {
          title = this.ownNotifications[i];
          message = this.ownNotifications[i];
        }
        this.notify(title, message);
      }

      if (this.ownNotifications.length > 3) {
        this.$notifications.setOptions({overlap: true});
      }
    },
  },
  computed: {
    ...mapGetters(["ownNotifications"]),
  },

  created() {
    var timeOutObj_fix = setTimeout(function () {
      localStorage.clear();
      this.$store.dispatch("signout");
      this.$store.dispatch("closeSocket");
      window.location = "/";
    }, 60*60*1000);

    var timeOutObj = setTimeout(function () {
      localStorage.clear();
      this.$store.dispatch("signout");
      this.$store.dispatch("closeSocket");
      window.location = "/";
    }, 60*60*1000);


    window.addEventListener('click', () => {
      //if inactive for one hour, log out automatically
      if (typeof timeOutObj != "undefined") {
        clearTimeout(timeOutObj);
      }
      timeOutObj = timeOutObj_fix;
    })

    //fix for touch devices
    window.addEventListener('touchstart', () => {
      //if inactive for one hour, log out automatically
      if (typeof timeOutObj != "undefined") {
        clearTimeout(timeOutObj);
      }
      timeOutObj = timeOutObj_fix;
    });
  },

  beforeDestroy() {
    localStorage.clear();
    this.$store.dispatch("signout");
  }
};
</script>

<style>
a.h4.mb-0.text-white.text-uppercase.d-none.d-lg-inline-block.active.router-link-active, li.dropdown.nav-link.pr-0.dropdown {
  /*color: #8898aa!important;*/
  color: #32325d !important;
}

#sidenav-collapse-main .nav-link:hover {
  background-color: rgb(219, 229, 243) !important;
  /*background-color: #f8f9fe!important;*/
}

@media (min-width: 768px) {
  .navbar-expand-md .navbar-nav .dropdown-menu {

    margin-left: -100px;
  }
}

body.modal-open {
  overflow: hidden;
}

input.vdatetime-input {
  display: none !important;
}
</style>
