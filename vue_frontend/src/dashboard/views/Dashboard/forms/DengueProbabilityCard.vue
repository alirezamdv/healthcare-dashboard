<template>
  <card type="default" >
    <h2 class="text-white mb-0">Current dengue probabilty: </h2>
    <h3 class="text-white mb-0">{{ dengue_probability }}% </h3>
  </card>
</template>

<script>
export default {
    props: ["dengue_probability"]
}
</script>
<style>
</style>
