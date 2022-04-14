<template>
  <tr>
    <th width="30%" class="text-wrap" :title="name">
      <h4 v-if="heading">{{ name }}</h4>
      <span v-else>{{ name }}</span>
    </th>

    <td v-for="(item, i) in history"
        :key="i">
        <div class="wordbreak">
          {{ prefix }} {{ transformHistoryItem ? transformHistoryItem(item) : item }} {{ suffix }}
        </div>
    </td>

    <td>
      <slot></slot>
    </td>
  </tr>
</template>
<script>
export default {
  props: {
    name: String,
    heading: Boolean,
    prefix: String,
    suffix: String,
    history: Array,
    transformHistoryItem: Function,
  },
}
</script>
