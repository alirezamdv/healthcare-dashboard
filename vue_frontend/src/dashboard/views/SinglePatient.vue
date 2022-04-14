<template>
  <div class="singlePatient">
    <base-header
      type=""
      class="pb-6 pb-8 pt-5 pt-md-8"
      style="background-color: #dbe5f3"
    >
      <div>
        <modal :show.sync="editModal">
          <template slot="header">
            <h2 class="modal-title">DHF Prediction</h2>
            <br />
          </template>
          <section class="modal-body">
            <slot name="body">
              Until the latest prediction model is integrated, we use
              placeholder values for almost all parameters needed.
              <br />
              Only day 3 pulse and temperature is used.
            </slot>
          </section>
          <div class="mr-auto">
            <strong>Day 3 Pulse and Temperature </strong> needs to be submitted.
          </div>
          <template slot="footer">
            <!-- <div class="mr-auto">Day 3 Pulse and Temperature needs to be set</div> -->
            <base-button type="secondary" @click="editModal = false">
              Close
            </base-button>
          </template>
        </modal>
      </div>

      <div class="row">
        <div class="col-xl-8 mb-5 mb-xl-0">
          <h1>{{ patientData.first_name }} {{ patientData.last_name }}</h1>
          <h5 v-if="!patientData.admission_date && !patientData.dismissal_date" class="text-uppercase text-muted">
          Create Diagnosis to admit patient to the hospital.
          </h5>
          <h5 v-if="patientData.admission_date" class="text-uppercase text-muted">
            (Admission:
            {{
              new Date(patientData.admission_date).toLocaleDateString("en-GB")
            }})
          </h5>
          <h5
            v-if="patientData.dismissal_date"
            class="text-uppercase text-muted"
          >
            (Dismissal:
            {{
              new Date(patientData.dismissal_date).toLocaleDateString("en-GB")
            }})
          </h5>
          <base-button
            v-if="patientData.admission_date"
            class="mb-5"
            type="btn btn-sm btn-primary"
            icon="fas fa-clock"
            size="lg"
            @click="dismissPatient(patientData)"
            v-b-popover.hover.top="
              'Dismiss ' + patientData.first_name + ' ' + patientData.last_name
            "
            >Dismiss Patient
          </base-button>
          <base-alert
            type="success text-center"
            v-if="this.status === 'febrile'"
            ><i class="fa fa-exclamation-triangle mr-2"></i> Patient is in the
            febrile phase
          </base-alert>

          <base-alert
            type="danger text-center"
            v-if="this.status === 'critical'"
            ><i class="fa fa-exclamation-triangle mr-2"></i> Patient is in the
            critical phase
          </base-alert>

          <base-alert
            type="primary text-center"
            v-if="this.status === 'recovery'"
            ><i class="fa fa-exclamation-triangle mr-2"></i> Patient is in the
            recovery phase
          </base-alert>
        </div>
        <div class="col-xl-4">
          <card header-classes="bg-transparent">
            <div class="row mb-4">
              <div class="col-4">



                <h5 class="h3 mb-0">
                  <!-- Number.parseFloat(x).toPrecision(4); -->
                  Dengue Probability:
                </h5>
                <!-- <small>in %</small> -->

              </div>

              <div class="col-8">
                <span class="btn btn-secondary btn-block" disabled>
                  <span class="font-weight-bold text-monospace">{{
                    dengue_probability
                  }}
                  </span>
                  <span
                  v-if="this.dengue_status == 'Confirmed'"
                  class="badge badge-danger"
                >
                  Dengue confirmed by doctor
                </span>
                <span
                  v-if="this.dengue_status == 'Suspected'"
                  class="badge badge-warning"
                >
                  Dengue suspected by doctor
                </span>
                <span
                  v-if="this.dengue_status == 'Negative'"
                  class="badge badge-success"
                >
                  <!-- No Dengue confirmed by doctor -->
                </span>
                <span v-else class="badge badge-info">
                  No Dengue assessment by doctor
                </span>
                </span>

              </div>
            </div>

            <div class="row mt-4">
              <div class="col-4">
                <h5 class="h3">
                  DHF Probability:
                </h5>
                <!-- <small>in %</small> -->
              </div>

              <div class="col-8">
                <a
                  class="btn btn-secondary btn-block"
                  href="#"
                  @click="editModal = true"
                >
                  <span class="text-monospace">{{ dhf_probability }}</span><br />
                  DHF Details
                </a>


              </div>
            </div>
          </card>
        </div>
      </div>
    </base-header>

    <!--    BEGIN CHARTS -->
    <div v-if="charts1">
      <div class="container-fluid mt--7">
        <template v-if="this.reportData">
          <div class="row">
            <div class="col-xl-8 mb-5 mb-xl-0">
              <card type="default" header-classes="bg-transparent">
                <div slot="header" class="row align-items-center">
                  <div class="col">
                    <h6
                      v-if="feverChart.activeIndex === 0"
                      class="text-muted text-uppercase ls-1 mb-1"
                    >
                      Today ({{ new Date().toLocaleDateString() }})
                    </h6>
                    <h6 v-else class="text-light text-uppercase ls-1 mb-1">
                      Course
                    </h6>
                    <h5 class="h3 text-white mb-0">Temperature/Pulse</h5>

                    <small class="text-white">Temperature in °C</small>
                  </div>
                  <div class="col">
                    <ul class="nav nav-pills justify-content-end">
                      <li class="nav-item mr-2 mr-md-0">
                        <a
                          class="nav-link py-2 px-3"
                          href="#"
                          :class="{ active: feverChart.activeIndex === 0 }"
                          @click.prevent="initBigChart(0)"
                        >
                          <span class="d-none d-md-block">Day</span>
                          <span class="d-md-none">D</span>
                        </a>
                      </li>
                      <li class="nav-item">
                        <a
                          class="nav-link py-2 px-3"
                          href="#"
                          :class="{ active: feverChart.activeIndex === 1 }"
                          @click.prevent="initBigChart(1)"
                        >
                          <span class="d-none d-md-block">Course</span>
                          <span class="d-md-none">C</span>
                        </a>
                      </li>
                    </ul>
                  </div>
                </div>
                <line-chart
                  :height="350"
                  :v-if="feverChart.loaded"
                  :chart-data="feverChart.chartData"
                  :extra-options="feverChart.extraOptions"
                >
                </line-chart>
              </card>
            </div>

            <div class="col-xl-4">
              <card header-classes="bg-transparent">
                <div slot="header" class="row align-items-center">
                  <div class="col">
                    <h6
                      v-if="redBarChart.activeIndex === 0"
                      class="text-muted text-uppercase ls-1 mb-1"
                    >
                      Today ({{ new Date().toLocaleDateString() }})
                    </h6>
                    <h6 v-else class="text-uppercase text-muted ls-1 mb-1">
                      Course
                    </h6>
                    <h5 class="h3 mb-0">Fluid Input/Output</h5>
                    <small>in ml</small>
                  </div>

                  <div class="col">
                    <ul class="nav nav-pills justify-content-end">
                      <li class="nav-item mr-2 mr-md-0">
                        <a
                          class="nav-link py-2 px-3"
                          href="#"
                          :class="{ active: redBarChart.activeIndex === 0 }"
                          @click.prevent="initBarChart(0)"
                        >
                          <span class="d-none d-md-block">Day</span>
                          <span class="d-md-none">D</span>
                        </a>
                      </li>
                      <li class="nav-item">
                        <a
                          class="nav-link py-2 px-3"
                          href="#"
                          :class="{ active: redBarChart.activeIndex === 1 }"
                          @click.prevent="initBarChart(1)"
                        >
                          <span class="d-none d-md-block">Course</span>
                          <span class="d-md-none">C</span>
                        </a>
                      </li>
                    </ul>
                  </div>
                </div>

                <bar-chart
                  :height="350"
                  ref="barChart"
                  :chart-data="redBarChart.chartData"
                >
                </bar-chart>
              </card>
            </div>
          </div>
          <!-- End charts-->
        </template>

        <!--End tables-->
      </div>
    </div>
    <div v-else>
      <div class="container-fluid mt--7">
        <template v-if="this.reportData">
          <div class="row">
            <div class="col-xl-8 mb-5 mb-xl-0">
              <card type="default" header-classes="bg-transparent">
                <div slot="header" class="row align-items-center">
                  <div class="col">
                    <h6
                      v-if="respChart.activeIndex === 0"
                      class="text-muted text-uppercase ls-1 mb-1"
                    >
                      Today ({{ new Date().toLocaleDateString() }})
                    </h6>
                    <h6 v-else class="text-light text-uppercase ls-1 mb-1">
                      Course
                    </h6>
                    <h5 class="h3 text-white mb-0">
                      Respirations/Blood Pressure
                    </h5>

                    <small class="text-white">-</small>
                  </div>
                  <div class="col">
                    <ul class="nav nav-pills justify-content-end">
                      <li class="nav-item mr-2 mr-md-0">
                        <a
                          class="nav-link py-2 px-3"
                          href="#"
                          :class="{ active: respChart.activeIndex === 0 }"
                          @click.prevent="initRespChart(0)"
                        >
                          <span class="d-none d-md-block">Day</span>
                          <span class="d-md-none">D</span>
                        </a>
                      </li>
                      <li class="nav-item">
                        <a
                          class="nav-link py-2 px-3"
                          href="#"
                          :class="{ active: respChart.activeIndex === 1 }"
                          @click.prevent="initRespChart(1)"
                        >
                          <span class="d-none d-md-block">Course</span>
                          <span class="d-md-none">C</span>
                        </a>
                      </li>
                    </ul>
                  </div>
                </div>
                <line-chart
                  :height="350"
                  :v-if="respChart.loaded"
                  :chart-data="respChart.chartData"
                  :extra-options="respChart.extraOptions"
                >
                </line-chart>
              </card>
            </div>

            <div class="col-xl-4">
              <card header-classes="bg-transparent">
                <div slot="header" class="row align-items-center">
                  <div class="col">
                    <h6
                      v-if="balanceChart.activeIndex === 0"
                      class="text-muted text-uppercase ls-1 mb-1"
                    >
                      Today ({{ new Date().toLocaleDateString() }})
                    </h6>
                    <h6 v-else class="text-uppercase text-muted ls-1 mb-1">
                      Course
                    </h6>
                    <h5 class="h3 mb-0">Fluid Balance</h5>
                    <small>in ml</small>
                  </div>

                  <div class="col">
                    <ul class="nav nav-pills justify-content-end">
                      <li class="nav-item mr-2 mr-md-0">
                        <a
                          class="nav-link py-2 px-3"
                          href="#"
                          :class="{ active: balanceChart.activeIndex === 0 }"
                          @click.prevent="initBalanceChart(0)"
                        >
                          <span class="d-none d-md-block">Day</span>
                          <span class="d-md-none">D</span>
                        </a>
                      </li>
                      <li class="nav-item">
                        <a
                          class="nav-link py-2 px-3"
                          href="#"
                          :class="{ active: balanceChart.activeIndex === 1 }"
                          @click.prevent="initBalanceChart(1)"
                        >
                          <span class="d-none d-md-block">Course</span>
                          <span class="d-md-none">C</span>
                        </a>
                      </li>
                    </ul>
                  </div>
                </div>

                <bar-chart
                  :height="350"
                  ref="balanceChart"
                  :chart-data="balanceChart.chartData"
                >
                </bar-chart>
              </card>
            </div>
          </div>
          <!-- End charts-->
        </template>

        <!--End tables-->
      </div>
    </div>

    <!--    CHART SWITCH -->

    <div class="divider"></div>

    <div class="container-fluid">
      <!--      <div class="col">-->
      <ul class="nav nav-pills justify-content-end">
        <li class="nav-item mb-2 mr-2 mr-md-0">
          <a
            class="nav-link py-2 px-3"
            href="#"
            :class="{ active: charts1 === true }"
            @click.prevent="charts1 = true"
          >
            <span class="d-none d-md-block"
              >Temperature, Pulse, Fluid Input/Output</span
            >
            <span class="d-md-none">Temperature, Pulse, Fluid Input/Output</span>
          </a>
        </li>
        <li class="nav-item mb-2 mr-2 mr-md-0">
          <a
            class="nav-link py-2 px-3"
            href="#"
            :class="{ active: charts1 === false }"
            @click.prevent="charts1 = false"
          >
            <span class="d-none d-md-block"
              >Respiration, Blood Pressure, Fluid Balance</span
            >
            <span class="d-md-none"
              >Respiration, Blood Pressure, Fluid Balance</span
            >
          </a>
        </li>
      </ul>
      <!--    </div>-->
    </div>

    <!--    END CHARTS -->

    <!-- INPUT NEW REPORT -->
    <div class="container-fluid mt--2">
      <template v-if="this.reportData">
        <div class="row mt-5">
          <div class="col-xl-12 mb-5 mb-xl-0">
            <report
              v-bind:id="this.id"
              v-bind:data="this.reportData.history"
            ></report>
          </div>
        </div>

        <!--Tables-->
        <div class="row mt-5">
          <div class="col-xl-12 mb-5 mb-xl-0">
            <reports-table v-bind:id="this.id"></reports-table>
          </div>
        </div>
      </template>
    </div>
  </div>
</template>

<script>
// Charts
import * as chartConfigs from "../components/Charts/config";
import LineChart from "../components/Charts/LineChart";
import BarChart from "../components/Charts/BarChart";

// Tables
import ReportsTable from "./Dashboard/ReportsTable";
import Report from "./Dashboard/Report";
import { mapGetters } from "vuex";
export default {
  components: {
    LineChart,
    BarChart,
    ReportsTable,
    Report,
  },
  name: "patient",
  props: ["id"],
  created() {
    console.log(this);
  },
  computed: {
    reportData() {
      const report = this.$store.getters.getReportById(Number(this.id));
      if (report) {
        return report;
      }
      return {};
    },
    patientData() {
      return this.$store.getters.getPatientById(Number(this.id));
    },
    ownNotifications() {
      return this.$store.getters.ownNotifications;
    },
    // Pasted for #167
    ...mapGetters(["getSmileResult"]),
    smileResult() {
      return this.getSmileResult(Number(this.id)) ?? {};
    },
    dengueFormData() {
      return {
        ...this.infos,
        ...this.symptoms,
        ...this.lab_results,
        ...this.final_diagnosis,
      };
    },
    dengue_probability() {
      let probability = this.smileResult.dengue_probability;

      probability = probability ?? "Not enough data";

      if (!(typeof probability == "string")) {
        probability = parseFloat(probability).toFixed(4) * 100 + "%";
      }

      return probability;
    },
    dengue_status() {
      return this.confirmedDengue
        ? "Confirmed"
        : this.suspectedDengue
        ? "Suspected"
        : "Negative";
    },
    dhf_probability() {
      let probability = this.dhf_prob;
      console.log(probability)

      probability = probability ?? "Not enough data";

      if (!(typeof probability == "string")) {
        probability = parseFloat(probability).toFixed(4) * 100 + "%";
      }

      return probability;
    },
  },
  data() {
    return {
      editModal: false,
      charts1: true,
      loaded: false,
      dhf_prob:0,
      status: "",
      redBarChart: {
        activeIndex: 0,
        chartData: {
          datasets: [
            {
              label: "",
              data: [],
            },
          ],
        },
        extraOptions: chartConfigs.barChartOptions,
      },
      balanceChart: {
        activeIndex: 0,
        chartData: {
          datasets: [
            {
              label: "",
              data: [],
            },
          ],
        },
        extraOptions: chartConfigs.barChartOptions,
      },
      feverChart: {
        loaded: false,
        activeIndex: 0,
        chartData: {},
      },
      respChart: {
        loaded: false,
        activeIndex: 0,
        chartData: {},
        // extraOptions: chartConfigs.chartOptions,
      },
    };
  },

  // TODO watch? sortedHistory. It gets created in 9 different functions. make it a member of this class.
  methods: {
    logPatientData() {
      console.log(this.dengue_probability);
    },
    exportCSV() {
      const name =
        this.patientData.first_name + "_" + this.patientData.last_name;
      const download = function (data) {
        const blob = new Blob([data], { type: "text/csv" });
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement("a");
        a.setAttribute("hidden", "");
        a.setAttribute("href", url);
        a.setAttribute("download", `${name}.csv`);
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
      };
      const objectToCSV = function (jsonData) {
        const csvRows = [];

        // get headers
        const headers = Object.keys(jsonData[0]);
        csvRows.push(headers.join(","));
        //Loop through them
        for (const row of jsonData) {
          const values = headers.map((header) => {
            const escaped = ("" + row[header]).replace(/"/g, '\\"');
            return `"${escaped}"`;
          });
          csvRows.push(values.join(","));
        }
        return csvRows.join("\n");
      };

      const csvData = objectToCSV(this.reportData.history);
      download(csvData);
    },
    calcTimedelta(historyObj) {
      var timedelta =
        new Date(historyObj.datetime) -
        new Date(this.patientData.admission_date);
      return (
        "Day " + (Math.round(Math.abs(timedelta / (1000 * 3600 * 24))) + 1)
      );
    },
    dismissPatient(patient) {
      const id = patient.id;
      this.$store.dispatch("dismissPatient", { id });
    },

    //the dhf API need specific parameters to work.
    //currently we use as a placeholder only 4 parameters that we send to the backend.
    // d03_temp_avg
    // number
    // (query)

    // d03_temp_range
    // number
    // (query)

    // d03_pulse_rate_avg
    // integer
    // (query)

    // d03_pulse_rate_range
    // integer
    // (query)
    dhfPrediction() {
      // var feverArray = [];
      // var pulseArray = [];
      // var dayArray = [];
      // var fever = null;
      // var pulse = null;
      // var day = null;
      if (this.reportData != null) {
        //Test without any reports:
        //TODO request to DHF Api with correct parameters here
        //  var xhr = new XMLHttpRequest();
        //       //TODO correct URL in deployment. e.g. social.dengue.informatik..
        //       var url = "http://0.0.0.0:5001/dhf/demo/1";
        //       var params = 'd03_temp_avg=37&d03_pulse_rate_avg=90';
        //       xhr.open("POST", url, true);
        //       xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");

        //       xhr.onreadystatechange = function () {
        //           if (xhr.readyState === 4 && xhr.status === 200) {
        //               this.dhf_probability = xhr.responseText;
        //           }
        //       }.bind(this);
        //       xhr.send(params);

        if (this.reportData.history) {
          var sortedHistory = [].slice
            .call(this.reportData.history)
            .sort(function (a, b) {
              return new Date(a.datetime) - new Date(b.datetime);
            });
          var d03tempAvg = null;
          var d03pulseAvg = null;
          for (var i = 0; i < sortedHistory.length; i++) {
            // fever = sortedHistory[i].fever;
            // pulse = sortedHistory[i].pulse;
            // day = sortedHistory[i].daytime;

            // feverArray.push(parseFloat(fever));
            // pulseArray.push(parseFloat(pulse));
            // dayArray.push(day);
            // console.log(fever);
            // console.log(pulse);
            // console.log(day);

            if (i == 2) {
              d03tempAvg = sortedHistory[2].fever;
              d03pulseAvg = sortedHistory[2].pulse;
            }
          }

          this.loaded = true;
          // calculate from reports of day 3
          if (d03tempAvg != null && d03pulseAvg != null) {
            console.log("fever day 3: " + d03tempAvg);
            console.log("pulse day 3: " + d03pulseAvg);
            var xhr = new XMLHttpRequest();
            const url =
        process.env.NODE_ENV === "production"
          ? "https://social.informatik.uni-bremen.de/dhf-api/dhf/demo/1"
          : "http://0.0.0.0:5001/dhf/demo/1";

            // URL in deployment. e.g. social.dengue.informatik..
            // var url =
            //   "https://social.informatik.uni-bremen.de/dhf-api/dhf/demo/1";
            // var url =
            //   "http://0.0.0.0:5001/dhf/demo/1";
            var params =
              "d03_temp_avg=" +
              d03tempAvg +
              "&d03_pulse_rate_avg=" +
              d03pulseAvg;
            xhr.open("POST", url, true);
            xhr.setRequestHeader(
              "Content-Type",
              "application/x-www-form-urlencoded"
            );

            xhr.onreadystatechange = function () {
              if (xhr.readyState === 4 && xhr.status === 200) {
                this.dhf_prob = Math.round(xhr.responseText * 100) + "%";
                if (xhr.responseText * 100 >= 60) {
                  this.status = "critical";
                }
              }
            }.bind(this);
            xhr.send(params);
          }
        } else {
          console.log("no report history yet. create more reports.");
        }
      }
      // this.feverChart.chartData = {
      //   labels: columnArray,
      //   datasets: [
      //     {
      //       label: "Fever",
      //       data: feverArray,
      //     },
      //     {
      //       label: "Pulse",
      //       data: pulseArray,
      //       borderColor: "#fb6340",
      //       backgroundColor: "#fb6340",
      //       fill: false,
      //     },
      //   ],
      // };
    },

    weekFeverChart() {
      var feverArray = [];
      var pulseArray = [];
      var columnArray = [];
      var sameDays = null;

      if (this.reportData != null) {
        if (this.reportData.history) {
          var sortedHistory = [].slice
            .call(this.reportData.history)
            .sort((a, b) => new Date(a.datetime) - new Date(b.datetime));

          for (var i = 0; i < sortedHistory.length; i++) {
            if (
              columnArray.indexOf(this.calcTimedelta(sortedHistory[i])) === -1
            ) {
              columnArray.push(this.calcTimedelta(sortedHistory[i]));
              sameDays = sortedHistory.filter(
                (el) =>
                  new Date(el.datetime).getDate() ===
                  new Date(sortedHistory[i].datetime).getDate()
              );

              var tmpFeverArray = [];
              var tmpPulseArray = [];

              for (var x in sameDays) {
                tmpFeverArray.push(parseFloat(sameDays[x].fever));
                tmpPulseArray.push(parseInt(sameDays[x].pulse));
              }
              feverArray.push(Math.max(...tmpFeverArray));
              pulseArray.push(Math.max(...tmpPulseArray));
            }
            this.loaded = true;
          }
        }
      }

      this.feverChart.chartData = {
        labels: columnArray,
        datasets: [
          {
            label: "Fever",
            data: feverArray,
          },
          {
            label: "Pulse",
            data: pulseArray,
            borderColor: "#fb6340",
            backgroundColor: "#fb6340",
            fill: false,
          },
        ],
      };
    },
    dayFeverChart() {
      var feverArray = [];
      var pulseArray = [];
      var columnArray = [];
      var fever = null;
      var pulse = null;
      var column = null;

      if (this.reportData != null) {
        if (this.reportData.history) {
          var sortedHistory = [].slice
            .call(this.reportData.history)
            .sort(function (a, b) {
              return new Date(a.datetime) - new Date(b.datetime);
            });

          for (var i = 0; i < sortedHistory.length; i++) {
            if (
              new Date(sortedHistory[i].datetime).getDate() ===
              new Date().getDate()
            ) {
              fever = sortedHistory[i].fever;
              pulse = sortedHistory[i].pulse;
              column = sortedHistory[i].daytime;

              feverArray.push(parseFloat(fever));
              pulseArray.push(parseFloat(pulse));
              columnArray.push(column);
            }
            this.loaded = true;
          }
        }
      }
      this.feverChart.chartData = {
        labels: columnArray,
        datasets: [
          {
            label: "Fever",
            data: feverArray,
          },
          {
            label: "Pulse",
            data: pulseArray,
            borderColor: "#fb6340",
            backgroundColor: "#fb6340",
            fill: false,
          },
        ],
      };
    },
    dayFluidChart() {
      var fluidInputArray = [];
      var fluidOutputArray = [];
      var columnArray = [];

      var fluidInput = null;
      var fluidOutput = null;
      var column = null;

      if (this.reportData != null) {
        if (this.reportData.history) {
          var sortedHistory = [].slice
            .call(this.reportData.history)
            .sort(function (a, b) {
              return new Date(a.datetime) - new Date(b.datetime);
            });

          for (var i = 0; i < sortedHistory.length; i++) {
            if (
              new Date(sortedHistory[i].datetime).getDate() ===
              new Date().getDate()
            ) {
              fluidInput = sortedHistory[i].fi_total;
              fluidOutput = sortedHistory[i].fo_total;
              column = sortedHistory[i].daytime;
              fluidInputArray.push(parseFloat(fluidInput));
              fluidOutputArray.push(parseFloat(fluidOutput));
              columnArray.push(column);
            }
            this.loaded = true;
          }
        }
      }
      this.redBarChart.chartData = {
        labels: columnArray,
        datasets: [
          {
            label: "Input",
            data: fluidInputArray,
            borderColor: "#2dce89",
            backgroundColor: "#2dce89",
          },
          {
            label: "Output",
            data: fluidOutputArray,
            borderColor: "#5e72e4",
            backgroundColor: "#5e72e4",
          },
        ],
      };
    },
    weekFluidChart() {
      var columnArray = [];
      var fluidInputArray = [];
      var fluidOutputArray = [];
      var sameDays = null;

      var sortedHistory = [].slice
        .call(this.reportData.history)
        .sort(function (a, b) {
          return new Date(a.datetime) - new Date(b.datetime);
        });

      console.log("sortedHistory");
      console.log(sortedHistory);

      if (this.reportData != null) {
        if (this.reportData.history) {
          for (var i = 0; i < sortedHistory.length; i++) {
            if (
              columnArray.indexOf(this.calcTimedelta(sortedHistory[i])) === -1
            ) {
              columnArray.push(this.calcTimedelta(sortedHistory[i]));
              sameDays = sortedHistory.filter(
                (el) =>
                  new Date(el.datetime).getDate() ===
                  new Date(sortedHistory[i].datetime).getDate()
              );

              var tmpInputArray = [];
              var tmpOutputArray = [];

              for (var x in sameDays) {
                tmpInputArray.push(parseFloat(sameDays[x].fi_total));
                tmpOutputArray.push(parseInt(sameDays[x].fo_total));
              }
              fluidInputArray.push(tmpInputArray.reduce((a, b) => a + b));
              fluidOutputArray.push(tmpOutputArray.reduce((a, b) => a + b));
            }
            this.loaded = true;
          }
        }
      }
      this.redBarChart.chartData = {
        labels: columnArray,
        datasets: [
          {
            label: "Input",
            data: fluidInputArray,
            borderColor: "#2dce89",
            backgroundColor: "#2dce89",
          },
          {
            label: "Output",
            data: fluidOutputArray,
            borderColor: "#5e72e4",
            backgroundColor: "#5e72e4",
          },
        ],
      };
    },
    checkStatus() {
      if (this.reportData && this.reportData.history) {
        var sortedHistory = [].slice
          .call(this.reportData.history)
          .sort(function (a, b) {
            return new Date(a.datetime) - new Date(b.datetime);
          });
        if (sortedHistory.length > 0) {
          this.status = sortedHistory[sortedHistory.length - 1].status;
        }
      }
    },
    dayRespChart() {
      var respArray = [];
      var diaArray = [];
      var sysArray = [];
      var columnArray = [];
      var respiration = null;
      var systolic = null;
      var diastolic = null;
      var column = null;
      if (this.reportData != null) {
        if (this.reportData.history) {
          var sortedHistory = [].slice
            .call(this.reportData.history)
            .sort(function (a, b) {
              return new Date(a.datetime) - new Date(b.datetime);
            });

          for (var i = 0; i < sortedHistory.length; i++) {
            if (
              new Date(sortedHistory[i].datetime).getDate() ===
              new Date().getDate()
            ) {
              respiration = sortedHistory[i].respiration;
              diastolic = sortedHistory[i].bp_dia;
              systolic = sortedHistory[i].bp_sys;
              column = sortedHistory[i].daytime;

              respArray.push(parseInt(respiration));
              diaArray.push(parseFloat(diastolic));
              sysArray.push(parseFloat(systolic));
              columnArray.push(column);
            }
            this.loaded = true;
          }
        }
      }
      this.respChart.chartData = {
        labels: columnArray,
        datasets: [
          {
            label: "Respirations",
            data: respArray,
          },
          {
            label: "Systolic",
            data: sysArray,
            borderColor: "#fb6340",
            backgroundColor: "#fb6340",
            fill: false,
          },
          {
            label: "Diastolic",
            data: diaArray,
            borderColor: "#f3a4b5",
            backgroundColor: "#f3a4b5",
            fill: false,
          },
        ],
      };
    },
    weekRespChart() {
      var respArray = [];
      var diaArray = [];
      var sysArray = [];
      var columnArray = [];
      var sameDays = null;

      if (this.reportData != null) {
        if (this.reportData.history) {
          var sortedHistory = [].slice
            .call(this.reportData.history)
            .sort(function (a, b) {
              return new Date(a.datetime) - new Date(b.datetime);
            });

          for (var i = 0; i < sortedHistory.length; i++) {
            if (
              columnArray.indexOf(this.calcTimedelta(sortedHistory[i])) === -1
            ) {
              columnArray.push(this.calcTimedelta(sortedHistory[i]));
              sameDays = sortedHistory.filter(
                (el) =>
                  new Date(el.datetime).getDate() ===
                  new Date(sortedHistory[i].datetime).getDate()
              );

              var tmpRespArray = [];
              var tmpDiaArray = [];
              var tmpSysArray = [];

              for (var x in sameDays) {
                tmpRespArray.push(parseFloat(sameDays[x].respiration));
                tmpDiaArray.push(parseInt(sameDays[x].bp_dia));
                tmpSysArray.push(parseInt(sameDays[x].bp_sys));
              }
              respArray.push(Math.max(...tmpRespArray));
              diaArray.push(Math.max(...tmpDiaArray));
              sysArray.push(Math.max(...tmpSysArray));
            }
            this.loaded = true;
          }
        }
      }

      this.respChart.chartData = {
        labels: columnArray,
        datasets: [
          {
            label: "Respirations",
            data: respArray,
          },
          {
            label: "Systolic",
            data: sysArray,
            borderColor: "#fb6340",
            backgroundColor: "#fb6340",
            fill: false,
          },
          {
            label: "Diastolic",
            data: diaArray,
            borderColor: "#f3a4b5",
            backgroundColor: "#f3a4b5",
            fill: false,
          },
        ],
      };
    },
    dayBalanceChart() {
      var balanceArray = [];
      var columnArray = [];

      var fluidInput = null;
      var fluidOutput = null;
      var column = null;

      if (this.reportData != null) {
        if (this.reportData.history) {
          var sortedHistory = [].slice
            .call(this.reportData.history)
            .sort(function (a, b) {
              return new Date(a.datetime) - new Date(b.datetime);
            });

          for (var i = 0; i < sortedHistory.length; i++) {
            if (
              new Date(sortedHistory[i].datetime).getDate() ===
              new Date().getDate()
            ) {
              fluidInput = sortedHistory[i].fi_total;
              fluidOutput = sortedHistory[i].fo_total;
              column = sortedHistory[i].daytime;
              balanceArray.push(
                parseFloat(fluidInput) - parseFloat(fluidOutput)
              );
              columnArray.push(column);
            }
            this.loaded = true;
          }
        }
      }

      this.balanceChart.chartData = {
        labels: columnArray,
        datasets: [
          {
            label: "Balance",
            data: balanceArray,
            borderColor: "#2dce89",
            backgroundColor: "#2dce89",
          },
        ],
      };
    },
    weekBalanceChart() {
      var columnArray = [];
      var balanceArray = [];
      var sameDays = null;

      if (this.reportData != null) {
        if (this.reportData.history) {
          var sortedHistory = [].slice
            .call(this.reportData.history)
            .sort(function (a, b) {
              return new Date(a.datetime) - new Date(b.datetime);
            });

          for (var i = 0; i < sortedHistory.length; i++) {
            if (
              columnArray.indexOf(this.calcTimedelta(sortedHistory[i])) === -1
            ) {
              columnArray.push(this.calcTimedelta(sortedHistory[i]));
              sameDays = sortedHistory.filter(
                (el) =>
                  new Date(el.datetime).getDate() ===
                  new Date(sortedHistory[i].datetime).getDate()
              );

              var tmpInputArray = [];
              var tmpOutputArray = [];
              var tmpBalanceArray = [];

              for (var x in sameDays) {
                tmpInputArray.push(parseFloat(sameDays[x].fi_total));
                tmpOutputArray.push(parseInt(sameDays[x].fo_total));
                tmpBalanceArray.push(
                  parseFloat(sameDays[x].fi_total) -
                    parseInt(sameDays[x].fo_total)
                );
              }
              balanceArray.push(tmpBalanceArray.reduce((a, b) => a + b));
            }

            this.loaded = true;
          }
        }
      }

      this.balanceChart.chartData = {
        labels: columnArray,
        datasets: [
          {
            label: "Balance",
            data: balanceArray.reverse(),
            borderColor: "#2dce89",
            backgroundColor: "#2dce89",
          },
        ],
      };
    },
    initBigChart(index) {
      this.feverChart.activeIndex = index;
      if (index === 0) {
        this.dayFeverChart();
      } else if (index === 1) {
        this.weekFeverChart();
      }
    },
    initBarChart(index) {
      this.redBarChart.activeIndex = index;
      if (index === 0) {
        this.dayFluidChart();
      } else if (index === 1) {
        this.weekFluidChart();
      }
    },
    initRespChart(index) {
      this.respChart.activeIndex = index;
      if (index === 0) {
        this.dayRespChart();
      } else if (index === 1) {
        this.weekRespChart();
      }
    },
    initBalanceChart(index) {
      this.balanceChart.activeIndex = index;
      if (index === 0) {
        this.dayBalanceChart();
      } else if (index === 1) {
        this.weekBalanceChart();
      }
    },
  },
  watch: {
    reportData() {
      this.checkStatus();
      this.initBigChart(0);
      this.initBarChart(0);
      this.initRespChart(0);
      this.initBalanceChart(0);
      this.dhfPrediction();
    },
  },
  async mounted() {
    this.checkStatus();
    this.initBigChart(0);
    this.initBarChart(0);
    this.initRespChart(0);
    this.initBalanceChart(0);
    this.dhfPrediction();
  },
};
</script>

<style scoped>
.divider {
  height: 1.5rem !important;
}

.singlePatient {
  min-height: 100vh !important;
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

.dhf {
  background: #ffdab9;
}

.modal {
  z-index: 700 !important;
}
</style>
