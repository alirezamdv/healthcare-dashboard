<!--
Author: Jennifer Horstmann
Content: Report Overview Table
-->

<template>
  <div class="card" v-if="reportData">
    <div class="card-header border-0">
      <div class="row align-items-center">
        <div class="col">
          <h3 class="mb-0">Current report of {{ reportData.patient_name }}</h3>
        </div>
      </div>
    </div>

    <div class="table-responsive">
      <base-table thead-classes="thead-light" :data="reportData.history">
        <template slot="columns">
          <th>ID</th>
          <th>Date and Time</th>
          <th>Fever</th>
          <th>Pulse</th>
          <th>Fluid Input</th>
          <th>Fluid Output</th>
          <th>Status</th>
        </template>

        <template slot-scope="{ row }">
          <th scope="row">
            {{ row.history_id }}
          </th>
          <td>
            {{ formatDate(row.datetime) }}
          </td>
          <td>
            {{ row.fever }}
          </td>
          <td>
            {{ row.pulse }}
          </td>
          <td>
            {{ row.fi_total }}
          </td>
          <td>{{ row.fo_total }}</td>
          <td>
            <i
              class="fas fa-circle text-success mr-3"
              :class="row.status === 'febrile' ? 'text-success' : 'text-danger'"
            >
            </i>
            {{row.status}}
          </td>
        </template>
      </base-table>
    </div>
  </div>
</template>
<script>

export default {
  name: "reports-table",
  props: ["id"],
  data() {
    return {
      tableData: [],
    };
  },
  methods: {
    formatDate(date) {
      var options = {
        year: "numeric",
        month: "numeric",
        day: "numeric",
        hour: "numeric",
        minute: "numeric",
        hour12: false,
      };
      return new Intl.DateTimeFormat("en-GB", options).format(new Date(date));
    },
  },
  beforeDestroy() {
    clearInterval(this.reportData);
  },
  computed: {

    reportData() {
      return this.$store.getters.getReportById(Number(this.id));
    },
  },
};
</script>
<style></style>
