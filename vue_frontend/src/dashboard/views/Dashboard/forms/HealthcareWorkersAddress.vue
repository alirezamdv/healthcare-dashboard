<template>
  <div class="my-4">
    <strong v-if="!this.new">Address {{ this.address_index }}</strong>
    <div class="row">
      <div class="col-md-6 col-sm-12">
        <label :for="'address-category-' + this.address_index">
          Address Category
        </label>
        <select
          :id="'address-category-' + this.address_index"
          class="form-control"
          v-model="address_category"
        >
          <option
            v-for="address_category_option in address_categories"
            v-bind:key="address_category_option"
            v-bind:value="address_category_option"
          >
            {{ address_category_option }}
          </option>
        </select>
      </div>
      <div class="col-md-6 col-sm-12">
        <label :for="'address-note-' + this.address_index">
          Address Note
        </label>
        <input
          :id="'address-note-' + this.address_index"
          class="form-control"
          v-model="address_note"
        />
      </div>
    </div>
    <div class="row">
      <div class="col-md-6 col-sm-12">
        <label :for="'address-textual-' + this.address_index">
          Address
        </label>
        <input
          :id="'address-textual-' + this.address_index"
          class="form-control"
          v-model="address_textual"
        />
      </div>
      <div class="col-md-3 col-sm-6">
        <label :for="'address-geo-position-latitude-' + this.address_index">
          Latitude
        </label>
        <input
          type="number"
          disabled
          :id="'address-geo-position-latitude-' + this.address_index"
          class="form-control"
          v-model="address_geo_position.latitude"
        />
      </div>
      <div class="col-md-3 col-sm-6">
        <label :for="'address-geo-position-longitude-' + this.address_index">
          Latitude
        </label>
        <input
          type="number"
          disabled
          :id="'address-geo-position-longitude-' + this.address_index"
          class="form-control"
          v-model="address_geo_position.longitude"
        />
      </div>
    </div>
  </div>
</template>

<script>
// TODO: imports

export default {
  name: "healthcare-workers-address",
  props: {
    patient_id: {
      type: String,
      description: "ID of the Patient",
    },
    address_index: {
      type: Number,
      description: "Index of the address"
    },
    new: {
      type: Boolean,
      default: false,
      description: "Marks a new address"
    }
  },
  components: {
    // TODO: Components
  },
  created() {
    console.debug("Address component created");
  },
  data() {
    return {
      address_categories: [
        "Home",
        "Work",
        "School"
      ],
      address_category: "",
      address_note: "",
      address_textual: "",
      address_geo_position: {
        latitude: null,
        longitude: null
      }
    };
  },
  methods: {
    // TODO: Methods to get triggered ipon adding addresses
  },
  computed: {},
  watch: {},
};
</script>

<style>
</style>
