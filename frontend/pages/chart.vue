<template>
  <div>
    <v-container grid-list-md>

      <v-layout align-start justify-space-between row fill-height>
        <v-flex>
          <v-btn @click="submitDate()" large class="blue darken-3 white--text">Submit</v-btn>
        </v-flex>

        <v-flex md6>
          <DatePicker v-model="date1" labelText="FROM date" :error_messages="errors.date1"></DatePicker>
        </v-flex>

        <v-flex md6>
          <DatePicker v-model="date2" labelText="TO date" :error_messages="errors.date2"></DatePicker>
        </v-flex>
      </v-layout>

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
            <v-flex class="md8">
              <vue-highcharts :options="optionsProximityChartColumn"></vue-highcharts>
            </v-flex>

            <v-flex class="md4">
              <vue-highcharts :options="optionsProximityChartPie"></vue-highcharts>
            </v-flex>
        </v-layout>

        <v-layout align-start justify-space-between row fill-height>
            <v-flex class="md8">
              <vue-highcharts :options="optionsDwellTimeChartArea"></vue-highcharts>
            </v-flex>

            <v-flex class="md4">
              <vue-highcharts :options="optionsDwellTimeChartPie"></vue-highcharts>
            </v-flex>
        </v-layout>

        <v-layout align-start justify-space-between row fill-height>
            <v-flex class="md8">
              <vue-highcharts :options="optionsRepeatVisitorsChartArea"></vue-highcharts>
            </v-flex>

            <v-flex class="md4">
              <vue-highcharts :options="optionsRepeatVisitorsChartPie"></vue-highcharts>
            </v-flex>
        </v-layout>

      </div>

    </v-container>
  </div>
</template>

<script>
import VueHighcharts from 'vue2-highcharts'
import ChartsMixin from '~/mixins/chartsMixin.js'
import DatePicker from '~/components/DatePicker.vue'


export default {
  components: {
    VueHighcharts, DatePicker
  },
  mixins: [
    ChartsMixin
  ],
  data: () => ({
    date1: null,
    menu1: false,
    date2: null,
    menu2: false,
    minDate: '2017-12-20',
    currentDate: null,
    errors: {
      date1: '',
      date2: ''
    }
  }),
  async created() {
    let currentDate = new Date();
    currentDate.setDate(currentDate.getDate() - 1);
    let day = currentDate.getDate().toString();
    day = day.length > 1 ? day : '0' + day;
    let month = (currentDate.getMonth() + 1).toString();
    month = month.length > 1 ? month : '0' + month;
    let year = currentDate.getFullYear();
    this.currentDate  = year + '-' + month + '-' + day;

    await this.loadPickedDate(this.currentDate)
  },
  methods: {
    validateDates() {
      this.errors = [];

      if (this.date1 == null && this.date2 == null) {
        this.errors.date1 = 'Date field cant be unfilled';
      }

      if (this.date1 > this.date2) {
        let temp = '';
        temp = this.date1;
        this.date1 = this.date2;
        this.date2 = temp;
      }
    },

    async submitDate() {
      this.validateDates();

      if ((this.date1 === this.date2 || (this.date1 != null && this.date2 == null) || (this.date1 == null && this.date2 != null))
        && this.errors.date1 !== '') {
        this.readyCharts = false;
        await this.loadPickedDate(this.date1);
      }
      else if (this.date1 !== this.date2 && this.errors.date1 !== '') {
        this.readyCharts = false;
        await this.loadPickedRangeOfDates({startDate: this.date1, endDate: this.date2});
      }
    }
  }

}
</script>
