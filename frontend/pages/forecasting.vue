<template>
  <div>
    <div v-if="!readyCharts" class="text-md-center ma-5">
      <v-progress-circular
        :size="70"
        :width="7"
        color="amber"
        indeterminate
      ></v-progress-circular>
    </div>
    <v-container grid-list-md>
      <div v-if="readyCharts">
        <v-layout align-start justify-space-between row fill-height>
            <v-flex class="md12">
              <vue-highcharts :options="optionsForecastingConnectedChartArea"></vue-highcharts>
            </v-flex>
        </v-layout>

        <v-layout align-start justify-space-between row fill-height>
            <v-flex class="md12">
              <vue-highcharts :options="optionsForecastingVisitorsChartArea"></vue-highcharts>
            </v-flex>
        </v-layout>

        <v-layout align-start justify-space-between row fill-height>
            <v-flex class="md12">
              <vue-highcharts :options="optionsForecastingPasserbyChartArea"></vue-highcharts>
            </v-flex>
        </v-layout>
      </div>
    </v-container>
    </div>
</template>

<script>
  import VueHighcharts from 'vue2-highcharts'
  import ChartsMixin from '~/mixins/chartsMixin.js'

  export default {
    name: "forecasting",
    components: {
      VueHighcharts,
    },
    mixins: [
      ChartsMixin
    ],
    async created() {
      await this.loadForecasting();
    }
  }
</script>

<style scoped>

</style>
