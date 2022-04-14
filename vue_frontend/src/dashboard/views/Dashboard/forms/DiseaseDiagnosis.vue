<template>
  <div>
    <!-- Disease Diagnosis -->
    <div class="row">
      <div class="col-lg-4 col-md-6 table-responsive">
        <table class="table table-hover" thead-classes="thead-light">
          <report-row-component :name="this.disease_label">
            <select
              class="form-control"
              v-model="disease"
              v-on:change="this.update_disease_diagnosis"
            >
              <option
                type="text"
                v-for="disease_option in this.disease_options"
                v-bind:key="disease_option"
                v-bind:value="disease_option"
              >
                {{ disease_option }}
              </option>
            </select>
          </report-row-component>
        </table>
      </div>
      <div class="col-lg-4 col-md-6 table-responsive">
        <table class="table table-hover" thead-classes="thead-light">
          <report-row-component :name="this.disease_diagnosis_status_label">
            <select
              class="form-control"
              v-model="disease_diagnosis_status"
              v-on:change="this.update_disease_diagnosis"
            >
              <option
                type="text"
                v-for="disease_diagnosis_status_option in this
                  .disease_diagnosis_status_options"
                v-bind:key="disease_diagnosis_status_option"
                v-bind:value="disease_diagnosis_status_option"
              >
                {{ disease_diagnosis_status_option }}
              </option>
            </select>
          </report-row-component>
        </table>
      </div>
      <div class="col-lg-4 col-md-12 table-responsive">
        <table class="table table-hover" thead-classes="thead-light">
          <report-row-component :name="this.disease_diagnosis_note_label">
            <input
              class="form-control"
              v-model="disease_diagnosis_note"
              v-on:change="this.update_disease_diagnosis"
            />
          </report-row-component>
        </table>
      </div>
    </div>

    <!-- Checkboxes for Hospitalization and Healthcare Workers -->
    <div class="row">
      <div class="col-6">
        <input
          id="inform_healthcare_workers_checkbox"
          type="checkbox"
          v-model="inform_healthcare_workers"
          v-on:change="this.update_healthcare_workers_info"
        />
        <label
          class="ml-2"
          for="inform_healthcare_workers_checkbox"
        >
          Inform Healthcare Workers
        </label>
      </div>
      <div class="col-6">
        <input
          id="requires_hospitalization_checkbox"
          type="checkbox"
           
          v-model="requires_hospitalization"
          v-on:change="this.update_requires_hospitalization"
        />
        <label
          class="ml-2"
          for="requires_hospitalization_checkbox"
        >
          Requires Hospitalization
        </label>
        
 
    </div>
     </div>
  <div>
        <base-button
            class="mb-5"
            type="btn btn-block btn-primary"
            icon="fas fa-clock"
            size="md"
            style="marginTop:40px"
            @click="confirmDengue()"
            >Create Diagnose
          </base-button>
</div>
    <!-- Healthcare Workers Addresses -->
    <div class="row my-4 mt-6">
      <button
        class="btn btn-block btn-secondary d-flex justify-content-around"
        v-on:click="toggle_show_addresses"
      >
        <span>
          {{ this.show_hide_mapping[this.show_healthcare_workers_addresses] }}
          <strong>Addresses for Healthcare Workers</strong>
        </span>
        <span class="badge badge-info">
          {{ this.healthcare_workers_addresses.length }} Addresses
        </span>
      </button>
    </div>

    <div
      v-if="show_healthcare_workers_addresses"
    >
      <healthcare-workers-address
        v-for="(address, address_index) in this.healthcare_workers_addresses"
        v-bind:key="address_index"
        :patient_id="patient_id"
        :address_index="address_index"
        :new="false"
      />
      <div class="d-flex justify-content-between">
        <strong>Adding a new address</strong>
        <button
          class="btn btn-primary"
          v-on:click="add_address"
        >
          Add the address below
        </button>
      </div>
      <healthcare-workers-address
        :patient_id="patient_id"
        :address_index="this.healthcare_workers_addresses.length"
        v-bind:key="this.healthcare_workers_addresses.length"
        :new="true"
      />
    </div>
  </div>
</template>

<script>
import ReportRowComponent from "../reportComponents/ReportRowComponent";
import HealthcareWorkersAddress from "./HealthcareWorkersAddress.vue";

export default {
  name: "disease-diagnosis",
  props: {
    patient_id: {
      type: String,
      description: "ID of the Patient",
    }
  },
  components: {
    ReportRowComponent,
    HealthcareWorkersAddress
  },
  created() {
    console.debug("Disease Diagnosis created");
  },
  data() {
    return {
      disease_label: "Disease",
      disease_diagnosis_status_label: "Disease Diagnosis Status",
      disease_diagnosis_note_label: "Note",
      disease_model: this.disease,
      disease_diagnosis_status_model: this.disease_diagnosis_status,
      disease_options: ["Dengue", "DHF", "Influenza", "Other"],
      disease_diagnosis_status_options: [
        "Not diagnosed",
        "Suspected",
        "Confirmed",
      ],
      disease: "Dengue",
      disease_diagnosis_status: "Not diagnosed",
      disease_diagnosis_note: "",
      requires_hospitalization: false,
      is_hospitalized: false,
      inform_healthcare_workers: false,
      informed_healthcare_workers: false,
      healthcare_workers_addresses: [],
      show_healthcare_workers_addresses: false,
      show_hide_mapping: {
        false: "Show",
        true: "Hide"
      }
    };
  },
     
  methods: {
    update_disease_diagnosis() {
      console.log("TODO: Modify disease diagnosis database entry");
    },
    update_healthcare_workers_info() {
      console.log("TODO: Modify healthacre workers database entry and send it");
    },
    update_requires_hospitalization() {
      console.log("TODO: Modify requires hospitalization in database");
    },
    toggle_show_addresses() {
      this.show_healthcare_workers_addresses = !this.show_healthcare_workers_addresses
    },
    add_address() {
      this.healthcare_workers_addresses.push(
        this.healthcare_workers_addresses.length
      )
      console.log("Address added")
    },
    //TODO insert this again to see cases in healthcare workers app
    //  async createCaseForHealthcare() {
    //   // TODO: Not up-to-date. Should be managed by "DiseaseDiagnosis".
    //   console.debug("create adress for Healthcare Worker Case");

    //   this.confirmDengueButtonIsLoading = true;
    //   var token = localStorage.getItem("token");

    //   let myHeaders = new Headers();
    //   myHeaders.append("Authorization", "Token " + token);
    //   myHeaders.append("Content-Type", "application/json");
    //   //myHeaders.append("Cookie", "csrftoken=eOk3XgzetS3h3k1QUGlpZe32DfUASPb9dMfULQ0eDBUxFY0OmfAFXu3ViCsD1VQ3; sessionid=obrxvinequ0mvwdt0nzsgr233y0fk9jv");

    //   let raw = JSON.stringify({
    //     patient_id: this.patient_id,
    //     // TODO Is the fallback value ok?
    //     physicalAddress: this.innerHealthcareAddress ?? "Uni Bremen",
    //     //TODO placeholder long and lat, maybe not send them
    //     longitude: 53.105166246,
    //     latitude: 8.852163258,
    //   });

    //   let requestOptions = {
    //     method: "POST",
    //     headers: myHeaders,
    //     body: raw,
    //     redirect: "follow",
    //   };
    //   const addressUrl =
    //     process.env.NODE_ENV === "production"
    //       ? "https://social.informatik.uni-bremen.de/api/addresses/"
    //       : "http://localhost:8000/api/addresses/";

    //   await fetch(addressUrl, requestOptions)
    //     .then((response) => response.text())
    //     .then((result) => console.log(result))
    //     .catch((error) => console.log("error", error));

    //   //TODO only hardcode for presentation now, we dont yet have the possiblity to input addresses

    //   console.debug("create Healthcare Worker Case");

    //   let mHeaders = new Headers();
    //   mHeaders.append("Authorization", "Token " + token);
    //   mHeaders.append("Content-Type", "application/json");
    //   //myHeaders.append("Cookie", "csrftoken=eOk3XgzetS3h3k1QUGlpZe32DfUASPb9dMfULQ0eDBUxFY0OmfAFXu3ViCsD1VQ3; sessionid=obrxvinequ0mvwdt0nzsgr233y0fk9jv");

    //   let raw1 = JSON.stringify({
    //     patient_id: this.patient_id,
    //   });

    //   let requestOptions1 = {
    //     method: "POST",
    //     headers: mHeaders,
    //     body: raw1,
    //     redirect: "follow",
    //   };

    //   const caseUrl =
    //     process.env.NODE_ENV === "production"
    //       ? "https://social.informatik.uni-bremen.de/api/case/"
    //       : "http://localhost:8000/api/case/";

    //   await fetch(caseUrl, requestOptions1)
    //     .then((response) => response.text())
    //     .then((result) => console.log(result))
    //     .catch((error) => console.log("error", error));
    //   this.confirmDengueButtonIsLoading = false;
    // },
   async confirmDengue() {
      // TODO: Not up-to-date. Should be managed by "DiseaseDiagnosis"

      console.debug("confirm Diagnosis");
      // this.confirmDengueButtonIsLoading = true;

      if (this.requires_hospitalization) {
        console.debug("(createCaseForHealthcare) requiresHospitalization");
        this.$store.dispatch("requiresHospitalization", {
          id: Number(this.patient_id),
        });
      }
      if(!this.requires_hospitalization){
      this.$store.dispatch("dismissPatient", {
          id: Number(this.patient_id),
        });
      }

      // const token = localStorage.getItem("token");
      // const myHeaders = new Headers();
      // myHeaders.append("Authorization", "Token " + token);
      // myHeaders.append("Content-Type", "application/json");

      // let raw = JSON.stringify({
      //   patient_id: this.patient_id,
      //   disease_type: "Dengue",
      //   status: this.dengueStatus,
      //   note: "string",
      //   //TODO use the correct user.
      //   changed_by: this.user,
      // });

      // let requestOptions = {
      //   method: "POST",
      //   headers: myHeaders,
      //   body: raw,
      //   redirect: "follow",
      // };

      // const diagnosisUrl =
      //   process.env.NODE_ENV === "production"
      //     ? "https://social.informatik.uni-bremen.de/api/diagnosis/"
      //     : "http://localhost:8000/api/diagnosis/";

      // await fetch(diagnosisUrl, requestOptions)
      //   .then((response) => response.text())
      //   .then((result) => console.log(result))
      //   .catch((error) => console.log("error", error));

      // if (this.healthCareSelected) await this.createCaseForHealthcare();
      // else this.confirmDengueButtonIsLoading = false;
    },
  },
  computed: {
    dengueStatus() {
      if (this.disease == "Dengue" || this.disease == "DHF") {
        return this.disease_diagnosis_status;
      } else {
        return null;
      }
    },
    confirmedDengue() {
      return this.dengueStatus != null && this.dengueStatus == "Confirmed";
    },
    suspectedDengue() {
      return this.dengueStatus != null && this.dengueStatus == "Suspected";
    },
  },
  watch: {},
};
</script>

<style>
</style>
