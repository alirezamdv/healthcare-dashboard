const state = {
    showWard: false,
    ward: null,
    wards: [],
  };
  
  const mutations = {
    UPDATE_SHOW_WARD(state, payload) {
      state.showWard = payload;
    },
    UPDATE_WARD(state, payload) {
        state.ward = payload;
    },
    UPDATE_WARDS(state, payload) {
        state.wards = payload;
    },
  };
  
  const actions = {
    async loadWards(context, payload) {
        //TODO this is dummy data for now, get from be!
        payload = [1,2,3,4]
        console.debug('[user.js] (loadWards)', {payload});
        context.commit("UPDATE_WARDS", payload);
    },

    async showWard(context, payload) {
      console.debug('[user.js] (showWard)', {payload});
      context.commit("UPDATE_SHOW_WARD", payload);
    },

    async ward(context, payload) {
      console.debug('[user.js] (ward)', {payload});
      context.commit("UPDATE_WARD", payload);
    },
  }

  const getters = {
    showWard: (state) => state.showWard,
    ward: (state) => state.ward,
    wards: (state) => state.wards,
  };
  
  const userModule = {
    state,
    mutations,
    actions,
    getters,
  };
  
  export default userModule;
  