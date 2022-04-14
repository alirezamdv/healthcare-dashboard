import Vue from "vue/dist/vue.js";
import Vuex from "vuex";
import createPersistedState from "vuex-persistedstate";

//import modules
import auth from "./modules/auth";
import dengue from "./modules/dengue/dengue.js";
import patients from "./modules/patients/patient.js";
import reports from "./modules/reports/reports.js";
import socket from "./modules/socket";
import user from "./modules/user/user.js";

Vue.use(Vuex);

let store = new Vuex.Store({
    modules: {
        auth,
        dengue,
        patients,
        reports,
        socket,
        user
    },
    // persist the state, excluding the socket (important!)
    plugins: [createPersistedState({
        paths: ['auth','patients', 'reports', 'dengue', 'user'],
        key: 'vuex',
        reducer: function (state) {
            //clear the state that is persisted in the local storage when the user is logged out
            if (state.auth.logged_in === false) {
                return {}
            }
            return {patients: state.patients, reports: state.reports, auth: state.auth, dengue: state.dengue, user: state.user}
        },
    })],
    //strict: process.env.NODE_ENV !== "production",
});

export default store;
