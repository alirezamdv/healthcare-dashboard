<template>
  <div>
    <base-header type="" class="pb-6 pb-8 pt-5 pt-md-8" style="background-color:#dbe5f3">
    </base-header>
    <div class="container-fluid mt--7">
      <div class="row mt-5">
        <div class="col-xl-12 mb-5 mb-xl-0">
          <patients-table title="Diagnosis Needed" :showPatients="'who need a diagnosis'" :showWardFilter="false"></patients-table>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import PatientsTable from "./Dashboard/PatientsTable";

// BUG: If a patient has two history entries, both on the same date. the dashboard can't decide if it should display a critical patient card or not.
// At first it will be displayed and after a while it disappears.
export default {
  components: {
    PatientsTable,
  },
  data() {
    return {
      notificationModal: false,
    };
  },
  methods: {
    enableNotifications(bool) {
      this.$store.dispatch("enableNotifications", bool);
    },
  },
};
</script>
<style></style>
