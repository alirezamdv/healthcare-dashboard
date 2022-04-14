const state = {
  dengueData: [],
  smileResult: {},
};

const mutations = {
  UPDATE_DENGUE_DATA(state, payload) {
    state.dengueData = payload;
  },
  UPDATE_SMILE_RESULT(state, payload) {
    state.smileResult = payload;
  },
};

const actions = {
  async loadDengue(context) {
    try {
        await _loadDengue(context);
      } catch (error) {
          console.debug('[dengue.js] (loadDengue) error');
          console.debug(error);
          context.commit('NEW_NOTIFICATION', error.errors, {root: true});
      }
  },

  async createDengue(context, payload) {
      try {
          await _createDengue(context, payload);
      } catch (error) {
          console.debug('[dengue.js] (createDengue) error');
          console.debug(error);
          context.commit('NEW_NOTIFICATION', error.errors, {root: true});
      }
  },

  async editDengue(context, payload) {
      try {
          await _editDengue(context, payload.id, payload.payload);
          await _loadDengue(context);
      } catch (error) {
          console.debug('[dengue.js] (editDengue) error');
          console.debug(error);
          context.commit('NEW_NOTIFICATION', error.errors, {root: true});
      }
  },

  async deleteDengue(context, payload) {
      try {
          await _deleteDengue(context, payload);
          await _loadDengue(context);
        } catch (error) {
          console.debug('[dengue.js] (deleteDengue) error');
          console.debug(error);
          context.commit('NEW_NOTIFICATION', error.errors, {root: true});
      }
  },

  async calculateDengueProbability(context, payload) {
    //payload = {id, smileEngineJson}
    try {
      await _calculateDengueProbability(context, payload);
    } catch (error) {
      console.debug('[dengue.js] (calculateDengueProbability) error');
      console.debug(error);
      context.commit('NEW_NOTIFICATION', error.errors, {root: true});
    }
  },
}

async function _loadDengue(context) {
  const client = await context.rootState.socket.client;
  const dengue = await client.list("dengue");
  context.commit("UPDATE_DENGUE_DATA", dengue);
}

async function _createDengue(context, payload) {
  payload = _addChangedByToPayload(context, payload)
  const client = await context.rootState.socket.client;
  const dengue = await client.create("dengue", payload);
  context.commit("UPDATE_DENGUE_DATA", [dengue]);
}

async function _editDengue(context, id, payload) {
  payload = _addChangedByToPayload(context, payload)
  const client = await context.rootState.socket.client;
  await client.patch("dengue", id, payload);
}

async function _deleteDengue(context, payload) {
  payload = _addChangedByToPayload(context, payload)
  const client = await context.rootState.socket.client;
  await client.delete("dengue", payload.id);
}

async function _calculateDengueProbability(context, payload) {
  smileRequest(
    payload.smileEngineJson,
    _onSuccessfullSmileRequest(context, payload),
    _onFailedSmileRequest(context),
  );
}

function _onSuccessfullSmileRequest(context, payload){
  return (responseText) => {
    const result = JSON.parse(responseText).result;
    result.dengue_probability = result.s1;
    
    const smile_result = {};
    smile_result[payload.id] = result;
    context.commit("UPDATE_SMILE_RESULT", smile_result);
  };
}

function _onFailedSmileRequest(context){
  return (status, responseText) => {
    console.debug('[dengue.js] (calculateDengueProbability) error');
    console.debug(responseText);
    context.commit('NEW_NOTIFICATION', [{
      'SMILE engine error': `Bad status: ${status}`,
    }], {root: true});
  };
}

function smileRequest(payload, onStatusOK, onOtherStatus) {
  const xhr = new XMLHttpRequest();
  //TODO use config file / system values for obtaining the correct url
  var url = process.env.NODE_ENV === 'production'
   ? "https://social.informatik.uni-bremen.de/smile-api/dengue"
   : 'http://localhost:5000/dengue';

  xhr.open("POST", url, true);
  xhr.setRequestHeader("Content-Type", "application/json");

  xhr.onreadystatechange = () => {
    if (xhr.readyState === 4){
      xhr.status === 200
      ? onStatusOK(xhr.responseText)
      : onOtherStatus(xhr.status, xhr.responseText)
    }
  };
  xhr.send(JSON.stringify(payload));
}

function _addChangedByToPayload(context, payload){
  const changed_by = context.rootGetters.user_id;
  return {
    ...payload,
    changed_by,
  }
}

const getters = {
  dengueData: (state) => state.dengueData,
  getSmileResult: (state) => (id) =>
    state.smileResult[id],
  getDengueById: (state) => (id) =>
      state.dengueData.find((dengue) => dengue.patient === id),
};

const dengueModule = {
  state,
  mutations,
  actions,
  getters,
};

export default dengueModule;
