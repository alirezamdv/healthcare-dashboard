<template>
    <div>
        <base-header type="" class="pb-8 pt-5 pt-md-8" style="background-color:#dbe5f3">
            <critical-table></critical-table>
        </base-header>

        <div class="container-fluid mt-3">
            <div class="row">
                <div class="col">
                    <patients-table title="Hospitalized Patients" :showPatients="'with admission'"></patients-table>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
  import PatientsTable from "./Dashboard/PatientsTable";
  import CriticalTable from "./Dashboard/CriticalTable";

  export default {
    name: 'tables',
    components: {
      PatientsTable,
      CriticalTable,
    },
  };
</script>
<style></style>
