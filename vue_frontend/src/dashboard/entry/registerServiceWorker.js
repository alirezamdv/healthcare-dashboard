/* eslint-disable no-console */
/**
 * This service worker is not used by the Dengue Dashboard
 */

import { register } from 'register-service-worker'

if (process.env.NODE_ENV === 'production') {
  register(`${process.env.BASE_URL}service-worker.js`, {
    ready () {
      console.log("Note: This service worker is not being used just yet but may be used in the future.");
      // console.log(
      //   'App is being served from cache by a service worker.\n' +
      //   'For more details, visit https://goo.gl/AFskqB'
      // )
    },
    registered () {
      console.log("Note: This service worker is not being used just yet but may be used in the future.");
      // console.log('Service worker has been registered.')
    },
    cached () {
      console.log("Note: This service worker is not being used just yet but may be used in the future.");
      // console.log('Content has been cached for offline use.')
    },
    updatefound () {
      console.log("Note: This service worker is not being used just yet but may be used in the future.");
      // console.log('New content is downloading.')
    },
    updated () {
      console.log("Note: This service worker is not being used just yet but may be used in the future.");
      // console.log('New content is available; please refresh.')
    },
    offline () {
      console.log("Note: This service worker is not being used just yet but may be used in the future.");
      // console.log('No internet connection found. App is running in offline mode.')
    },
    error () {
      console.log("Note: This service worker is not being used just yet but may be used in the future.");
      // console.error('Error during service worker registration:', error)
    }
  })
}
