import dcrf from "dcrf-client";

const state = {
  connected: false,
  error: "",
  client: null,
  subClient: null,
  ownNotifications: [],
  is_online: false
};

const mutations = {
  NEW_NOTIFICATION(state, payload) {
    console.debug("index.js payload");
    console.debug(payload);
    state.ownNotifications = payload;
  },
  CONNECTED(state, payload) {
    state.is_online = payload;
  },
  CLOSE_SOCKET(state, payload) {
    state.client = payload;
  },
  SET_CLIENT(state, payload) {
    state.client = payload;
  }
};

const actions = {
  setup(context) {
    console.debug('[index.js] (setup)', {state});
    if (!state.is_online) {
      const client = dcrf.connect(
        process.env.NODE_ENV === "production"
          ? process.env.VUE_APP_WS
          : "ws://localhost:8000/ws/"
      );
      client.transport.socket.onopen = 
        () => context.commit("CONNECTED", true);
      context.commit("SET_CLIENT", client);
      context.dispatch("subscriptions");
      client.list('patients');
      client.list('reports');
      client.list('dengue');
      context.dispatch("loadWards");
    }
  },

  closeSocket(context) {
    state.client.transport.socket.onclose = function() {};
    state.client.transport.socket.close();
    context.commit("CLOSE_SOCKET", state.client.transport.socket.close());
    context.commit("CONNECTED", false);
  },

  subscriptions(context) {
    console.debug('[index.js] (subscriptions)');
    state.client.transport.socket.onmessage = function(e) {
      const message = JSON.parse(e.data);
      console.debug('message', {e, message, stream: message.stream, type: message.payload.type, action: message.payload.action});

      const stream = StreamFactory.create(context, message);
      stream?.invokeStreamActions();
    };

    state.client.transport.socket.onerror = function() {
      if (!state.is_online) {
        context.commit("NEW_NOTIFICATION", [
          {
            "No connection to the server":
              "Please refresh the page or try again later"
          }
        ]);
        context.commit("CONNECTED", false);
      }
    };
  },

  newNotification(context, errors) {
    context.commit('NEW_NOTIFICATION', errors, {root: true})
  },
};

const getters = {
  connected: state => state.connected,
  error: state => state.error,
  client: state => state.client,
  ownNotifications: state => state.ownNotifications
};

const socketModule = {
  state,
  mutations,
  actions,
  getters
};

class StreamFactory{
  static create(context, message){
    switch (message.stream) {
      case 'patients':
        return new PatientStream(context, message);
      case 'history':
        return new HistoryStream(context, message);
      case 'reports':
        return new ReportStream(context, message);
      default:
        console.debug('Unknown stream', {context, message});
        break;
    }
  }
}

function StreamActions(message, onList, onCreate, onDelete, onPatch, onUpdate){
  switch (message?.payload?.action) {
    case 'list':
      onList(message.payload);
      break;
    case 'create':
      onCreate(message.payload);
      break;
    case 'delete':
      onDelete(message.payload);
      break;
    case 'patch':
      onPatch(message.payload);
      break;
    case 'update':
      onUpdate(message.payload);
      break;
    default:
      console.debug('(StreamActions) unkown message?.payload?.action', {message});
      break;
  }
}

class Stream {
  constructor(context, message){
    this.context = context;
    this.message = message;
  }
}

class PatientStream extends Stream{
  get patientData(){
    return this.context.getters.patientData;
  }
  
  invokeStreamActions(){
    const x = !!this.message?.payload?.type;
    StreamActions(
      this.message,
      (payload) => this.context.commit("UPDATE_PATIENT_DATA", payload.data),
      (payload) => x ? this.context.commit("UPDATE_PATIENT_DATA", [...this.context.getters.patientData, payload]) : ()=>{},
      () => this.context.rootState.socket.client.list('patients'),
      (payload) => this.context.commit("UPDATE_PATIENT", payload.data),
      (payload) => this.context.commit("UPDATE_PATIENT", payload),
    )
    this.context.dispatch("loadPatientsWithoutDiagnosis");
  }
}

class HistoryStream extends Stream {
  invokeStreamActions(){
    const type = this.message?.payload?.type;
    if(type){
      switch (type) {
        case 'notifications':
          this.onNotifications();
          break;
        case 'history.change':
          console.debug('[index.js] history.change', {history_stream: this});
          break;
        default:
          console.debug('[index.js] history type unkown', {type});
          break;
      }
    }
    StreamActions(
      this.message,
      (payload) => console.debug('[index.js] history list', {payload}),
      //TODO currently there is a bug, where only create history is send to all clients, not create report
      // (payload) => this.context.commit('CREATE_HISTORY', payload),
      (payload) => this.context.dispatch('loadReports', payload),
      (payload) => this.context.commit('DELETE_HISTORY', payload),
      (payload) => this.context.commit('UPDATE_HISTORY', payload.data),
      (payload) => this.context.commit('UPDATE_HISTORY', payload),
    )
  }

  onNotifications(){
    // distinguish between monitoring interval and fever notifications
    if (this.context.rootState.auth.show_notifications) {
      if (this.message.payload.data.type === "interval") {
        this.context.commit("NEW_NOTIFICATION", [
          {
            "Please visit the following patient:": this.context.getters.patientNameById(
              this.message.payload.data.patient
            )
          }
        ]);
      }
      if (this.message.payload.data.type === "fever") {
        this.context.commit("NEW_NOTIFICATION", [
          {
            "The following patient might enter a critical phase:": this.context.getters.patientNameById(
              this.message.payload.data.patient
            )
          }
        ]);
      }
    }
  }
}

class ReportStream extends Stream{
  invokeStreamActions(){
    StreamActions(
      this.message,
      (payload) => this.context.commit('UPDATE_REPORT_DATA', payload.data),
      (payload) => this.context.commit("UPDATE_REPORT_DATA", [...this.context.getters.reportData, payload.data]),
      (payload) => console.debug('[index.js] reports delete', {payload}),
      (payload) => console.debug('[index.js] reports patch', {payload}),
      (payload) => console.debug('[index.js] reports update', {payload}),
    )
  }
}

export default socketModule;
