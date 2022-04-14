<template>
  <modal @close="close()" :show.sync="editModal">
  <template slot="header">
          <h2 class="modal-title" v-if="firstEntry">First Report</h2>
          <h2 v-else-if="patientNumber" class="modal-title">Add Report</h2>
          <h2 v-else class="modal-title">Edit Report
            <br/>
            <small class="text-muted">
              last updated: {{ formatDate(this.updated_at) }}
              {{ formatTime(this.updated_at) }}
            </small>
            </h2>
            <br/>
    </template>
    <div class="row align-items-center">

      <div class="card col-md-12 mt-3">
        <div class="card-body">
          <div class="row align-items-center">
            <label class=" col-md-4 mt--2 pb-3">
              <h5 class="mb-2">Daytime</h5>

              <select
                  v-model="daytime"
                  class="form-control"
              >
                <option
                    v-for="daytime in daytimes"
                    :key="daytime.option"
                    :value="daytime.option"
                >{{ daytime.option }}
                </option>
              </select>
            </label>

            <label class="form-control-label mt--2 col-md-4">
              Time of report
              <base-input disabled :value="new Date(this.datetime).toLocaleString()" class="mt-2"
                          placeholder="Select Datetime"></base-input>
            </label>
            <base-button @click="openDateTimePicker('date-modal')" icon="fa fa-calendar"
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
                placeholder="°C"
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

      <!--  -->

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
                placeholder="ml"
            ></base-input>

            <base-input
                type="number"
                label="Parenteral"
                v-model.number="fi_parenteral"
                class="col-md-4"
                min="0" oninput="validity.valid||(value='');"
                placeholder="ml"
            ></base-input>

            <base-input
                type="number"
                label="Other"
                v-model.number="fi_other"
                class="col-md-4"
                min="0" oninput="validity.valid||(value='');"
                placeholder="ml"
            ></base-input>

            <base-input
                type="number"
                label="In 8 hours"
                v-model.number="fi_eight_hrs"
                class="col-md-4"
                min="0" oninput="validity.valid||(value='');"
                placeholder="ml"
            ></base-input>

            <base-input
                type="number"
                label="Total"
                v-model.number="fi_total"
                class="col-md-4"
                min="0" oninput="validity.valid||(value='');"
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
                placeholder="ml"
            ></base-input>

            <base-input
                type="number"
                label="UF"
                v-model.number="fo_uf"
                class="col-md-4"
                min="0" oninput="validity.valid||(value='');"
                placeholder="ml"
            ></base-input>

            <base-input
                type="number"
                label="Emesis"
                v-model.number="fo_emesis"
                class="col-md-4"
                min="0" oninput="validity.valid||(value='');"
                placeholder="ml"
            ></base-input>

            <base-input
                type="number"
                label="Drainage"
                v-model.number="fo_drainage"
                class="col-md-4"
                min="0" oninput="validity.valid||(value='');"
                placeholder="ml"
            ></base-input>

            <base-input
                type="number"
                label="In 8 hours"
                v-model.number="fo_eight_hrs"
                class="col-md-4"
                min="0" oninput="validity.valid||(value='');"
                placeholder="ml"
            ></base-input>

            <base-input
                type="number"
                label="Total"
                v-model.number="fo_total"
                class="col-md-4"
                min="0" oninput="validity.valid||(value='');"
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
            ></base-input>

            <base-input
                type="number"
                label="Abd. Cir."
                v-model.number="abd_cir"
                class="col-md-4"
                min="0" oninput="validity.valid||(value='');"
                placeholder="cm"
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
                type="number"
                label="Weight"
                v-model.number="weight"
                class="col-md-4"
                placeholder="kg"
            ></base-input>

            <base-input
                type="number"
                label="Height"
                v-model.number="height"
                class="col-md-4"
                min="0" oninput="validity.valid||(value='');"
                placeholder="cm"
            ></base-input>

            <base-input
                type="number"
                label="O2 Sat"
                v-model.number="o2sat"
                class="col-md-4"
                min="0" oninput="validity.valid||(value='');"
                placeholder="%"
            ></base-input>

            <base-input
                type="number"
                label="Hematocrit"
                v-model.number="hematocrit"
                class="col-md-4"
                min="0" oninput="validity.valid||(value='');"
                placeholder="%"
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
                    v-for="stat in statusOptions"
                    :key="stat.option"
                    :value="stat.option"
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
                    v-for="mon_interval in intervals"
                    :key="mon_interval.option"
                    :value="mon_interval.option"
                >{{ mon_interval.option }}
                </option
                >
              </select>
            </label>

            <label class="col-md-12 mt-5">
              <h5 class="mb-2">Warning Signs</h5>
              <textarea class="form-control col-md-12" rows="5" placeholder="..."
                        v-model="warning_signs"></textarea>
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
      <base-button type="secondary" @click="close()">
        Close
      </base-button>

      <base-button type="primary" @click="firstEntry 
        ? createReport()
        : patientNumber
          ? addReport()
          : editReport(history_id)"
      >{{firstEntry ? 'Create Report' : 'Save changes'}}
      </base-button>

      <datetime ref="date-table" type="datetime" v-model="datetime" :backdrop-click=true
                :auto=true></datetime>

      <datetime ref="date-modal" type="datetime" v-model="datetime" :backdrop-click=true
                :auto=true></datetime>
    </template>
  </modal>
 
</template>
<script>
import {Datetime} from 'vue-datetime';
import BaseInput from './BaseInput.vue';

export default {
  name: "report-modal",
  components: { 
    BaseInput,
    Datetime,
  },
  props: ['input', 'firstEntry', 'patientNumber', 'daytimes', 'statusOptions', 'intervals'],
  data() {
    return {
      ...this.input, 
      editModal: true,
    }
  },
  methods: {
    openDateTimePicker(pickerName) {
      const input = this.$refs[pickerName].$el.firstChild.nextElementSibling;

      if (input) {
        input.click();
      }
    },
    toJson() {
      const currentValues = {};
      for (const [key, value] of Object.entries(this)) {
        if(this.input[key] !== undefined){
          currentValues[key] = value;
        }
      }
      return {
        ...this.input,
        ...currentValues,
      };
    },
    createReport() {
      const report = this.toJson();
      this.$store.dispatch("createReport", {report});
      this.close();
    },
    addReport() {
      const report = this.toJson();
      this.$store.dispatch("addReport", {id: this.patientNumber, report})
      this.close();
    },
    editReport() {
      const json = this.toJson();
      this.$store.dispatch("editReport", {id: json.history_id, report: json});
      this.close();
    },
    close() {
      this.$emit('close')
    },
    formatDate(date) {
      var options = {
        year: "numeric",
        month: "2-digit",
        day: "2-digit",
      }
      return new Intl.DateTimeFormat("en-US", options).format(new Date(date));
    },
    formatTime(date) {
      var time = new Date(date);
      var offset = time.getTimezoneOffset();

      offset = Math.abs(offset / 60);
      time.setHours(time.getHours() - offset);

      return (time.toLocaleTimeString());
    },
  },
};
</script>
<style>
</style>
