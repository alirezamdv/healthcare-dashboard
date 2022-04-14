<template>
    <component class="form-group"
               :is="tag"
               :class="[{show: isOpen}, {'dropdown': direction === 'down'}, {'dropup': direction ==='up'}]"
               aria-haspopup="true"
               :aria-expanded="isOpen"
               @click="toggleDropDown"
               v-click-outside="closeDropDown">
        <div v-if="label">
        <slot name="label">
            <label v-if="label" class="form-control-label" :class="labelClasses">
                {{label}}
                <span v-if="required" title="Required">*</span>
            </label>
        </slot>
        <br>
        </div>
        <slot name="title">
            <a class="dropdown-toggle nav-link"
               :class="{'no-caret': hideArrow}"
               data-toggle="dropdown">
                <i :class="icon"></i>
                <span class="no-icon">{{title}}</span>
            </a>
        </slot>
        <ul class="dropdown-menu"
            ref="menu"
            :class="[{'dropdown-menu-right': position === 'right'}, {show: isOpen}, menuClasses]">
            <slot></slot>
        </ul>
    </component>
</template>
<script>
export default {
  name: "base-dropdown",
  props: {
    required: {
      type: Boolean,
      description: "Whether input is required (adds an asterix *)"
    },
    direction: {
      type: String,
      default: "down"
    },
    title: {
      type: String,
      description: "Dropdown title"
    },
    icon: {
      type: String,
      description: "Icon for dropdown title"
    },
    position: {
      type: String,
      description: "Position of dropdown menu (e.g right|left)"
    },
    menuClasses: {
      type: [String, Object],
      description: "Dropdown menu classes"
    },
    labelClasses: {
      type: String,
      description: "Input label css classes"
    },
    hideArrow: {
      type: Boolean,
      description: "Whether dropdown arrow should be hidden"
    },
    appendToBody: {
      type: Boolean,
      default: true,
      description: "Whether dropdown should be appended to document body"
    },
    label: {
      type: String,
      description: "Input label (text before input)"
    },
    tag: {
      type: String,
      default: "li",
      description: "Dropdown html tag (e.g div, li etc)"
    }
  },
  data() {
    return {
      isOpen: false
    };
  },
  methods: {
    toggleDropDown() {
      this.isOpen = !this.isOpen;
      this.$emit("change", this.isOpen);
    },
    closeDropDown() {
      this.isOpen = false;
      this.$emit("change", this.isOpen);
    }
  }
};
</script>
<style>
.dropdown {
  list-style-type: none;
}

.dropdown .dropdown-toggle {
  cursor: pointer;
}
</style>
