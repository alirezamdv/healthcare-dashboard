<template>
  <div>
    <modal :show.sync="editModal">
      <template slot="header">
        <h2 class="modal-title" v-if="firstEntry">First Report</h2>
        <h2 v-else class="modal-title" id="editReport">
          First Report<br/>
          <small class="text-muted" v-if="currentRecord">
            last updated: {{ formatDate(this.currentRecord.updated_at) }}
            {{ formatTime(this.currentRecord.updated_at) }}
          </small>
        </h2>
        <br/>
      </template>
      <div class="row align-items-center">
        <div class="card col-md-12 mt-3">
          <div class="card-body">
            <div class="row align-items-center">
              <label class="form-control-label col-md-4 mt--2 pb-3" for="daytime">
                <base-select-daytime label="Daytime" class="mt-4" v-model="daytime" :daytimes="daytimes" required />
             </label>




              <label class="form-control-label mt--2 col-md-4">
                <base-input disabled label="Time" :value="new Date(this.date).toLocaleString()" class="mt-2"></base-input>
              </label>
              <base-button @click="openPicker('datetime-picker')" icon="fa fa-calendar"
                           class="btn btn-md col-md-2 mt--2 picker-button"
                           type="primary"></base-button>
                  <base-input
                      type="number"
                      label="Day of fever"
                      v-model.number="day_of_fever"
                      class="col-md-4"
                      min="0" oninput="validity.valid||(value='');"
                  ></base-input>

              <base-input
                  label="Temperature"
                  v-model="fever"
                  class="col-md-4"
              ></base-input>
              <base-input
                  type="number"
                  label="Pulse"
                  v-model.number="pulse"
                  class="col-md-4"
                  min="0" oninput="validity.valid||(value='');"
              ></base-input>

              <base-input
                  type="number"
                  label="Respiration"
                  v-model.number="respiration"
                  class="col-md-4"
                  min="0" oninput="validity.valid||(value='');"
              ></base-input>

              <base-input
                  label="Diet"
                  v-model="diet"
                  class="col-md-4"
              ></base-input>
            </div>
          </div>
        </div>
        <div class="card col-md-12 mt-5">
          <div class="card-header border-0">
            <div class="row align-items-center">
              <div class="col">
                <h3 class="mb-0">Blood Pressure</h3>
              </div>
            </div>
          </div>

          <div class="card-body">
            <div class="row align-items-center">
              <base-input
                  type="number"
                  label="Systolic"
                  v-model.number="bp_sys"
                  class="col-md-4"
                  min="0" oninput="validity.valid||(value='');"
              ></base-input>

              <base-input
                  type="number"
                  label="Diastolic"
                  v-model.number="bp_dia"
                  class="col-md-4"
                  min="0" oninput="validity.valid||(value='');"
              ></base-input>
            </div>
          </div>
        </div>
        <div class="card col-md-12 mt-5">
          <div class="card-header border-0">
            <div class="row align-items-center">
              <div class="col">
                <h3 class="mb-0">Fluid Intake</h3>
              </div>
            </div>
          </div>
          <div class="card-body">
            <div class="row align-items-center">
              <base-input
                  type="number"
                  label="Oral Fluids"
                  v-model.number="fi_oral"
                  class="col-md-4"
                  min="0" oninput="validity.valid||(value='');"
                  placeholder="in ml"
              ></base-input>

              <base-input
                  type="number"
                  label="Parenteral"
                  v-model.number="fi_parenteral"
                  class="col-md-4"
                  min="0" oninput="validity.valid||(value='');"
                  placeholder="in ml"
              ></base-input>

              <base-input
                  type="number"
                  label="Other"
                  v-model.number="fi_other"
                  class="col-md-4"
                  min="0" oninput="validity.valid||(value='');"
                  placeholder="in ml"
              ></base-input>

              <base-input
                  type="number"
                  label="In 8 hours"
                  v-model.number="fi_eight_hrs"
                  class="col-md-4"
                  min="0" oninput="validity.valid||(value='');"
                  placeholder="in ml"
              ></base-input>

              <base-input
                  type="number"
                  label="Total"
                  v-model.number="fi_total"
                  class="col-md-4"
                  disabled
              ></base-input>
            </div>
          </div>
        </div>
        <div class="card col-md-12 mt-5">
          <div class="card-header border-0">
            <div class="row align-items-center">
              <div class="col">
                <h3 class="mb-0">Fluid Output</h3>
              </div>
            </div>
          </div>
          <div class="card-body">
            <div class="row align-items-center">
              <base-input
                  type="number"
                  label="Urine"
                  v-model.number="fo_urine"
                  class="col-md-4"
                  min="0" oninput="validity.valid||(value='');"
                  placeholder="in ml"
              ></base-input>

              <base-input
                  type="number"
                  label="UF"
                  v-model.number="fo_uf"
                  class="col-md-4"
                  min="0" oninput="validity.valid||(value='');"
                  placeholder="in ml"
              ></base-input>

              <base-input
                  type="number"
                  label="Emesis"
                  v-model.number="fo_emesis"
                  class="col-md-4"
                  min="0" oninput="validity.valid||(value='');"
                  placeholder="in ml"
              ></base-input>

              <base-input
                  type="number"
                  label="Drainage"
                  v-model.number="fo_drainage"
                  class="col-md-4"
                  min="0" oninput="validity.valid||(value='');"
                  placeholder="in ml"
              ></base-input>

              <base-input
                  type="number"
                  label="In 8 hours"
                  v-model.number="fo_eight_hrs"
                  class="col-md-4"
              ></base-input>

              <base-input
                  type="number"
                  label="Total"
                  v-model.number="fo_total"
                  class="col-md-4"
                  disabled
              ></base-input>
            </div>
          </div>
        </div>
        <div class="card col-md-12 mt-5">
          <div class="card-body">
            <div class="row align-items-center">
              <base-input
                  type="number"
                  label="Pain Score"
                  v-model.number="pain_score"
                  class="col-md-4"
                  min="0" oninput="validity.valid||(value='');"
                  max="10"
              ></base-input>

              <base-input
                  type="number"
                  label="Abd. Cir."
                  v-model.number="abd_cir"
                  class="col-md-4"
                  min="0" oninput="validity.valid||(value='');"
                  placeholder="in cm"
              ></base-input>

              <base-input
                  type="number"
                  label="Stools"
                  v-model.number="stools"
                  class="col-md-4"
                  min="0" oninput="validity.valid||(value='');"
              ></base-input>

              <base-input
                  type="number"
                  label="Urine"
                  v-model.number="urine"
                  class="col-md-4"
                  min="0" oninput="validity.valid||(value='');"
              ></base-input>

              <base-input
                  label="Weight"
                  v-model.number="weight"
                  class="col-md-4"
                  placeholder="in kg"
              ></base-input>
              <base-input
                  type="number"
                  label="Height"
                  v-model.number="height"
                  class="col-md-4"
                  min="0" oninput="validity.valid||(value='');"
                  placeholder="in cm"
              ></base-input>

              <base-input
                  type="number"
                  label="O2 Sat"
                  v-model.number="o2sat"
                  class="col-md-4"
                  min="0" oninput="validity.valid||(value='');"
                  placeholder="in %"
              ></base-input>

              <base-input
                  type="number"
                  label="Hematocrit"
                  v-model.number="hematocrit"
                  class="col-md-4"
                  min="0" oninput="validity.valid||(value='');"
                  placeholder="in %"
              ></base-input>

              <base-input
                  type="number"
                  label="Platelet Count"
                  v-model.number="platelet"
                  class="col-md-4"
                  min="0" oninput="validity.valid||(value='');"
              ></base-input>
                            <base-input
                  type="number"
                  label="WBC Count"
                  v-model.number="wbc"
                  class="col-md-4"
                  min="0" oninput="validity.valid||(value='');"
              ></base-input>

              <label class="col-md-4 mt--2 pb-1">
                <h5 class="mb-2">Status</h5>
                <select v-model="status" class="form-control">
                  <option
                      :value="stat.option"
                      v-for="stat in statusOptions"
                      :key="stat.option"
                      :selected="stat"
                  >{{ stat.option }}
                  </option
                  >
                </select>
              </label>
              <label class=" col-md-4">
                <h5 class="mb-2">Monitoring Interval</h5>

                <select
                    v-model="monitoring_interval"
                    label="Monitoring Interval"
                    class="form-control"
                >
                  <option
                      v-bind:value="mon_interval.interval"
                      v-for="mon_interval in intervals"
                      v-bind:key="mon_interval.interval"
                  >{{ mon_interval.interval }}
                  </option
                  >
                </select>
              </label>

                            <label class="col-md-12 mt-5">
                <h5 class="mb-2">Warning Signs</h5>
                <textarea class="form-control col-md-12" rows="5" placeholder="..." v-model="warning_signs"></textarea>
              </label>

              <label class="col-md-12 mt-5">
                <h5 class="mb-2">Additional Info</h5>
                <textarea class="form-control col-md-12" rows="5" placeholder="..." v-model="additional"></textarea>
              </label>

              <label class="col-md-12 mt-5">
                <h5 class="mb-2">Medical Advice</h5>
                <textarea class="form-control col-md-12" rows="5" placeholder="..."
                          v-model="medical_advice"></textarea>
              </label>


            </div>
          </div>
        </div>
      </div>

      <template slot="footer">
        <div class="mr-auto">Fields marked with an <strong>*</strong> are required</div>
        <base-button type="secondary" @click="editModal = false"
        >Close
        </base-button
        >
        <base-button type="primary" @click="addReport()"
        >Save changes
        </base-button>
      </template>
    </modal>

    <datetime ref="datetime-picker" type="datetime" v-model="date" :backdrop-click=true
              :auto=true></datetime>
  </div>

</template>
<script>
import {Datetime} from 'vue-datetime';

export default {
  name: "new-patient",
  props: ["id", "show", "patient"],
  components: {
    datetime: Datetime
  },
  data() {
    return {
      newPatient: true,
      editModal: false,
      firstEntry: null,
      currentRecord: null,
      edit: false,
      date: null,
      time: new Date().toLocaleTimeString(),
      daytime: null,
      day_of_fever: null,
      fever: null,
      history_id: null,
      updated_at: null,
      pulse: null,
      respiration: null,
      bp_sys: null,
      bp_dia: null,
      diet: null,
      fi_oral: null,
      fi_parenteral: null,
      fi_other: null,
      fi_eight_hrs: null,
      fi_total: null,
      fo_urine: null,
      fo_uf: null,
      fo_emesis: null,
      fo_drainage: null,
      fo_eight_hrs: null,
      fo_total: null,
      pain_score: null,
      abd_cir: null,
      stools: null,
      urine: null,
      weight_ht: null,
      weight: null,
      height: null,
      additional: null,
      medical_advice: null,
      warning_signs: null,
      o2sat: null,
      hematocrit: null,
      platelet: null,
      wbc: null,
      monitoring_interval: null,
      status: null,
      intervals: [
        {interval: 1},
        {interval: 2},
        {interval: 4},
        {interval: 6},
      ],
      daytimes: [
        {time: "D"},
        {time: "E"},
        {time: "N"},
      ],
      statusOptions: [{option: "febrile"}, {option: "critical"}, {option: "recovery"}],
      notes: [],
      tableData: null,
      columns: [],
    };
  },
  created() {
    this.editModal = this.show;
  },
  computed: {

    reportData() {
      try {
        return this.$store.getters.getReportById(Number(this.id));
      } catch (e) {
        console.log(e);

      }
      return null;
    },
  },
  watch: {
    reportData() {
      var history = this.$store.getters.getReportById(Number(this.id)).history.reverse();
      var sortHistory = [].slice.call(history).sort(function (a, b) {
        return (new Date(a.datetime) - new Date(b.datetime));
      });
      this.tableData = sortHistory;
      this.calcTimedelta(history);

    },
  },
  methods: {

    calcFoTotal(report) {
      return report.fo_drainage + report.fo_emesis + report.fo_uf + report.fo_urine;
    },

    calcFiTotal(report) {
      return report.fi_oral + report.fi_other + report.fi_parenteral;
    },

    openPicker(pickerName) {
      var input = this.$refs[pickerName].$el.firstChild.nextElementSibling;

      if (!input) {
        return;
      }

      input.click();
    },

    deleteReport(reportId) {
      if (confirm("Do you really want to delete this Report?")) {
        this.newPatient = false;
        this.$store.dispatch("deleteReport", {id: reportId});
      } else {
        return;
      }
    },

    addReport() {
      if (this.firstEntry) {
        this.deleteReport(this.reportData.history[0].history_id)
      }
      this.newPatient = false;
      this.firstEntry = false;

      var jsonObj = {
        patient: this.id,
        daytime: this.daytime,
        respiration: this.respiration,
        day_of_fever: this.day_of_fever,
        fever: this.fever,
        pulse: this.pulse,
        bp_sys: this.bp_sys,
        bp_dia: this.bp_dia,
        diet: this.diet,
        fi_oral: this.fi_oral,
        fi_parenteral: this.fi_parenteral,
        fi_other: this.fi_other,
        fi_eight_hrs: this.fi_eight_hrs,
        fiTotal: this.fi_oral + this.fi_parenteral + this.fi_other,
        fo_urine: this.fo_urine,
        fo_uf: this.fo_uf,
        fo_emesis: this.fo_emesis,
        fo_drainage: this.fo_drainage,
        fo_eight_hrs: this.fo_eight_hrs,
        foTotal: this.fo_urine + this.fo_uf + this.fo_emesis + this.fo_drainage,
        pain_score: this.pain_score,
        abd_cir: this.abd_cir,
        stools: this.stools,
        urine: this.urine,
        weight_ht: this.weight_ht,
        weight: this.weight,
        height: this.height,
        additional: this.additional,
        medical_advice: this.medical_advice,
        warning_signs: this.warning_signs,
        o2sat: this.o2sat,
        hematocrit: this.hematocrit,
        platelet: this.platelet,
        wbc: this.wbc,
        status: this.status,
        monitoring_interval: this.monitoring_interval,
      };
      this.$store.dispatch("createReport", {report: jsonObj});
      this.editModal = false;
    },

    formatTime(date) {
      var options = {
        hour: "numeric",
        minute: "numeric",
        hour12: false,
      };

      return new Intl.DateTimeFormat("en-GB", options).format(new Date(date));
    },

    formatDate(date) {
      return (new Date(date).toLocaleDateString('en-GB'));
    },
  },
};
</script>
<style>
@media (min-width: 576px) {
  .modal-dialog {
    width: 800px !important;
    max-width: 800px !important;
  }
}

.modal {
  overflow: auto !important;
}

</style>
