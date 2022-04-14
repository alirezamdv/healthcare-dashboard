<template>
    <select
        v-model="key"
        class="form-control"
        @change="onChange($event)"
    >
        <option
            v-for="stat in statusOptions"
            :value="stat.option"
            :key="stat.option"
            type="text"
        >
            {{ stat.option }}
        </option>
    </select>
</template>
<script>
export default {
    props: ['statusOptions', 'value'],
    created() {
        this.key = this.value;
    },
    data() {
        return {
            key: "",
        };
    },
     watch: {
        value: function(newVal) {
            if (newVal === null){
                this.key = newVal;
            }
        }
    },
    methods: {
        onChange(event) {
            this.$emit("input", event.target.value);
        }
    }
}
</script>
