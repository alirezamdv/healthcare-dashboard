const state = {
    patientData: [],
    patientsHavingNoDiagnosis: [],
};

const mutations = {
    UPDATE_PATIENT_DATA(state, payload) {
        console.debug('(UPDATE_PATIENT_DATA)', {payload, state});
        state.patientData = payload;
    },

    UPDATE_PATIENTS_HAVING_NO_DIAGNOSIS_DATA(state, payload) {
        console.debug('(UPDATE_PATIENTS_HAVING_NO_DIAGNOSIS_DATA)', {payload, state});
        state.patientsHavingNoDiagnosis = payload;
    },

    UPDATE_PATIENT(state, payload) {
        console.debug('(UPDATE_PATIENT)', {payload, state});
        for (var i = 0; i < state.patientData.length; i++) {
            if (state.patientData[i].id === payload.id) {
                state.patientData.splice(i, 1, payload);
            }
        }
    },
};

const actions = {
    // loads all available patient data
    async loadPatients(context) {
        console.debug('(loadPatients)', {context});
        try {
            const client = context.rootState.socket.client;
            const patients = client.list('patients');
            context.commit("UPDATE_PATIENT_DATA", patients);
        } catch (error) {
            context.commit('NEW_NOTIFICATION', error.errors, {root: true});
        }
    },

    async loadPatientsWithoutDiagnosis(context) {
        console.debug('(loadPatientsWithoutDiagnosis)', {context});
        try {
            const patients = context.state.patientData;
            const patientsHavingNoDiagnosis = await getPatientsHavingNoDiagnosis(patients);
            context.commit("UPDATE_PATIENTS_HAVING_NO_DIAGNOSIS_DATA", patientsHavingNoDiagnosis);
        } catch (error) {
            console.debug('[patients.js] (loadPatientsWithoutDiagnosis) error', {error});
            context.commit('NEW_NOTIFICATION', error.errors, {root: true});
        }
    },

    async addPatient(context, payload) {
        const client = context.rootState.socket.client;
        try {
            await client.create("patients", payload);
        } catch (error) {
            console.debug('[patients.js] (addPatient) error', {error});
            context.commit('NEW_NOTIFICATION', error.errors, {root: true});
        }
    },

    async deletePatient(context, payload) {
        const client = context.rootState.socket.client;
        try {
            await client.delete("patients", payload);
        } catch (error) {
            console.debug('[patients.js] (deletePatient) error', {error});
            context.commit('NEW_NOTIFICATION', error.errors, {root: true});
        }
    },

    async editPatient(context, payload) {
        console.debug('[patients.js] (editPatient)', {context, payload});
        try {
            const client = context.rootState.socket.client;
            await client.patch("patients", payload.id, payload.patient);
        } catch (error) {
            console.debug('[patients.js] (editPatient) error', {error});
            context.commit('NEW_NOTIFICATION', error.errors, {root: true});
        }
    },

    async dismissPatient(context, payload){
        //payload = {id}
        try {
            await _dismissPatient(context, payload);
          } catch (error) {
            console.debug('[patient.js] (dismissPatient) error', {error});
            context.commit('NEW_NOTIFICATION', error.errors, {root: true});
          }
    },

    async requiresHospitalization(context, payload) {
        //payload = {id}
        try {
          await _requiresHospitalization(context, payload);
        } catch (error) {
          console.debug('[patient.js] (requiresHospitalization) error', {error});
          console.debug(error);
          context.commit('NEW_NOTIFICATION', error.errors, {root: true});
        }
    },
};

async function getPatientsHavingNoDiagnosis(patients){
    const diagnosisNeeded = []

    // for (const patient of patients) {
    //     const token = localStorage.getItem("token");

    //     const headers = new Headers();
    //     headers.append("Authorization", "Token " + token);
    //     headers.append("Content-Type", "application/json");

    //     const url = process.env.NODE_ENV === 'production'
    //     ? 'https://social.informatik.uni-bremen.de/api/diagnosis/'
    //     : 'http://localhost:8000/api/diagnosis/';
    //     //TODO this triggers a new login. The user should already be logged in
    //     // we are using the token but it does not seem to work.
    //     // maybe we should use axios, like in index.js
    //     const response = await fetch(url + "?patient=" + patient.id, {headers});
    //     const responseText = await response.text();
    //     // TODO: if a patient has no diagnosis, why is this <= 5?
    //     if (responseText.length <= 5){ 
    //         diagnosisNeeded.push(patient);
    //     }
    // }
    for (const patient of patients) {
        console.log(patient);
        if (patient.admission_date == null && patient.dismissal_date == null){ 
            diagnosisNeeded.push(patient);
            console.log(diagnosisNeeded);
        }
    }
    return diagnosisNeeded;
}

async function _dismissPatient(context, payload){
    const client = await context.rootState.socket.client;
    const dismissal_date = (new Date()).toISOString();
    await client.patch("patients", payload.id, {dismissal_date});
}

async function _requiresHospitalization(context, payload){
    const client = await context.rootState.socket.client;
    const admission_date = (new Date()).toISOString();
    await client.patch("patients", payload.id, {admission_date});
}

const getters = {
    patientData: (state) => state.patientData,
    patientsHavingNoDiagnosis: (state) => state.patientsHavingNoDiagnosis,
    getPatientById: (state) => (id) =>
        state.patientData.find((patient) => patient.id === id),
    patientNameById: (state) => (id) => {
        let patient = state.patientData.find((patient) => patient.id === id)
        return patient.first_name + " " + patient.last_name;
    }
};

const patientModule = {
    state,
    mutations,
    actions,
    getters,
};

export default patientModule;
