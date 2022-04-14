<template>
    <div class="table-responsive">
        <table class="table table-hover" thead-classes="thead-light">
          <tbody>
            <tr>
              <th>{{hasReportData ? 'Edit/Delete' : 'Create a report'}}</th>
              <td v-for="(item, i) in sortedHistory"
                :key="i">
                <base-button
                    @click="showEditModal(item.history_id)"
                    class="btn btn-sm"
                    icon="fas fa-edit"
                    type="primary">
                </base-button>
                <base-button
                    class="btn btn-sm"
                    icon="fas fa-trash-alt"
                    type="danger"
                    v-on:click="deleteReport(item.history_id)">
                </base-button>
              </td>
              <td>
                <div class="col text-center minInputColumnWidth10Rem" v-if="this.$route.name !== 'tables'">
                <button class="btn btn-sm btn-primary "
                        v-on:click="hasReportData ? addReport() : createReport()">
                        {{hasReportData ? 'Add Report' : 'Create Report'}}
                </button>
                </div>
              </td>
            </tr>
          <template v-if="hasReportData">
            <tr>
              <th>Day</th>
              <th v-for="(item, i) in sortedHistory"
                  :key="i" class="text-center">Day
                  {{ Math.round(Math.abs((new Date(item.datetime) - new Date(item.created_at)) / (1000 * 3600 * 24) + 1)) }}
              </th>
            </tr>
            <report-row-component :name="daytime.name" :suffix="daytime.placeholder" :history="getHistoryFor(daytime.backend_id)">
            </report-row-component>

            <report-row-component :name="time.name" :history="getHistoryFor(time.backend_id)"  :transformHistoryItem="(item) => item ? new Date(item).toLocaleDateString() : ''">
            </report-row-component>

            <report-row-component :name="day_of_fever.name" :suffix="day_of_fever.placeholder" :history="getHistoryFor(day_of_fever.backend_id)">
            </report-row-component>
            <report-row-component :name="fever.name" :suffix="fever.placeholder" :history="getHistoryFor(fever.backend_id)">
            </report-row-component>
            <report-row-component :name="pulse.name" :suffix="pulse.placeholder" :history="getHistoryFor(pulse.backend_id)">
            </report-row-component>
            <report-row-component :name="respiration.name" :suffix="respiration.placeholder" :history="getHistoryFor(respiration.backend_id)">
            </report-row-component>
            <report-row-component :name="bp_sys.name" :suffix="bp_sys.placeholder" :history="getHistoryFor(bp_sys.backend_id)">
            </report-row-component>
            <report-row-component :name="bp_dia.name" :suffix="bp_dia.placeholder" :history="getHistoryFor(bp_dia.backend_id)">
            </report-row-component>
            <report-row-component :name="diet.name" :suffix="diet.placeholder" :history="getHistoryFor(diet.backend_id)">
            </report-row-component>

            <tr>
                <th>FLUID<br>INTAKE</th>
            </tr>
            <report-row-component :name="fi_oral.name" :suffix="fi_oral.placeholder" :history="getHistoryFor(fi_oral.backend_id)">
            </report-row-component>
            <report-row-component :name="fi_parenteral.name" :suffix="fi_parenteral.placeholder" :history="getHistoryFor(fi_parenteral.backend_id)">
            </report-row-component>
            <report-row-component :name="fi_other.name" :suffix="fi_other.placeholder" :history="getHistoryFor(fi_other.backend_id)">
            </report-row-component>
            <report-row-component :name="fi_eight_hrs.name" :suffix="fi_eight_hrs.placeholder" :history="getHistoryFor(fi_eight_hrs.backend_id)">
            </report-row-component>
            <report-row-component :name="fi_total.name" :suffix="fi_total.placeholder" 
                :history="getHistoryTotalFor([
                fi_oral.backend_id, fi_parenteral.backend_id, fi_other.backend_id, fi_eight_hrs.backend_id,
                ])"
            >
            </report-row-component>

            <tr>
                <th>FLUID<br>OUTPUT</th>
            </tr>
            <report-row-component :name="fo_urine.name" :suffix="fo_urine.placeholder" :history="getHistoryFor(fo_urine.backend_id)">
            </report-row-component>
            <report-row-component :name="fo_uf.name" :suffix="fo_uf.placeholder" :history="getHistoryFor(fo_uf.backend_id)">
            </report-row-component>
            <report-row-component :name="fo_emesis.name" :suffix="fo_emesis.placeholder" :history="getHistoryFor(fo_emesis.backend_id)">
            </report-row-component>
            <report-row-component :name="fo_drainage.name" :suffix="fo_drainage.placeholder" :history="getHistoryFor(fo_drainage.backend_id)">
            </report-row-component>
            <report-row-component :name="fo_eight_hrs.name" :suffix="fo_eight_hrs.placeholder" :history="getHistoryFor(fo_eight_hrs.backend_id)">
            </report-row-component>
            <report-row-component :name="fo_total.name" :suffix="fo_total.placeholder" 
              :history="getHistoryTotalFor([
                fo_urine.backend_id, fo_uf.backend_id, fo_emesis.backend_id, fo_drainage.backend_id, fo_eight_hrs,
              ])"
            >
            </report-row-component>

            <report-row-component :name="pain_score.name" :suffix="pain_score.placeholder" :history="getHistoryFor(pain_score.backend_id)">
            </report-row-component>
            <report-row-component :name="abd_cir.name" :suffix="abd_cir.placeholder" :history="getHistoryFor(abd_cir.backend_id)">
            </report-row-component>
            <report-row-component :name="stools.name" :suffix="stools.placeholder" :history="getHistoryFor(stools.backend_id)">
            </report-row-component>
            <report-row-component :name="weight.name" :suffix="weight.placeholder" :history="getHistoryFor(weight.backend_id)">
            </report-row-component>
            <report-row-component :name="height.name" :suffix="height.placeholder" :history="getHistoryFor(height.backend_id)">
            </report-row-component>
            <report-row-component :name="o2sat.name" :suffix="o2sat.placeholder" :history="getHistoryFor(o2sat.backend_id)">
            </report-row-component>
            <report-row-component :name="hematocrit.name" :suffix="hematocrit.placeholder" :history="getHistoryFor(hematocrit.backend_id)">
            </report-row-component>
            <report-row-component :name="platelet.name" :suffix="platelet.placeholder" :history="getHistoryFor(platelet.backend_id)">
            </report-row-component>
            <report-row-component :name="wbc.name" :suffix="wbc.placeholder" :history="getHistoryFor(wbc.backend_id)">
            </report-row-component>

            <report-row-component :name="status.name" :suffix="status.placeholder" :history="getHistoryFor(status.backend_id)">
            </report-row-component>

            <report-row-component :name="monitoring_interval.name" :suffix="monitoring_interval.placeholder" :history="getHistoryFor(monitoring_interval.backend_id)">
            </report-row-component>

            <report-row-component :name="warning_signs.name" :suffix="warning_signs.placeholder" :history="getHistoryFor(warning_signs.backend_id)">
            </report-row-component>
            <report-row-component :name="additional.name" :suffix="additional.placeholder" :history="getHistoryFor(additional.backend_id)">
            </report-row-component>
            <report-row-component :name="medical_advice.name" :suffix="medical_advice.placeholder" :history="getHistoryFor(medical_advice.backend_id)">
            </report-row-component>
            
            <tr>
              <th>Created<br>By</th>
              <td v-for="(item, i) in sortedHistory"
                  :key="i">
                  {{ item.history_user_name }}
              </td>
              <td></td>
            </tr>
          </template>
          </tbody>
        </table>

        <report-modal
          v-if="editModal"
          :show.sync="editModal"
          :input="getReportFromHistory(selectedHistoryId)"
          :firstEntry="!hasReportData"
          :patientNumber="patientNumber"
          :statusOptions="status.statusOptions"
          :daytimes="daytime.statusOptions"
          :intervals="monitoring_interval.statusOptions"
          @close="onCloseModal"
        >
        </report-modal>
    </div>
</template>

<script>
import ReportRowComponent from '../reportComponents/ReportRowComponent';
import {RowComponent, TotalComponent, SelectComponent, JsonRowItem, hasJsonNameAndValue, isRowItem} from './reportHelper';
import BaseButton from '../../../components/BaseButton.vue';

export default {
  props: ["id", "data"],
  components: {
    ReportRowComponent,
    BaseButton,
  },
  
  // TODO refactor like DengueForm, implement abstract factory that takes backend_id and returns object...
  // ... this way it could also be used for report modal
  data() { 
    const fi_oral = new RowComponent('fi_oral', 'Oral Fluids', 'ml'); 
    const fi_parenteral = new RowComponent('fi_parenteral', 'Parenteral', 'ml');  
    const fi_other = new RowComponent('fi_other', 'Other', 'ml'); 
    const fi_eight_hrs = new RowComponent('fi_eight_hrs', 'In 8 Hrs.', 'ml'); 

    const fo_urine = new RowComponent('fo_urine', 'Urine', 'ml');
    const fo_uf = new RowComponent('fo_uf', 'UF', 'ml');
    const fo_emesis = new RowComponent('fo_emesis', 'Emesis', 'ml');
    const fo_drainage = new RowComponent('fo_drainage', 'Drainage', 'ml');
    const fo_eight_hrs = new RowComponent('fo_eight_hrs', 'In 8 Hrs.', 'ml');
    return {
      day_of_fever: new RowComponent('day_of_fever', 'Day of Fever'),
      fever: new RowComponent('fever', 'Fever', '°C'),
      pulse: new RowComponent('pulse', 'Pulse'),
      respiration: new RowComponent('respiration', 'Respiration'),
      bp_sys: new RowComponent('bp_sys', 'Blood Pressure'),
      bp_dia: new RowComponent('bp_dia', 'Diastolic'),
      diet: new RowComponent('diet', 'Diet'),

      fi_oral: fi_oral,
      fi_parenteral: fi_parenteral,
      fi_other: fi_other,
      fi_eight_hrs: fi_eight_hrs,
      fi_total: new TotalComponent('fi_total', 'Total', 'ml', null, [fi_oral, fi_parenteral, fi_other, fi_eight_hrs]),

      fo_urine: fo_urine,
      fo_uf: fo_uf,
      fo_emesis: fo_emesis,
      fo_drainage: fo_drainage,
      fo_eight_hrs: fo_eight_hrs,
      fo_total: new TotalComponent('fo_total', 'Total', 'ml', null, [fo_urine, fo_uf, fo_emesis, fo_drainage, fo_eight_hrs]),

      pain_score: new RowComponent('pain_score', 'Pain Score'),
      abd_cir: new RowComponent('abd_cir', 'Abd. Cir.', 'cm'),
      stools: new RowComponent('stools', 'Stools'),
      weight: new RowComponent('weight', 'Weight', 'kg'),
      height: new RowComponent('height', 'Height', 'kg'),
      o2sat: new RowComponent('o2sat', 'O2 Sat', '%'),
      hematocrit: new RowComponent('hematocrit', 'Hematocrit', '%'),
      platelet: new RowComponent('platelet', 'Platelet Count'),
      wbc: new RowComponent('wbc', 'WBC Count'),
      
      fluid_intake: new RowComponent('fluid_intake', 'Fluid Intake'),
      fluid_output: new RowComponent('fluid_output', 'Fluid Output'),

      daytime: new SelectComponent('daytime', 'Daytime', null, null, [{option: "D"}, {option: "E"}, {option: "N"}]),
      status: new SelectComponent('status', 'Status', null, null, [{option: "febrile"}, {option: "critical"}, {option: "recovery"}]),
      monitoring_interval: new SelectComponent('monitoring_interval', 'Monitoring Interval', 'hourly', null, [{option: 1}, {option: 2}, {option: 4}, {option: 6}]),

      warning_signs: new RowComponent('warning_signs', 'Warning Signs'),
      additional: new RowComponent('additional', 'Additional Info'),
      medical_advice: new RowComponent('medical_advice', 'Medical Advice'),

      editModal: false,
      updated_at: null,
      patientNumber: null,
      time: new RowComponent('datetime', 'Time'),
      history_id: null,
      urine: new JsonRowItem('urine', 'Urine'),
      weight_ht: null,
    };
  },
  computed: {
    report() {
      try {
        return this.$store.getters.getReportById(Number(this.id));
      } catch (e) {
        console.log(e);
        return null;
      }
    },
    sortedHistory() {
      if (this.report){
        const history = this.report.history;
        return history.sort((a, b) => new Date(a.datetime) - new Date(b.datetime));
      } else {
        return [];
      }
    },
    hasReport() {
      return this.report !== null && this.report !== undefined;
    },
    hasReportData() {
      // TODO consufing? The history contains the actual report. Deleting a report deletes it from the history
      // the report itself contains only the most current report information.
      return this.report !== null && this.report !== undefined && this.report.history[0];
    },
    backendJson() {
      const json = {}

      Object.keys(this.$data).forEach(key => {
        const item = this.$data[key];
        if(hasJsonNameAndValue(item)){
          const value = item.getJsonValue();
          json[item.backend_id] = value
        }
      });

      json['updated_at'] = Date.now();
      json['patient'] = this.id; //TODO this is unintuitive?

      return json
    },
  },
  methods: {
    openDateTimePicker(pickerName) {
      var input = this.$refs[pickerName].$el.firstChild.nextElementSibling;

      if (!input) {
        return;
      } else {
        input.click();
      }
    },
    getHistoryFor(id){
      const result = [];
      this.sortedHistory.forEach(element => {
        result.push(element[id]);
      });
      return result;
    },
    getHistoryTotalFor(items){
      const result = [];
      this.sortedHistory.forEach(element => {
        let total = 0;
        items.forEach(key => {
            total += +element[key] || 0;
        })
        result.push(total);
      });
      return result;
    },
    getReportFromHistory(reportId) {
      return reportId
        ? this.data.find((record) => record.history_id === reportId)
        : this.backendJson;
    },
    showEditModal(reportId) {
      this.selectedHistoryId = reportId;
      this.editModal = true;
      document.body.classList.add("modal-open");
    },
    onCloseModal(){
      this.editModal = false;
      document.body.classList.remove("modal-open");
    },
    createReport(){
      this.showEditModal(null);
    },
    addReport() {
      this.patientNumber = this.report.pk;
      this.showEditModal(null);
    },
    deleteReport(id) {
      if (confirm("Do you really want to delete this Report?")) {
        this.$store.dispatch("deleteReport", {id});
      }
    },
    clearData() {
      Object.keys(this.$data).forEach(key => {
        const item = this.$data[key];
        if(isRowItem(item))
          item.clearData();
      });

      this.date = null;
    },
  },
  destroyed() {
      document.body.classList.remove("modal-open");
  },
}
</script>

<style>
/*from https://stackoverflow.com/questions/19651293/how-to-use-word-wrapbreak-word-for-a-div-without-specifying-width */

.wordbreak {
  display: table;
  table-layout: fixed;
  width: 100%;
  word-break: break-all;
  white-space: -moz-pre-wrap; /* Mozilla */
  white-space: -o-pre-wrap; /* Opera 7 */
  white-space: pre-wrap; /* CSS 2.1 */
  white-space: pre-line; /* CSS 3 */
  word-wrap: break-word; /* IE */
}

thead {
  background-color: #f6f9fc;
}

tbody th:first-child,
td:first-child {
  z-index: 3;
  position: sticky;
  left: 0px;
  background-color: #f6f9fc;
}

.bottom-line {
  border-bottom-color: rgba(0, 0, 0, 0.05);
  border-bottom-style: solid;
  border-bottom-width: 1px;
}

.minInputColumnWidth10Rem {
  min-width: 10rem;
}

</style>