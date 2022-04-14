<template>
    <base-input
        type="text"
        :value="value"
        v-on="$listeners"
        v-bind="$attrs"
    ></base-input>
</template>
<script>
export default {
    props: ['value'],
}
</script>
