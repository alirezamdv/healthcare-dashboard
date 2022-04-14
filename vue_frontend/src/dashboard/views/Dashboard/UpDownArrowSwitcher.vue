<template>
    <div v-if="value === null"></div>
    <span v-else>
        <b-icon-arrow-down v-if="value === 'ascending'"></b-icon-arrow-down>
        <b-icon-arrow-up v-if="value === 'descending'"></b-icon-arrow-up>
    </span>
</template>

<script>
import { BIconArrowUp, BIconArrowDown } from 'bootstrap-vue'

// TODO? This file could be moved to some core folder or something similar.
// For now it is only used in ReportsTable and thus can stay here.
export default {
    props: ['value'],
    components: {
    BIconArrowUp,
    BIconArrowDown,
  },
}
</script>
<style>
</style>