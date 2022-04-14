<!--
Author: Jennifer Horstmann
-->

<template>
  <base-nav
      class="navbar-top pt-4 mt-1 navbar-dark"
      id="navbar-main"
      :show-toggle-button="false"
      expand
  >
    <ul class="navbar-nav align-items-center d-none d-md-flex ml-lg-auto">
      <li class="nav-item dropdown">
        <base-dropdown class="nav-link pr-0">
          <div class="media align-items-center" slot="title">
            <div class="media-body ml-2 d-none d-lg-block">
              <span class="mb-0 text-sm  mr-3 font-weight-bold">{{ this.username }}</span>
              <i class="ni ni-single-02"></i>
            </div>
          </div>

          <template>
            <div class="dropdown-divider"></div>
            <a href="#" class="dropdown-item" @click="signout">
              <i class="ni ni-user-run"></i>
              <span>Logout</span>
            </a>
          </template>
        </base-dropdown>
      </li>
    </ul>
  </base-nav>
</template>
<script>

import {mapGetters} from 'vuex'

export default {
  data() {
    return {
      activeNotifications: false,
      showMenu: false,
      searchQuery: "",
    };
  },
  computed: {
    ...mapGetters(["username"]),
  },
  methods: {

    toggleSidebar() {
      this.$sidebar.displaySidebar(!this.$sidebar.showSidebar);
    },
    hideSidebar() {
      this.$sidebar.displaySidebar(false);
    },
    toggleMenu() {
      this.showMenu = !this.showMenu;
    },
    signout() {
      // sign out the user when the sign out button is triggered, close the websocket
      // connection and redirect to the login page
      this.$store.dispatch("signout").then((r) => {
        console.log(r);
        this.$store.dispatch("closeSocket");
        this.$router.push("/login");
        window.location.reload();
        this.$store.dispatch("enableNotifications", false);
      });
    },
  },
};
</script>
