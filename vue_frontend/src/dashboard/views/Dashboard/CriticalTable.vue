<!--
  Content: Composed component for the critical cards in the dashboard and the table displaying the critical patients
-->

<template>
  <div v-if="criticalReports">
    <!-- Warning Cards -->
    <div class="row">
      <div
          class="col-xl-3 col-lg-6"
          v-for="report in tableData"
          :key="report.patient"
      >
        <router-link :to="'/patients/' + report.patient">
          <stats-card
              type="white"
              :title="report.status"
              :sub-title="patientName(report.patient)"
              icon="fa fa-exclamation-triangle  text-default"
              class="mb-4 mb-xl-0 bg-danger text-white mt-xl-5"
          >
            <template slot="footer">
            <span class="text-white mr-2" title="Fever and Pulse"
            ><i class="fa fa-thermometer-three-quarters mr-1" title="Fever"></i>
              {{ report.fever }} °C
              <i class="fa fa-heart ml-3 mr-1" title="Pulse"></i>
              {{ report.pulse }}</span
            >
            </template>
          </stats-card>
        </router-link>
      </div>
    </div>

    <div class="card mt-5">
      <div class="card-header border-0">
        <div class="row align-items-center">
          <div class="col">
          <h3 class="mb-0">Critical Patients <i class="far fa-question-circle text-muted"
                                                  v-b-popover.hover.top="'Table shows all patients marked with the status attribute critical.'"></i>
            </h3>
          <div v-if="showWardFilter" class="row ml-3 mt-3">
            <base-checkbox @input="checkShowWard" :checked="showWard"></base-checkbox>
            Display only from ward
            <select class="ml-2" v-if="showWard" @input="selectWard" :value="ward">
              <option v-for="(item, index) in wards" :key="index">{{ item }}</option>
            </select>
          </div>
        </div>
      </div>
    </div>

      <div class="table-responsive">
        <base-table thead-classes="thead-light" :data="filteredSortedPatientData">
          <template slot="columns">
            <th>ID</th>
            <th>Patient</th>
            <th>Fever</th>
            <th>Pulse</th>
            <th>Monitoring Interval</th>
            <th>Status</th>
            <th>Report <i class="far fa-question-circle" v-b-popover.hover.top="'See/Edit Patient Report'"></i></th>
          </template>

          <template slot-scope="{ row }">
            <th scope="row">
              <router-link :to="'/patients/' + row.patient">{{
                  row.patient
                }}
              </router-link>
            </th>
            <td>
              {{ patientName(row.patient) }}
            </td>
            <td class="text-danger">
              {{ row.fever }} °C
            </td>
            <td class="text-danger">
              {{ row.pulse }}
            </td>
            <td class="text-danger">
              {{ row.monitoring_interval }}
            </td>
            <td>
              <i
                  class="fas fa-circle text-success mr-3"
                  :class="row.status === 'ok' ? 'text-success' : 'text-danger'"
              >
              </i>
            </td>
            <td>
              <router-link :to="'/patients/' + row.patient">
                <base-button class="btn btn-sm" icon="fas fa-chart-bar" type="primary"
                             @click="'/patients/'+ row.patient"> Patient Report
                </base-button>
              </router-link>

            </td>
          </template>
        </base-table>
      </div>
    </div>
  </div>
</template>
<script>
import {mapGetters} from "vuex";

export default {
  name: "critical-table",
  props: {
    showWardFilter: {
      type: Boolean,
      default: false,
    },
  },
  created(){


    this.tableData = this.criticalReports;
  },
  data() {
    return {
      modal0: false,
      tableData: [],
    };
  },

  methods: {
    notify(title, message) {
      this.$notify({
        title: title,
        message: message,
        type: "warning",
        closeOnClick: false,
        timeout: 50000,
        icon: "fa fa-exclamation-triangle",
      });
    },
    patient(id) {
      return this.$store.getters.getPatientById(id);
    },
    patientName(id){
      return this.$store.getters.patientNameById(id);
    },
  },
  beforeDestroy() {
    clearInterval(this.criticalReports);
  },
  computed: {
    ...mapGetters(["criticalReports", "showWard", "ward", "wards"]),
    filteredSortedPatientData() {
      return [...this.tableData]
        // TODO replace filter with actual filter function
        .filter(report => this.isFilteringByWard && this.showWard
          ? report.patient % this.selected == 0
          : true);
    }
  },
  watch:{
    criticalReports(){
      this.tableData=this.criticalReports;
    }
  }
};
</script>
<style></style>
