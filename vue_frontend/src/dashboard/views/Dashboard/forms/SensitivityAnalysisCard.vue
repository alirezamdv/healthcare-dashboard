<template>
  <card type="default" style="white-space: pre-wrap;">
    <h2 class="text-white">The following data could have an impact on the diagnosis.</h2>
    <div v-if="highSensitivity">
      <h2 class="text-red mt-2">High impact</h2>
      <h3 class="text-red mb-0"
        v-for="sensitivityEntry in highSensitivity"
        v-bind:key="sensitivityEntry"
        v-bind:value="sensitivityEntry"
        >{{ sensitivityEntry }}</h3>
    </div>
    <div v-if="mediumSensitivity">
      <h2 class="text-yellow mt-2">Medium impact</h2>
      <h3 class="text-yellow mb-0"
        v-for="sensitivityEntry in mediumSensitivity"
        v-bind:key="sensitivityEntry"
        v-bind:value="sensitivityEntry"
        >{{ sensitivityEntry }}</h3>
    </div>
    <div v-if="lowSensitivity">
      <h2 class="text-white mt-2">Low impact</h2>
      <h3 class="text-white mb-0"
        v-for="sensitivityEntry in lowSensitivity"
        v-bind:key="sensitivityEntry"
        v-bind:value="sensitivityEntry"
        >{{ sensitivityEntry }}</h3>
    </div>
  </card>
</template>

<script>
const high = 30;
const medium = 15;
const low = 5;
const max_count_of_items = 10;

export default {
    props: ["sensitivity_analysis"],
    computed: {
      sensitivity_analysis_max_count() {
        return this.sensitivity_analysis
          ? this.sensitivity_analysis.filter(value => value).slice(0,max_count_of_items)
          : {};
      },
      highSensitivity() {
        const result = [];
        for (const value of Object.values(this.sensitivity_analysis_max_count)) {
          if(value && percentage(value.value) >= high)
            result.push(value.name + '\n')
        }
        return result.empty
          ? null
          : result;
      },
      mediumSensitivity() {
        const result = [];
        for (const value of Object.values(this.sensitivity_analysis_max_count)) {
          if(value && percentage(value.value) >= medium && percentage(value.value) < high)
            result.push(value.name + '\n')
        }
        return result.empty
          ? null
          : result;
      },
      lowSensitivity() {
        const result = [];
        for (const value of Object.values(this.sensitivity_analysis_max_count)) {
          if(value && percentage(value.value) >= low && percentage(value.value) < medium)
            result.push(value.name + '\n')
        }
        return result.empty
          ? null
          : result;
      },
    }
}

function percentage(value) {
  return Math.floor(value * 100);
}

</script>
<style>
</style>
