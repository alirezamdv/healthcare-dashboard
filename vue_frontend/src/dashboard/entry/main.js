import Vue from "vue/dist/vue.js";

import App from '../../App.vue'
import router from './router.js'
import store from '../../store/vuex_usage_utils'
import './registerServiceWorker.js'
import ArgonDashboard from '../plugins/argon-dashboard'

import { Datetime } from 'vue-datetime'

import 'vue-datetime/dist/vue-datetime.css'

import { VBPopover } from 'bootstrap-vue'
// Note: Vue automatically prefixes the directive name with 'v-'
Vue.directive('b-popover', VBPopover)

Vue.config.productionTip = false

Vue.use(ArgonDashboard)
Vue.use(Datetime)

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
