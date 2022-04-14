const state = {
    reportData: [],
    criticalReports: [],
};

const mutations = {
    UPDATE_REPORT_DATA(state, payload) {
        console.debug('(UPDATE_REPORT_DATA)', {payload, state});
        state.reportData = payload;
    },
    UPDATE_CRITICAL_REPORT_DATA(state, payload) {
        console.debug('(UPDATE_CRITICAL_REPORT_DATA)', {payload, state});
        state.criticalReports = payload;
    },
    UPDATE_HISTORY(state, payload) {
        console.debug('(UPDATE_HISTORY)', {payload, state});
        const report = state.reportData.find((report) => report.pk === payload.id);
        if (report){
            const historyIndex = report.history.findIndex((history) => history.history_id === payload.history_id);
            if (historyIndex >= 0){
                report.history.splice(historyIndex, 1, payload);
            } else {
                console.debug('(UPDATE_HISTORY) error, historyIndex not found', {payload, state});
            }
        } else {
            console.debug('(UPDATE_HISTORY) error, report not found', {payload, state});
        }
    },
    CREATE_HISTORY(state, payload) {
        console.debug('(CREATE_HISTORY)', {payload, state});
        const report = state.reportData.find((report) => report.pk === payload.id);
        if (report){
            console.debug('(report)', {report});
            report.history.push(payload);
        } else {
            console.debug('(CREATE_HISTORY) report not found', {payload, state});
            
        }
    },
    DELETE_HISTORY(state, payload) {
        console.debug('(DELETE_HISTORY)', {payload, state});
        const report = state.reportData.find((report) => report.pk === payload.id);
        const index = report.history.findIndex((history) => history.history_id === payload.history_id);
        report.history.splice(index, 1);
    },
};

// TODO addOrUpdateReport, let backend decide to create or add a report based on the data provided
const actions = {
    async loadReports(context) {
        try {
            console.debug('[report.js] (loadReports)');
            await _loadReports(context);
        } catch (error) {
            console.debug('[report.js] (loadReports) error', {error});
            context.commit('NEW_NOTIFICATION', error.errors, {root: true});
        }
    },

    async addReport(context, payload) {
        try {
            console.debug('[report.js] (addReport)', {payload});
            await _addReport(context, payload);
        } catch (error) {
            console.debug('[report.js] (addReport) error', {error});
            context.commit('NEW_NOTIFICATION', error.errors, {root: true});
        }
    },

    async createReport(context, payload) {
        try {
            console.debug('[report.js] (createReport)', {payload});
            await _createReport(context, payload);
        } catch (error) {
            console.debug('[report.js] (createReport) error', {error});
            context.commit('NEW_NOTIFICATION', error.errors, {root: true});
        }
    },

    async editReport(context, payload) {
        try {
            console.debug('[report.js] (editReport)', {payload});
            await _editReport(context, payload);
        } catch (error) {
            console.debug('[report.js] (editReport) error', {error});
            context.commit('NEW_NOTIFICATION', error.errors, {root: true});
        }
    },

    async deleteReport(context, payload) {
        try {
            console.debug('[report.js] (deleteReport)', {payload});
            await _deleteReport(context, payload);
        } catch (error) {
            console.debug('[report.js] (deleteReport) error', {error});
            context.commit('NEW_NOTIFICATION', error.errors, {root: true});
        }
    },

    formatJson(context, payload) {
        var formattedJson = {
            daytime: payload.report.daytime,
            day_of_fever: payload.report.day_of_fever,
            fever: payload.report.fever,
            pulse: payload.report.pulse,
            respiration: payload.report.respiration,
            bp_sys: payload.report.bp_sys,
            bp_dia: payload.report.bp_dia,
            diet: payload.report.diet,
            fi_oral: payload.report.fi_oral,
            fi_parenteral: payload.report.fi_parenteral,
            fi_other: payload.report.fi_other,
            fi_eight_hrs: payload.report.fi_eight_hrs,
            fi_total: payload.report.fi_total,
            fo_urine: payload.report.fo_urine,
            fo_uf: payload.report.fo_uf,
            fo_emesis: payload.report.fo_emesis,
            fo_drainage: payload.report.fo_drainage,
            fo_eight_hrs: payload.report.fo_eight_hrs,
            fo_total: payload.report.fo_total,
            pain_score: payload.report.pain_score,
            abd_cir: payload.report.abd_cir,
            stools: payload.report.stools,
            urine: payload.report.urine,
            weight_ht: payload.report.weightHt,
            weight: payload.report.weight,
            height: payload.report.height,
            o2sat: payload.report.o2sat,
            hematocrit: payload.report.hematocrit,
            platelet: payload.report.platelet,
            wbc: payload.report.wbc,
            additional: payload.report.additional,
            medical_advice: payload.report.medical_advice,
            warning_signs: payload.report.warning_signs,
            status: payload.report.status,
            datetime: payload.report.datetime,
            monitoring_interval: payload.report.monitoring_interval,
            patient_id: payload.report.patient,
            changed_by: context.rootGetters.user_id,
        };
        return formattedJson;
    },
};

async function _loadReports(context) {
    const client = await context.rootState.socket.client;
    const reports = await client.list("reports");
    context.commit("UPDATE_REPORT_DATA", reports);
}

async function _addReport(context, payload) {
    const formattedJson = await context.dispatch('formatJson', payload);
    const client = await context.rootState.socket.client;
    await client.patch("reports", payload.id, formattedJson);
}

async function _createReport(context, payload) {
    const formattedJson = await context.dispatch('formatJson', payload);
    const client = await context.rootState.socket.client;
    await client.create("reports", formattedJson);
}

async function _editReport(context, payload) {
    const formattedJson = await context.dispatch('formatJson', payload);
    const client = await context.rootState.socket.client;
    await client.patch("history", payload.id, formattedJson);
}

async function _deleteReport(context, payload) {
    const client = await context.rootState.socket.client;
    await client.delete("history", payload.id);
}

const getters = {
    reportData: (state) => state.reportData,
    getReportById: (state) => (id) =>
        state.reportData.find((report) => report.patient === id),
    criticalReports: (state, getters) => {
        var criticalArray = [];
        for (var i = 0; i < state.reportData.length; i++) {
            if (state.reportData[i].history.length > 0) {
                var history = state.reportData[i].history.reverse();
                var sortedHistory = [].slice.call(history).sort((a, b) => new Date(a.datetime) - new Date(b.datetime));

                if (sortedHistory[sortedHistory.length - 1].status === "critical" && (getters.getPatientById(state.reportData[i].history[0].patient).dismissal_date === null)) {
                    criticalArray.push(sortedHistory.pop());
                }
            }
        }
        return criticalArray;
    },
};

const reportModule = {
    state,
    mutations,
    actions,
    getters,
};

export default reportModule;
