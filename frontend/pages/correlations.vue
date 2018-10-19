<template>
  <v-container grid-list-md>
    <div v-if="!readyCharts" class="text-md-center ma-5">
      <v-progress-circular
        :size="70"
        :width="7"
        color="amber"
        indeterminate
      ></v-progress-circular>
    </div>

    <div v-if="readyCharts">
      <v-layout align-start justify-space-between row fill-height>
          <v-flex class="md12">
            <vue-highcharts :options="optionsProximityChartColumn"></vue-highcharts>
          </v-flex>
      </v-layout>

      <v-layout align-start justify-space-between row fill-height>
          <v-flex class="md12">
            <vue-highcharts :options="optionsDwellTimeChartArea"></vue-highcharts>
          </v-flex>
      </v-layout>

      <v-layout align-start justify-space-between row fill-height>
          <v-flex class="md12">
            <vue-highcharts :options="optionsRepeatVisitorsChartArea"></vue-highcharts>
          </v-flex>
      </v-layout>

    </div>

  </v-container>

</template>

<script>
  import VueHighcharts from 'vue2-highcharts'
  import ChartsMixin from '~/mixins/chartsMixin.js'

  export default {
    name: "correlations",
    components: {
      VueHighcharts,
    },
    mixins: [
      ChartsMixin
    ],
    async created() {
      await this.loadCorrelations();
    }
  }
</script>

<style scoped>

</style>
