<template>
  <div class="wrapper" :class="{ 'nav-open': $sidebar.showSidebar }">
    <side-bar
        :background-color="sidebarBackground"
        short-title="Dengue Dashboard"
        title="Dengue Dashboard"
    >
      <template slot="links">
        <sidebar-item
            :link="{
            name: 'Registration',
            icon: 'ni ni-bullet-list-67 text-primary',
            path: '/registration',
          }"
        />
        <sidebar-item
            :link="{
            name: 'Diagnosis',
            icon: 'ni ni-tv-2 text-primary',
            path: '/diagnosis',
          }"
        />
        <sidebar-item
            :link="{
            name: 'Monitoring',
            icon: 'ni ni-tv-2 text-primary',
            path: '/monitoring',
          }"
        />
        <sidebar-item
            :link="{
            name: 'Administration',
            icon: 'ni ni-settings text-primary',
            path: `/${admin}`,
            target: '_blank'
          }"
        />
        <sidebar-item
            :link="{
            name: 'Settings',
            icon: 'ni ni-bell-55 text-primary',
            path: '/settings',
          }"

        />
      </template>
    </side-bar>
    <div class="main-content" :data="sidebarBackground">
      <dashboard-navbar></dashboard-navbar>

      <div @click="toggleSidebar">
        <fade-transition :duration="200" origin="center top" mode="out-in">
          <router-view></router-view>
        </fade-transition>
        <content-footer v-if="!$route.meta.hideFooter"></content-footer>
      </div>
    </div>
  </div>
</template>
<script>
import DashboardNavbar from "./DashboardNavbar.vue";
import ContentFooter from "./ContentFooter.vue";
import {FadeTransition} from "vue2-transitions";

export default {
  components: {
    DashboardNavbar,
    ContentFooter,
    FadeTransition,
  },
  data() {
    return {
      sidebarBackground: "vue", //vue|blue|orange|green|red|primary
      admin: process.env.NODE_ENV === 'production' ? process.env.VUE_APP_ADMIN : 'admin',
    };
  },
  methods: {
    toggleSidebar() {
      if (this.$sidebar.showSidebar) {
        this.$sidebar.displaySidebar(false);
      }
    },
  },
};
</script>
<style lang="scss"></style>
