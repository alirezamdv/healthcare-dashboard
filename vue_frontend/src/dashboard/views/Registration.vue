<template>
    <div>
        <base-header type="" class="pb-6 pb-8 pt-5 pt-md-8" style="background-color:#dbe5f3">
    </base-header>

        <div class="container-fluid mt--7">
            <div class="row mt-5">
                <div class="col-xl-12 mb-5 mb-xl-0">
                    <patients-table 
                        title="All Registered Patients"
                        :showPatients="'currently in the hospital'"
                        :showDeletePatientButton="true"
                        :showWardFilter="false"></patients-table>
                </div>
            </div>

            <div class="row mt-5">
                <div class="col-xl-12 mb-5 mb-xl-0">
                    <patients-table title="Admitted Patients" :showPatients="'with admission'"></patients-table>
                </div>
            </div>

            <div class="row mt-5">
                <div class="col-xl-12 mb-5 mb-xl-0">
                    <patients-table title="Dismissed Patients" :showPatients="'that are dismissed'"></patients-table>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
  import PatientsTable from "./Dashboard/PatientsTable";
  export default {
    components: {
      PatientsTable
    },
    created() {
        this.$store.dispatch("setup");        
    }
  };
</script>
<style></style>
