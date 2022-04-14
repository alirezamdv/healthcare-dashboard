<template>
  <div class="card">
    <div class="card-header border-0">
      <tabs>
        <tab title="Dengue Diagnosis">
          <dengue-form :patient_id="id"></dengue-form>
        </tab>
        <tab title="Patient Chart">
          <report-data-form :id="id" :data="data"></report-data-form>
        </tab>
      </tabs>
    </div>
  </div>
</template>
<script>
import Tabs from '../../components/Tabs/Tabs.vue';
import Tab from '../../components/Tabs/Tab.vue';
import ReportDataForm from './forms/ReportDataForm.vue'
import DengueForm from './forms/DengueForm.vue';

export default {
  name: "report",
  props: ["data", "id"],
  components: {
    Tabs,
    Tab,
    ReportDataForm,
    DengueForm,
  },
};
</script>
<style>
</style>
