<!--
Author: Jennifer Horstmann
-->
<template>
  <div>

    <base-header type="" class="pb-6 pb-8 pt-5 pt-md-8" style="background-color:#dbe5f3"
    >
      <div class="container-fluid d-flex align-items-center">
        <div class="row">
          <div class="col-md-10">
            <h1 class="display">Manage Notifications</h1>
            <p>Current Status: Notifications
              <span v-if="show_notifications" class="text-success">ON</span>
              <span v-else class="text-danger">OFF</span></p>
          </div>
          <base-button @click="enableNotifications(true)" class="mt-5 mb-5 ml-3" type="primary"
                       v-b-popover.hover.top="'Enables Notifications about the monitoring interval and a patient possibly entering a critical state after 3 days of fever'"
          >Enable Notifications
          </base-button>
          <base-button @click="enableNotifications(false)" class="mt-5 mb-5 ml-5" type="secondary"
                       v-b-popover.hover.top="'Disables Notifications about the monitoring interval and a patient possibly entering a critical state after 3 days of fever. All other notifications will remain enabled.'"
          >Disable Notifications
          </base-button>
        </div>
      </div>
    </base-header>
  </div>
</template>

<script>
import {mapGetters} from "vuex";

export default {
  name: "settings",
  data() {
    return {
      notificationEnabled: null,
    }
  },

  computed: {
    ...mapGetters(["username"]),
    ...mapGetters(["show_notifications"]),
  },
  methods: {
    enableNotifications(bool) {
      this.notificationEnabled = bool;
      this.$store.dispatch("enableNotifications", bool);
    },
  },

}
</script>

<style scoped>

</style>
