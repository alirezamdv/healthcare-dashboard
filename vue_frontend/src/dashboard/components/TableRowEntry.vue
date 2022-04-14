<template>

  <tr>
    <th>
     {{ name }}
    </th>
    <td
        v-for="(item, i) in this.$parent.tableData"
        :key="i">
      {{ item[id] }} {{ placeholder }}
    </td>
    <td>
      <base-input
        type="number"
        :value="value"
        v-on="listeners"
        v-bind="$attrs"
        :placeholder="place(placeholder)"
        min="0" oninput="validity.valid||(value='');">
      </base-input>
    </td>
  </tr>

</template>
<script>
import BaseInput from './BaseInput.vue';
export default {
  components: { BaseInput },
  inheritAttrs: false,
  name: "table-row-entry",
  props: {
    value: {
      type: [String, Number],
      description: "Input value"
    },
    name: {
      type: String,
    },
    id: {
      type: [String, Number],
    },
    placeholder: String,
  },
  computed: {
    listeners() {
      return {
        ...this.$listeners,
        input: this.updateValue,
        focus: this.onFocus,
        blur: this.onBlur
      };
    },
  },
  methods: {
    updateValue(evt) {
      this.$emit("input", evt);
    },
    onFocus(value) {
      this.focused = true;
      this.$emit("focus", value);
    },
    onBlur(value) {
      this.focused = false;
      this.$emit("blur", value);
    },
    place(placeholder) {
      return placeholder ? 'in ' + placeholder : null;
    }
  }
};

export class TRE {
  name;
  placeholder;
  value;

  constructor(name, placeholder = null, value = null){
    this.name = name;
    this.placeholder = placeholder;
    this.value = value;
  }
}

</script>
<style>
</style>
