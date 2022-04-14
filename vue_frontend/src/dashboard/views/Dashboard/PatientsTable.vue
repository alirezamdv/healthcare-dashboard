<template>
  <div class="card" >
    <div class="card-header border-0">
      <div class="row align-items-center">
        <div class="col">
          <h3 class="row ml-0">{{ title }} 
            <i v-if="showOnlyCurrentPatients" class="far fa-question-circle text-muted"
              v-b-popover.hover.top="'Table shows all currently active patients. As soon as a patient is provided with a dismissal date the patient is moved to the dismissed patients table.'"></i>
            <!-- TODO -->
            <i v-else-if="showOnlyPatientsWithoutDiagnosis" class="far fa-question-circle text-muted"
              v-b-popover.hover.top="'TODO'"></i>
            <i v-else-if="showOnlyPatientsHavingAdmissionDate" class="far fa-question-circle text-muted"
              v-b-popover.hover.top="'Table shows all patients that have an admission date.'"></i>
            <i v-else class="far fa-question-circle text-muted"
               v-b-popover.hover.top="'Table shows all dismissed patients as soon as a dismissal date is set.'"></i>
          </h3>
          <div class="row ml-0">
            <div v-if="showWardFilter" class="col">
              <div class="row">
                <div class="col-0">
                <base-checkbox @input="checkShowWard" :checked="showWard"></base-checkbox>
                </div>
                <div class="col-0">
                Display only from ward
                </div>
                <div class="col-0">
                <base-dropdown v-if="showWard" class="col" menuClasses="wards">
                  <template v-slot:title>
                    <base-button type="secondary" size="sm" class="dropdown-toggle">
                      {{ward}}
                    </base-button>
                  </template>
                  <a class="dropdown-item" v-for="(item, index) in wards" :key="index" @click="selectWard(item)" >
                    {{ item }}
                    </a>
                </base-dropdown>
                </div>
              </div>
            </div>
              <div class="col" style="text-align: center; max-width: 100%">
              <base-button
                      v-if="showOnlyCurrentPatients" 
                      type="btn btn-sm btn-primary" 
                      icon="fas fa-plus"
                      size="lg"
                      @click="patientModal = true; newPatient = true"
                      v-b-popover.hover.top="'Register a new Patient'"
              >Register Patient
              </base-button>
              </div>
            </div>
        </div>
        <div>
          <register-patient-modal 
            v-if="patientModal"
            :show.sync="patientModal"
            :input="patientModalInput()"
            @close="onCloseModal"
          ></register-patient-modal>
        </div>
      </div>
    </div>

    <div>
      <div class="table-responsive">
        <base-table thead-classes="thead-light" :data="filteredSortedPatientData">
          <template slot="columns">
            <th @click="sort('id')"> <up-down-arrow-switcher :value="showSortArrow('id')"></up-down-arrow-switcher> ID </th>
            <th @click="sort('first_name')"> <up-down-arrow-switcher :value="showSortArrow('first_name')"></up-down-arrow-switcher> First Name </th>
            <th @click="sort('last_name')"> <up-down-arrow-switcher :value="showSortArrow('last_name')"></up-down-arrow-switcher> Last Name </th>
            <th @click="sort('gender')"> <up-down-arrow-switcher :value="showSortArrow('gender')"></up-down-arrow-switcher> Gender </th>
            <th @click="sort('age')"> <up-down-arrow-switcher :value="showSortArrow('age')"></up-down-arrow-switcher> Age </th>
            <th @click="sort('admission_date')"> <up-down-arrow-switcher :value="showSortArrow('admission_date')"></up-down-arrow-switcher> Admission </th>
            <th @click="sort('dismissal_date')"> <up-down-arrow-switcher :value="showSortArrow('dismissal_date')"></up-down-arrow-switcher> Dismissal </th>
            <th v-if="showDeletePatientButton">Edit/Delete <i class="far fa-question-circle" v-b-popover.hover.top="'Edit/Delete Patient'"></i></th>
            <th v-else>Edit <i class="far fa-question-circle" v-b-popover.hover.top="'Edit Patient'"></i></th>
            <th>Report <i class="far fa-question-circle" v-b-popover.hover.top="'See/Edit Patient Report'"></i></th>
          </template>

          <template slot-scope="{ row }" v-if="showPatient(row)">
            <th scope="row">
              <router-link :to="'/patients/' + row.id">{{
                  row.id
                }}
              </router-link>
            </th>
            <td>
              {{ row.first_name ? row.first_name : defaultValue}}
            </td>
            <td>
              {{ row.last_name ? row.last_name : defaultValue}}
            </td>
            <td>
              {{ row.gender ? row.gender : defaultValue }}
            </td>
            <td>
              {{ row.age ? row.age : defaultValue }}
            </td>
            <td>
              {{
                row.admission_date ?
                new Intl.DateTimeFormat("en-GB").format(
                    new Date(row.admission_date)
                ) : defaultValue
              }}
            </td>
            <td>
              <template v-if="patientData.admission_date">
                <base-button
                      type="btn btn-sm btn-primary" 
                      icon="fas fa-clock"
                      size="lg"
                      @click="dismissPatient(row)"
                      v-b-popover.hover.top="'Dismiss ' + row.first_name + ' ' + row.last_name">
                </base-button>
              </template>
              <template v-else>
                {{ row.dismissal_date ?
                  new Intl.DateTimeFormat("en-GB").format(
                      new Date(row.dismissal_date)
                  ) : defaultValue
                }}
              </template>
            </td>
            <td>
              <base-button class="btn btn-sm" icon="fas fa-edit" type="primary"
                           @click="initializePatientModal(row); edit = true"></base-button>
              <base-button v-if="showDeletePatientButton" class="btn btn-sm" icon="fas fa-trash-alt" type="danger"
                           @click="deletePatient(row.id)"></base-button>
            </td>
            <td>
              <router-link :to="'/patients/' + row.id">
                <base-button class="btn btn-sm" icon="fas fa-chart-bar" type="primary"
                             @click="'/patients/'+ row.id"> Patient Report
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
import BaseButton from '../../components/BaseButton.vue';
import UpDownArrowSwitcher from './UpDownArrowSwitcher.vue';
import RegisterPatientModal from './RegisterPatientModal.vue';

export default {
  name: "patients-table",
  components: {
    UpDownArrowSwitcher,
    BaseButton,
    RegisterPatientModal,
  },
  props: {
    title: String,
    showPatients: String,
    showDeletePatientButton: Boolean,
    showWardFilter: {
      type: Boolean,
      default: true,
    },
  },
  data() {
    return {
      defaultValue: '-',
      datepicker: false,
      patientModal: false,
      newPatient: true,
      patientId: null,
      edit: false,
      first_name: null,
      last_name: null,
      gender: null,
      age: null,
      hospital_number: null,
      currentSort:'id',
      currentSortDir:'ascending'
    };
  },
  methods: {
    checkShowWard(checked){
      this.$store.dispatch("showWard", checked);
    },
    selectWard(value){
      this.$store.dispatch("ward", value);
    },
    displayOnlyFromward(item) {
      console.log(item);
    },
    initializePatientModal(row) {
      this.currentPatientToEdit = row;
      this.newPatient = false;
      this.patientModal = true;
    },
    
    deletePatient(id) {
      if (confirm("Do you really want to delete this Patient?")) {
        this.$store.dispatch("deletePatient", id);
      }
    },
    dismissPatient(patient){
      const id = patient.id;
      this.$store.dispatch('dismissPatient', {id});
    },
    sort(id) {
      if(id === this.currentSort) {
        this.currentSortDir = this.currentSortDir==='ascending'?'descending':'ascending';
      } else {
        this.currentSortDir = 'ascending';
      }
      this.currentSort = id;
    },
    showSortArrow(id) {
      return id === this.currentSort
        ? this.currentSortDir
        : null;
    },
    showPatient(row) {
      if(this.showOnlyPatientsWithoutDiagnosis)
        return true;
      if(this.showOnlyCurrentPatients)
        return true;
      if(this.showOnlyDismissedPatients && row.dismissal_date)
        return true;
      if(this.showOnlyPatientsHavingAdmissionDate && row.admission_date && !row.dismissal_date)
        return true;
      return false;
    }, 
    sortPatientData() {
      return (a,b) => {
        let modifier = 1;
        if(this.currentSortDir === 'descending') modifier = -1;
        if(a[this.currentSort] < b[this.currentSort]) return -1 * modifier;
        if(a[this.currentSort] > b[this.currentSort]) return 1 * modifier;
        return 0;
      };
    },
    onCloseModal(){
      this.patientModal = false;
      this.currentPatientToEdit = null;
    },
    patientModalInput(){
      return {
        ...this.currentPatientToEdit,
        newPatient: this.newPatient,
      }
    }
  },
  beforeDestroy() {
    clearInterval(this.patientData);
  },
  computed: {
    ...mapGetters(["patientData", "patientsHavingNoDiagnosis", "showWard", "ward", "wards"]),
    showOnlyPatientsWithoutDiagnosis() {
     return this.showPatients === 'who need a diagnosis';
    },
    showOnlyDismissedPatients() {
      return this.showPatients === 'that are dismissed';
    },
    showOnlyCurrentPatients() {
      return this.showPatients === 'currently in the hospital';
    },
    showOnlyPatientsHavingAdmissionDate() {
      return this.showPatients === 'with admission';
    },
    patientsToDisplay()  {
      // only load patients without diagnosis if needed
      return this.showOnlyPatientsWithoutDiagnosis
        ? this.patientsHavingNoDiagnosis
        : this.patientData;
    },
    filteredSortedPatientData() {
      return [...this.patientsToDisplay]
        // TODO replace filter with actual filter function
        .filter(patient => this.showWard && this.showWardFilter
          ? patient.id % this.ward == 0
          : true)
        .sort(this.sortPatientData());
    },
  },
};
</script>
<style>

.datetime-picker {
  margin-top: 0.5rem;
}

.datetime-picker input {

  border: 1px solid #cad1d7;
  border-radius: 0.375rem;
  height: calc(1.5em + 1.25rem + 2px);
  padding-top: 0.625rem;
  padding-bottom: 0.625rem;
  font-size: 0.875rem;
  min-width: 0 !important;
  display: block;
  width: 100%;
  font-weight: 400;
  line-height: 1.5;
  color: #8898aa;
  background-color: #fff;
  background-clip: padding-box;
  -webkit-box-shadow: none;
  box-shadow: none;
  -webkit-transition: all 0.2s cubic-bezier(0.68, -0.55, 0.265, 1.55);
  transition: all 0.2s cubic-bezier(0.68, -0.55, 0.265, 1.55);

}

.vdatetime-popup {
  -webkit-box-sizing: border-box !important;
  box-sizing: border-box !important;
  z-index: 1000 !important;
  position: fixed !important;
  top: 50% !important;
  left: 50% !important;
  -webkit-transform: translate(-50%, -50%) !important;
  transform: translate(-50%, -50%) !important;
  width: 340px !important;
  max-width: calc(100% - 30px) !important;
  -webkit-box-shadow: 0 1px 3px 0 rgba(0, 0, 0, .3) !important;
  box-shadow: 0 1px 3px 0 rgba(0, 0, 0, .3) !important;
}

.modal {
  z-index: 5700 !important;
}

.form-group {
margin-bottom: 0rem;
}

.vdatetime-popup {
  z-index: 5900 !important;
}

.vdatetime-overlay {
  z-index: 5800 !important;
}

.picker-button {
  margin-right: 0 !important;
  max-width: 75% !important;
}

@media (min-width: 576px) {
  .modal-dialog {
    /*width: 745px;*/
    /*max-width: 745px;*/
    width: 80% !important;
    max-width: 800px !important;
  }
}

</style>
