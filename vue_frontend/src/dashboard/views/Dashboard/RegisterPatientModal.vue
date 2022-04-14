<template>
  <modal @close="close()" :show.sync="patientModal">
            <template slot="header">
              <div v-if="newPatient">
                <h2 class="modal-title">Patient registration</h2>
              </div>
              <div v-else>
                <h2 class="modal-title">Edit Patient</h2>
              </div>

            </template>
            <div class="row align-items-center text-left">
              <div class="card col-md-12 mt-3">
                <div class="card-body">
                  <div class="row align-items-center">
                    <base-input
                        label="First Name"
                        v-model="first_name"
                        class="col-md-6"
                        required
                    >
                    </base-input>
                    <base-input
                        label="Last Name"
                        v-model="last_name"
                        class="col-md-6"
                        required
                    ></base-input>
                    <div class="col-md-6">
                        <label class="form-control-label">Hospital Number *</label>
                        <base-input
                            :placeholder="'12345/67'"
                            v-model="hospital_number"
                            required
                        >
                            <template v-slot:addonLeft>HN</template>
                        </base-input>
                    </div>
                    <div class="col-md-6"></div>
                    <base-input
                        label="Age"
                        v-model="age"
                        class="col-md-6"
                    ></base-input>
                    <base-dropdown label="Gender" class="col-md-6">
                      <template v-slot:title>
                        <base-button type="secondary" class="dropdown-toggle">
                          <span d-if="!gender.length"> 
                            {{gender}}
                          </span>
                        </base-button>
                      </template>
                          <a class="dropdown-item" @click="gender = 'Male'">Male</a>
                          <a class="dropdown-item" @click="gender = 'Female'">Female</a>
                          <a class="dropdown-item" @click="gender = 'Other'">Other</a>
                      </base-dropdown>
                    </div>
                </div>
              </div>
            </div>
            <template slot="footer">
            <div class="mr-auto">Fields marked with an <strong>*</strong> are required</div>
              <base-button type="secondary" @click="close()">
                Close
              </base-button>
                <base-button :disabled="formIsInvalid" type="primary" @click="newPatient ? registerPatient() : editPatient()">
                    {{newPatient ? 'Register patient' : 'Save changes'}}
                </base-button>
            </template>
          </modal>
</template>

<script>
export default {
    props: ['input'],
    created(){
        if(this.hospital_number?.startsWith('HN')){
            this.hospital_number = this.hospital_number.substr(2);
        }
    },
    data() {
        return {
            patientModal: true,
            newPatient: null,
            first_name: null,
            last_name: null,
            hospital_number: null,
            age: null,
            gender: null,
            ...this.input, 
        }
    },
    computed: {
        formIsValid(){
            let valid = true;
            if(!this.first_name){
                valid = false;
            }
            if(!this.last_name){
                valid = false;
            }
            if(!this.hospitalNumberIsValid){
                valid = false;
            }
            return valid;
        },
        formIsInvalid() {
            return !this.formIsValid;
        },
        hospitalNumberWithPrefixHN(){
            return 'HN' + this.hospital_number;
        },
        hospitalNumberIsValid(){
            if(this.hospital_number){
                const regex = /[H][N]\S{5}[/]\d{2}/g;
                const found = this.hospitalNumberWithPrefixHN?.match(regex);
                return this.hospital_number && found && this.hospitalNumberWithPrefixHN === found[0];
            } else {
                return false;
            }
        },
    },
    methods:{
        close(){
            this.$emit('close')
        },
        
        registerPatient() {
            const patient = {
                first_name: this.first_name,
                last_name: this.last_name,
                hospital_number: this.hospitalNumberWithPrefixHN,
                age: this.age,
                gender: this.gender,
            }

            this.$store.dispatch("addPatient", patient);
            this.close();
        },
        editPatient() {
            console.debug('editPatient');
            const patient = {
                first_name: this.first_name,
                last_name: this.last_name,
                gender: this.gender,
                age: this.age,
            }
            const id = this.id;

            this.$store.dispatch("editPatient", {id, patient});
            this.close();
        },
    }    
}
</script>

<style>

</style>