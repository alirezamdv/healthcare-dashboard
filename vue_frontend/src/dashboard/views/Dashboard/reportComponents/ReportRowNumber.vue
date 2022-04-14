<template>
    <base-input
        type="number"
        id="id"
        :value="value"
        v-on="$listeners"
        v-bind="$attrs"
        :placeholder="place(placeholder)"
        min="0" oninput="validity.valid||(value='');"
    ></base-input>
</template>
<script>
export default {
    props: ['value', 'placeholder'],
    methods: {
        place(placeholder) {
            return placeholder ? 'in ' + placeholder : null;
        }
    },
}
</script>
