<template>
  <div>
    <tabs>
      <tab title="General Information">
        <div class="row">
          <div class="col table-responsive">
            <table class="table table-hover" thead-classes="thead-light">
              <report-row-component
                :name="infos.age.name"
                :suffix="infos.age.placeholder"
              >
                <report-row-number
                  v-model="infos.age.value"
                  :placeholder="infos.age.placeholder"
                  max="100"
                ></report-row-number>
              </report-row-component>
            </table>
          </div>
          <div class="col table-responsive">
            <table class="table table-hover" thead-classes="thead-light">
              <report-row-component :name="infos.occ2.name">
                <report-row-select
                  v-model="infos.occ2.value"
                  :statusOptions="infos.occ2.statusOptions"
                ></report-row-select>
              </report-row-component>
            </table>
          </div>
        </div>
        <div class="row">
          <div class="col-6 table-responsive">
            <table class="table table-hover" thead-classes="thead-light">
              <report-row-component :name="infos.ud2.name">
                <report-row-select
                  v-model="infos.ud2.value"
                  :statusOptions="infos.ud2.statusOptions"
                ></report-row-select>
              </report-row-component>
            </table>
          </div>
        </div>
      </tab>
      <tab title="Symptoms">
        <div class="row">
          <div class="col table-responsive">
            <table class="table table-hover" thead-classes="thead-light">
              <report-row-component :name="symptoms.nausea.name">
                <report-row-select
                  v-model="symptoms.nausea.value"
                  :statusOptions="symptoms.nausea.statusOptions"
                ></report-row-select>
              </report-row-component>
            </table>
          </div>
          <div class="col table-responsive">
            <table class="table table-hover" thead-classes="thead-light">
              <report-row-component :name="symptoms.petechiae.name">
                <report-row-select
                  v-model="symptoms.petechiae.value"
                  :statusOptions="symptoms.petechiae.statusOptions"
                ></report-row-select>
              </report-row-component>
            </table>
          </div>
        </div>

        <div class="row">
          <div class="col table-responsive">
            <table class="table table-hover" thead-classes="thead-light">
              <report-row-component :name="symptoms.myalgia.name">
                <report-row-select
                  v-model="symptoms.myalgia.value"
                  :statusOptions="symptoms.myalgia.statusOptions"
                ></report-row-select>
              </report-row-component>
            </table>
          </div>
          <div class="col table-responsive">
            <table class="table table-hover" thead-classes="thead-light">
              <report-row-component :name="symptoms.bleeding.name">
                <report-row-select
                  v-model="symptoms.bleeding.value"
                  :statusOptions="symptoms.bleeding.statusOptions"
                ></report-row-select>
              </report-row-component>
            </table>
          </div>
        </div>
        <!-- Bleeding Categories Button -->
        <div class="row">
          <div class="col table-responsive">
            <table class="table table-hover" thead-classes="thead-light">
              <report-row-component :name="'Bleeding Categories'" heading>
                <div class="col text-center">
                  <button
                    class="btn btn-sm btn-primary"
                    v-on:click="toggleShowCategories"
                  >
                    {{ showCategories ? "Hide" : "Show" }} Bleeding Categories
                  </button>
                </div>
              </report-row-component>
            </table>
          </div>
        </div>
        <!-- Bleeding Categories -->

        <div class="row">
          <div class="col table-responsive">
            <table class="table table-hover" thead-classes="thead-light">
              <report-row-component
                v-if="showCategories"
                :name="symptoms.gum_bleeding.name"
              >
                <report-row-select
                  v-model="symptoms.gum_bleeding.value"
                  :statusOptions="symptoms.gum_bleeding.statusOptions"
                ></report-row-select>
              </report-row-component>
            </table>
          </div>
          <div class="col table-responsive">
            <table class="table table-hover" thead-classes="thead-light">
              <report-row-component
                v-if="showCategories"
                :name="symptoms.gastrointestinal_bleeding.name"
              >
                <report-row-select
                  v-model="symptoms.gastrointestinal_bleeding.value"
                  :statusOptions="
                    symptoms.gastrointestinal_bleeding.statusOptions
                  "
                ></report-row-select>
              </report-row-component>
            </table>
          </div>
        </div>
        <div class="row">
          <div class="col table-responsive">
            <table class="table table-hover" thead-classes="thead-light">
              <report-row-component
                v-if="showCategories"
                :name="symptoms.epistaxis.name"
              >
                <report-row-select
                  v-model="symptoms.epistaxis.value"
                  :statusOptions="symptoms.epistaxis.statusOptions"
                ></report-row-select>
              </report-row-component>
            </table>
          </div>
          <div class="col table-responsive">
            <table class="table table-hover" thead-classes="thead-light">
              <report-row-component
                v-if="showCategories"
                :name="symptoms.menstrual_bleeding.name"
              >
                <report-row-select
                  v-model="symptoms.menstrual_bleeding.value"
                  :statusOptions="symptoms.menstrual_bleeding.statusOptions"
                ></report-row-select>
              </report-row-component>
            </table>
          </div>
        </div>
        <div class="row">
          <div class="col table-responsive">
            <table class="table table-hover" thead-classes="thead-light">
              <report-row-component
                v-if="showCategories"
                :name="symptoms.other_mucosal_bleeding.name"
              >
                <report-row-select
                  v-model="symptoms.other_mucosal_bleeding.value"
                  :statusOptions="symptoms.other_mucosal_bleeding.statusOptions"
                ></report-row-select>
              </report-row-component>
            </table>
          </div>
          <div class="col table-responsive">
            <table class="table table-hover" thead-classes="thead-light">
              <report-row-component
                v-if="showCategories"
                :name="symptoms.other_bleeding.name"
              >
                <report-row-select
                  v-model="symptoms.other_bleeding.value"
                  :statusOptions="symptoms.other_bleeding.statusOptions"
                ></report-row-select>
              </report-row-component>
            </table>
          </div>
        </div>
      </tab>

      <tab title="Lab Results">
        <div class="row">
          <div class="col table-responsive">
            <table class="table table-hover" thead-classes="thead-light">
              <report-row-component :name="lab_results.tourniquettest.name">
                <report-row-select
                  v-model="lab_results.tourniquettest.value"
                  :statusOptions="lab_results.tourniquettest.statusOptions"
                ></report-row-select>
              </report-row-component>
            </table>
          </div>
          <div class="col table-responsive">
            <table class="table table-hover" thead-classes="thead-light">
              <report-row-component :name="lab_results.ns1.name">
                <report-row-select
                  v-model="lab_results.ns1.value"
                  :statusOptions="lab_results.ns1.statusOptions"
                ></report-row-select>
              </report-row-component>
            </table>
          </div>
        </div>
        <div class="row">
          <div class="col table-responsive">
            <table class="table table-hover" thead-classes="thead-light">
              <report-row-component
                :name="lab_results.ast.name"
                :suffix="lab_results.ast.placeholder"
              >
                <report-row-number
                  v-model="lab_results.ast.value"
                  :placeholder="lab_results.ast.placeholder"
                ></report-row-number>
              </report-row-component>
            </table>
          </div>
          <div class="col table-responsive">
            <table class="table table-hover" thead-classes="thead-light">
              <report-row-component
                :name="lab_results.alt.name"
                :suffix="lab_results.alt.placeholder"
              >
                <report-row-number
                  v-model="lab_results.alt.value"
                  :placeholder="lab_results.alt.placeholder"
                ></report-row-number>
              </report-row-component>
            </table>
          </div>
        </div>
        <div class="row">
          <div class="col table-responsive">
            <table class="table table-hover" thead-classes="thead-light">
              <report-row-component
                :name="lab_results.plt.name"
                :suffix="lab_results.plt.placeholder"
              >
                <report-row-number
                  v-model="lab_results.plt.value"
                  :placeholder="lab_results.plt.placeholder"
                ></report-row-number>
              </report-row-component>
            </table>
          </div>
          <div class="col table-responsive">
            <table class="table table-hover" thead-classes="thead-light">
              <report-row-component
                :name="lab_results.hct_d0.name"
                :suffix="lab_results.hct_d0.placeholder"
              >
                <report-row-number
                  v-model="lab_results.hct_d0.value"
                  :placeholder="lab_results.hct_d0.placeholder"
                ></report-row-number>
              </report-row-component>
            </table>
          </div>
        </div>
        <div class="row">
          <div class="col table-responsive">
            <table class="table table-hover" thead-classes="thead-light">
              <report-row-component
                :name="lab_results.wbc_d0.name"
                :suffix="lab_results.wbc_d0.placeholder"
              >
                <report-row-number
                  v-model="lab_results.wbc_d0.value"
                  :placeholder="lab_results.wbc_d0.placeholder"
                ></report-row-number>
              </report-row-component>
            </table>
          </div>
          <div class="col table-responsive">
            <table class="table table-hover" thead-classes="thead-light">
              <report-row-component
                :name="lab_results.lymp_d0.name"
                :suffix="lab_results.lymp_d0.placeholder"
              >
                <report-row-number
                  v-model="lab_results.lymp_d0.value"
                  :placeholder="lab_results.lymp_d0.placeholder"
                ></report-row-number>
              </report-row-component>
            </table>
          </div>
        </div>
        <div class="row">
          <div class="col-6 table-responsive">
            <table class="table table-hover" thead-classes="thead-light">
              <report-row-component
                :name="lab_results.atypl_d0.name"
                :suffix="lab_results.atypl_d0.placeholder"
              >
                <report-row-number
                  v-model="lab_results.atypl_d0.value"
                  :placeholder="lab_results.atypl_d0.placeholder"
                ></report-row-number>
              </report-row-component>
            </table>
          </div>
        </div>
      </tab>
    </tabs>
    <table
      id="dengue-diagnosis"
      class="table table-hover"
      thead-classes="thead-light"
    >
      <tr>
        <th><h3 class="text-uppercase">Dengue Probability</h3></th>
      </tr>
      <!-- TODO final diagnosis? -->

      <tr v-if="hasNoReport">
        <td>
          <div class="col text-center">
            <button
              class="btn btn-sm btn-primary"
              v-on:click="createDengueReport"
            >
              Get Dengue Probability
            </button>
          </div>
        </td>
        <td>
          <card type="default">
            <h5 class="h3 text-white mb-0" id="dengue-probability">
              {{ dengue_probability }}
            </h5>
          </card>
        </td>
      </tr>

      <tr v-else>
        <td>
          <div class="col text-center">
            <button
              class="btn btn-sm btn-primary"
              v-on:click="editDengueReport"
            >
              Update Dengue Report
            </button>
          </div>
        </td>

        <td>
          <dengue-probability-card
            :dengue_probability="parseInt(dengue_probability * 100)"
          ></dengue-probability-card>
          <div class="p-4"></div>
          <sensitivity-analysis-card
            :sensitivity_analysis="sensitivity_analysis"
          ></sensitivity-analysis-card>
        </td>
      </tr>
    </table>

    <disease-diagnosis :patient_id="patient_id" />
  </div>
</template>

<script>
import Tabs from "../../../components/Tabs/Tabs.vue";
import Tab from "../../../components/Tabs/Tab.vue";
import ReportRowComponent from "../reportComponents/ReportRowComponent";
import ReportRowNumber from "../reportComponents/ReportRowNumber.vue";
import ReportRowSelect from "../reportComponents/ReportRowSelect.vue";
import DengueProbabilityCard from "./DengueProbabilityCard.vue";
import SensitivityAnalysisCard from "./SensitivityAnalysisCard.vue";
import { hasJsonNameAndValue, isRowItem } from "./reportHelper";
import {
  AST,
  ALT,
  GumBleeding,
  GastrointestinalBleeding,
  Epistaxis,
  MenstrualBleeding,
  OtherMucosalBleeding,
  OtherBleeding,
  RowItemFactory,
} from "./dengueHelper";
import {
  Age,
  Occupation,
  UnderlyingDesease,
  Incidencerate,
  Nausea,
  Petechiae,
  Myalgia,
  Bleeding,
  BleedingCategories,
  TourniquetTest,
} from "./dengueHelper";
import {
  NS1,
  Platelets,
  Hematocrit,
  WhiteBloodCells,
  Lymphocytes,
  AtypicalLymphocytes,
  AST_ALT,
} from "./dengueHelper";
import DiseaseDiagnosis from "./DiseaseDiagnosis.vue";
import { Validators } from "./validators";
import { mapGetters } from "vuex";

export default {
  props: ["patient_id"],
  components: {
    Tabs,
    Tab,
    ReportRowComponent,
    ReportRowSelect,
    ReportRowNumber,
    DengueProbabilityCard,
    SensitivityAnalysisCard,
    DiseaseDiagnosis
  },
  created() {
    console.debug("created");
    this.setValuesFromBackend();
    if (this.hasNoFormErrors) this.fetchSmileResults();
  },
  data() {
    const ast = new AST();
    const alt = new ALT();

    const gum_bleeding = new GumBleeding();
    const gastrointestinal_bleeding = new GastrointestinalBleeding();
    const epistaxis = new Epistaxis();
    const menstrual_bleeding = new MenstrualBleeding();
    const other_mucosal_bleeding = new OtherMucosalBleeding();
    const other_bleeding = new OtherBleeding();

    const occ2 = new Occupation();
    occ2.validators = [Validators.required];
    const age = new Age();
    age.validators = [Validators.required];

    return {
      admission: null,
      dismissal: null,
      showCategories: false,
      showDengueDiagnosis: false,
      infos: {
        age: age,
        // TODO gender ? id: gender
        occ2: occ2,
        ud2: new UnderlyingDesease(),
        incidencerate: new Incidencerate(),
      },
      symptoms: {
        // TODO feverdays? use from normal report? id: feverdays
        nausea: new Nausea(),
        petechiae: new Petechiae(),
        myalgia: new Myalgia(),
        // TODO abdominal pain? id: abdominal_pain
        // TODO calf pain? id: calf_pain
        // TODO has fever? id: has_fever
        // TODO eschar? id: eschar
        bleeding: new Bleeding(),
        gum_bleeding: gum_bleeding,
        gastrointestinal_bleeding: gastrointestinal_bleeding,
        epistaxis: epistaxis,
        menstrual_bleeding: menstrual_bleeding,
        other_mucosal_bleeding: other_mucosal_bleeding,
        other_bleeding: other_bleeding,
        bleeding_categories: new BleedingCategories(
          gum_bleeding,
          gastrointestinal_bleeding,
          epistaxis,
          menstrual_bleeding,
          other_mucosal_bleeding,
          other_bleeding
        ),
      },
      lab_results: {
        tourniquettest: new TourniquetTest(),
        ns1: new NS1(),
        ast: ast,
        alt: alt,
        plt: new Platelets(),
        hct_d0: new Hematocrit(),
        wbc_d0: new WhiteBloodCells(),
        lymp_d0: new Lymphocytes(),
        atypl_d0: new AtypicalLymphocytes(),
        ast_alt: new AST_ALT(ast, alt),
      },
      final_diagnosis: {
        // TODO final diagnosis?
        // TODO calculate diagnosis / show diagnosis result?
      },
      disease: "Dengue",
      disease_diagnosis_status: "Not diagnosed",
      requires_hospitalization: false,
      informed_healthcare_workers: false,
      // TODO: Healthcare Workers Addresses
      healthcareAddress: "",
      innerHealthcareAddress: "",
    };
  },
  methods: {
    setValuesFromBackend() {
      const report = this.$store.getters.getDengueById(Number(this.patient_id));
      if (report) {
        this.backend_id = report.id;
        const reportWithLowercaseKeys = {};
        Object.entries(report).map(
          (entry) =>
            (reportWithLowercaseKeys[entry[0].toLowerCase()] = entry[1])
        );

        Object.keys(this.dengueFormData).forEach((key) => {
          const item = this.dengueFormData[key];
          const value = report[item.backend_id];
          item.setJsonValue(value);
        });
      }
    },
    async createCaseForHealthcare() {
      // TODO: Not up-to-date. Should be managed by "DiseaseDiagnosis".
      console.debug("create adress for Healthcare Worker Case");

      this.confirmDengueButtonIsLoading = true;
      var token = localStorage.getItem("token");

      let myHeaders = new Headers();
      myHeaders.append("Authorization", "Token " + token);
      myHeaders.append("Content-Type", "application/json");
      //myHeaders.append("Cookie", "csrftoken=eOk3XgzetS3h3k1QUGlpZe32DfUASPb9dMfULQ0eDBUxFY0OmfAFXu3ViCsD1VQ3; sessionid=obrxvinequ0mvwdt0nzsgr233y0fk9jv");

      let raw = JSON.stringify({
        patient_id: this.patient_id,
        // TODO Is the fallback value ok?
        physicalAddress: this.innerHealthcareAddress ?? "Uni Bremen",
        //TODO placeholder long and lat, maybe not send them
        longitude: 53.105166246,
        latitude: 8.852163258,
      });

      let requestOptions = {
        method: "POST",
        headers: myHeaders,
        body: raw,
        redirect: "follow",
      };
      const addressUrl =
        process.env.NODE_ENV === "production"
          ? "https://social.informatik.uni-bremen.de/api/addresses/"
          : "http://localhost:8000/api/addresses/";

      await fetch(addressUrl, requestOptions)
        .then((response) => response.text())
        .then((result) => console.log(result))
        .catch((error) => console.log("error", error));

      //TODO only hardcode for presentation now, we dont yet have the possiblity to input addresses

      console.debug("create Healthcare Worker Case");

      let mHeaders = new Headers();
      mHeaders.append("Authorization", "Token " + token);
      mHeaders.append("Content-Type", "application/json");
      //myHeaders.append("Cookie", "csrftoken=eOk3XgzetS3h3k1QUGlpZe32DfUASPb9dMfULQ0eDBUxFY0OmfAFXu3ViCsD1VQ3; sessionid=obrxvinequ0mvwdt0nzsgr233y0fk9jv");

      let raw1 = JSON.stringify({
        patient_id: this.patient_id,
      });

      let requestOptions1 = {
        method: "POST",
        headers: mHeaders,
        body: raw1,
        redirect: "follow",
      };

      const caseUrl =
        process.env.NODE_ENV === "production"
          ? "https://social.informatik.uni-bremen.de/api/case/"
          : "http://localhost:8000/api/case/";

      await fetch(caseUrl, requestOptions1)
        .then((response) => response.text())
        .then((result) => console.log(result))
        .catch((error) => console.log("error", error));
      this.confirmDengueButtonIsLoading = false;
    },
    async confirmDengue() {
      // TODO: Not up-to-date. Should be managed by "DiseaseDiagnosis"

      console.debug("confirm Diagnosis");
      this.confirmDengueButtonIsLoading = true;

      if (this.requiresHospitalization) {
        console.debug("(createCaseForHealthcare) requiresHospitalization");
        this.$store.dispatch("requiresHospitalization", {
          id: Number(this.patient_id),
        });
      }

      const token = localStorage.getItem("token");
      const myHeaders = new Headers();
      myHeaders.append("Authorization", "Token " + token);
      myHeaders.append("Content-Type", "application/json");

      let raw = JSON.stringify({
        patient_id: this.patient_id,
        disease_type: "Dengue",
        status: this.dengueStatus,
        note: "string",
        //TODO use the correct user.
        changed_by: this.user,
      });

      let requestOptions = {
        method: "POST",
        headers: myHeaders,
        body: raw,
        redirect: "follow",
      };

      const diagnosisUrl =
        process.env.NODE_ENV === "production"
          ? "https://social.informatik.uni-bremen.de/api/diagnosis/"
          : "http://localhost:8000/api/diagnosis/";

      await fetch(diagnosisUrl, requestOptions)
        .then((response) => response.text())
        .then((result) => console.log(result))
        .catch((error) => console.log("error", error));

      if (this.healthCareSelected) await this.createCaseForHealthcare();
      else this.confirmDengueButtonIsLoading = false;
    },
    toggleShowCategories() {
      this.showCategories = !this.showCategories;
    },
    createDengueReport() {
      console.debug("createDengueReport");
      if (this.formErrors) {
        this.$store.dispatch("newNotification", this.formErrorNotification);
      } else {
        this.$store.dispatch("createDengue", this.backendJson);
        this.$store.dispatch("calculateDengueProbability", {
          id: Number(this.patient_id),
          smileEngineJson: this.smileEngineJson,
        });
      }
    },
    changeProb(result) {
      this.dengue_probability = result;
    },
    editDengueReport() {
      console.debug("editDengueReport");
      if (this.formErrors) {
        this.$store.dispatch("newNotification", this.formErrorNotification);
      } else {
        this.$store.dispatch("editDengue", {
          id: this.backend_id,
          payload: this.backendJson,
        });
        this.$store.dispatch("calculateDengueProbability", {
          id: Number(this.patient_id),
          smileEngineJson: this.smileEngineJson,
        });
      }
    },
    deleteDengueReport() {
      console.debug("deleteDengueReport");
      this.$store.dispatch("deleteDengue", { id: this.backend_id });
      this.clearForm();
    },
    clearForm() {
      Object.keys(this.dengueFormData).forEach((key) => {
        const item = this.dengueFormData[key];
        if (isRowItem(item)) item.clearData();
      });
    },
    async fetchSmileResults() {
      console.debug("fetchSmileResults");
      this.$store.dispatch("calculateDengueProbability", {
        id: Number(this.patient_id),
        smileEngineJson: this.smileEngineJson,
      });
    },
  },
  computed: {
    ...mapGetters(["getSmileResult"]),
    smileResult() {
      return this.getSmileResult(Number(this.patient_id)) ?? {};
    },
    dengueFormData() {
      return {
        ...this.infos,
        ...this.symptoms,
        ...this.lab_results,
        ...this.final_diagnosis,
      };
    },
    formErrors() {
      let errors = [];

      Object.keys(this.dengueFormData).forEach((key) => {
        const item = this.dengueFormData[key];
        if (item.validator) {
          const value = item.validator();
          if (value) {
            errors.push(value);
          }
        }
      });

      return errors.length === 0 ? null : errors;
    },
    hasNoFormErrors() {
      return !this.formErrors;
    },
    formErrorNotification() {
      const formErrorNotificationString = this.formErrors
        .map(
          (formError) =>
            `${Object.keys(formError)[0]} (${formError[
              Object.keys(formError)[0]
            ].join(", ")})`
        )
        .join(", ");
      return [{ title: "Invalid forms", message: formErrorNotificationString }];
    },
    hasReport() {
      //TODO? we are doing this getter request very often.
      // i dont know if it is already being cached and not expensive,
      // otherwise we should store report ourselves.
      const report = this.$store.getters.getDengueById(Number(this.patient_id));
      if (report) {
        return true;
      } else {
        return false;
      }
    },
    hasNoReport() {
      return !this.hasReport;
    },
    backendJson() {
      const json = {};

      Object.keys(this.dengueFormData).forEach((key) => {
        const item = this.dengueFormData[key];
        if (hasJsonNameAndValue(item)) {
          const value = item.getJsonValue();
          if (value) {
            json[item.backend_id] = value;
          }
        }
      });

      json["patient_id"] = this.patient_id;

      return json;
    },
    smileEngineJson() {
      const json = {};

      Object.keys(this.dengueFormData).forEach((key) => {
        const item = this.dengueFormData[key];
        if (item.toSMILEEngine) {
          const value = item.toSMILEEngine();
          if (value) {
            json[item.backend_id] = value;
          }
        }
      });

      return json;
    },
    dengue_probability() {
      let probability = this.smileResult.dengue_probability;

      probability = probability ?? "Not enough data";

      if (!(typeof probability == "string")) {
        probability = parseFloat(probability).toFixed(4) * 100 + "%";
      }

      return probability;
    },
    sensitivity_analysis() {
      const impact_of_missing_inputs =
        this.smileResult.impact_of_missing_inputs;
      return impact_of_missing_inputs
        ? Object.entries(impact_of_missing_inputs).map(([key, value]) =>
            RowItemFactory.create(key, value)
          )
        : [];
    },
    dengueStatus() {
      // TODO: Should be managed by "DiseaseDiagnosis".
      return this.confirmedDengue
        ? "Confirmed"
        : this.suspectedDengue
        ? "Suspected"
        : "Negative";
    },
    confirmedDengue() {
      // TODO: Should be managed by "DiseaseDiagnosis".
      return (
        this.disease == "Dengue" && this.disease_diagnosis_status == "Confirmed"
      );
    },
    suspectedDengue() {
      // TODO: Should be managed by "DiseaseDiagnosis".
      return (
        this.disease == "Dengue" && this.disease_diagnosis_status == "Suspected"
      );
    },
  },
  watch: {
    // TODO: Adjust watch over Dengue Status
    confirmedDengue(newValue) {
      // TODO: Should be managed by "DiseaseDiagnosis".
      if (newValue) this.suspectedDengue = false;
    },
    suspectedDengue(newValue) {
      // TODO: Should be managed by "DiseaseDiagnosis".
      if (newValue) this.confirmedDengue = false;
    },
    hasReport() {
      const report = this.$store.getters.getDengueById(Number(this.patient_id));
      if (report) {
        this.backend_id = report.id;
      }
    },
    healthcareAddress() {
      // TODO: Should be managed by "DiseaseDiagnosis".
      this.innerHealthcareAddress = this.healthcareAddress;
    },
    healthCareSelected(newValue) {
      // TODO: Should be managed by "DiseaseDiagnosis".
      if (newValue) this.innerHealthcareAddress = this.healthcareAddress;
      else this.innerHealthcareAddress = "";
    },
  },
};
</script>
<style>
</style>
