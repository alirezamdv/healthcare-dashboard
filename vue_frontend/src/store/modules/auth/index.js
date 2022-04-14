import axios from "axios";
import {CSRF_TOKEN} from "./csrf_token.js";

const state = {
    token: null,
    username: null,
    user_id: null,
    logged_in: false,
    show_notifications: true,
};

const mutations = {
    SET_TOKEN(state, token) {
        state.token = token;
        if (token == null) {
            state.logged_in = false;
        } else {
            state.logged_in = true;
        }
    },
    SET_USERNAME(state, username) {
        state.username = username;
    },
    SET_USER_ID(state, user_id) {
        state.user_id = user_id;
    },
    SHOW_NOTIFICATIONS(state, payload) {
        state.show_notifications = payload;
    },

};

const actions = {

    signin({commit}, credentials) {
        commit("SET_USERNAME", credentials.user);

        //sends a post request to the drf rest auth endpoint with the given credentials
        //the response will contain a token if the login was successful
        //the token will then be saved to local storage for the time being logged in

        return new Promise((resolve, reject) => {
            axios
                .post(
                    "/api/rest-auth/login/",
                    {
                        username: credentials.user,
                        password: credentials.pw,
                    },
                    {
                        headers: {
                            "X-CSRFTOKEN": CSRF_TOKEN,
                        },
                    }
                )
                .then((response) => {
                    localStorage.setItem("token", response.data.key);
                    commit("SET_TOKEN", response.data.key);

                    // sends a get request to the drf rest auth endpoint with the obtained token to
                    // access the user information
                    // the user information will then be saved to be displayed in the ui
                    axios
                        .get(
                            "/api/rest-auth/user/",
                            {
                                headers: {
                                    "X-CSRFTOKEN": CSRF_TOKEN,
                                    Authorization: `Token ${localStorage.getItem("token")}`,
                                },
                            }
                        )
                        .then((response) => {
                            commit("SET_USER_ID", response.data.pk);
                            resolve(200);
                        });

                }, error => {
                    reject(error.response.status);
                });
        })

    },


    signout(context) {

        //removes the token from local storage and the back end and resets the state
        return new Promise((resolve) => {
            axios
                .post(
                    "/api/rest-auth/logout/logout/",
                    {
                        headers: {
                            "X-CSRFTOKEN": CSRF_TOKEN,
                            Authorization: `Token ${localStorage.getItem("token")}`,
                        },
                    }
                )
                .then(() => {
                    resolve(200);
                }).catch((e) => {
                    console.log(e);
            });

            localStorage.removeItem("token");
            context.commit("SET_TOKEN", null);
            context.commit("SET_USERNAME", null);
            resolve();
        }).catch((e) => {
            context.commit('NEW_NOTIFICATION', e.errors, {root: true});
        })
            ;

    },

    enableNotifications(context, payload) {
        context.commit('SHOW_NOTIFICATIONS', payload);
    },

};

const getters = {
    token: (state) => state.token,
    username: (state) => state.username,
    user_id: (state) => state.user_id,
    show_notifications: (state) => state.show_notifications,
};

const authModule = {
    state,
    mutations,
    actions,
    getters,
};

export default authModule;
