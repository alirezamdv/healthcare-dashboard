<template>
    <span>
        <base-input 
            disabled 
            :value="value ? new Date(value).toLocaleString() : ''"
            placeholder="Select Datetime">
        </base-input>

        <base-button 
            class="btn btn-md col-md-8"
            type="primary"
            @click="openDatePicker('date-picker')" icon="fa fa-calendar">
        </base-button>

        <base-button 
            v-if="showRemove"
            type="danger"
            icon="fas fa-times" class="btn btn-md ml-2"
            @click="$emit('input', null)">
        </base-button>

        <datetime 
            ref="date-picker"
            type="datetime" 
            :backdrop-click=true
            :auto=true
            @input="$emit('input', $event)">
        </datetime>
    </span>
</template>
<script>
import {Datetime} from 'vue-datetime';

export default {
    props: ['value', 'showRemove'],
    components: {
        datetime: Datetime,
    },
    methods: {
        openDatePicker(pickerName) {
            try {
                const input = this.$refs[pickerName].$el.firstChild.nextElementSibling;
                if (input) {
                    input.click();
                }
            } catch (error) {
                console.debug('[ReportRowDate] (openDatePicker)', error);
                throw error;
            }
        },
    },
}
</script>
<style>
.vdatetime-popup__body {
    white-space: normal;
}
</style>