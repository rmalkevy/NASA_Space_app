/*** Charts Mixin ***/

const MOCK_DATE = require('~/assets/MOCK_DATE.json');

const ChartsMixin = {
  data() {
    return {
      readyCharts: false,
      idInterval: null,

      /*** Proximity Column Chart ***/
      optionsProximityChartColumn: {
        chart: {
          type: 'column',
        },
        title: {
          text: ''
        },
        subtitle: {
          text: 'Source: cisco-cmx.unit.ua'
        },
        xAxis: {
          gridLineWidth: 1,
          categories: [],
          crosshair: true,
          title: {
            text: 'Hours'
          }
        },
        yAxis: {
          minorTickInterval: 'auto',
          min: 0,
          title: {
            text: 'Clients'
          }
        },
        tooltip: {
          headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
          pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
              '<td style="padding:0"><b>{point.y:.1f}</b></td></tr>',
          footerFormat: '</table>',
          shared: true,
          useHTML: true
        },
        plotOptions: {
          column: {
            pointPadding: 0.2,
            borderWidth: 0
          }
        },
        series: [],
        colors: ['#55BF3B', '#DF5353', '#7798BF'],
      },

      /*** Proximity Pie Chart ***/
      optionsProximityChartPie: {
        chart: {
          type: 'pie'
        },
        title: {
          text: 'Proximity Distribution'
        },
        subtitle: {
          text: 'Source: cisco-cmx.unit.ua'
        },
        plotOptions: {
          pie: {
            shadow: false,
            center: ['50%', '50%']
          }
        },
        series: [],
      },

      /*** Dwell Time chart Area ***/
      optionsDwellTimeChartArea: {
        chart: {
          type: 'area'
        },
        title: {
          text: 'Dwell Time'
        },
        subtitle: {
          text: 'Source: cisco-cmx.unit.ua'
        },
        xAxis: {
          gridLineWidth: 1,
          categories: [],
          tickmarkPlacement: 'on',
          title: {
            text: 'Hours'
          }
        },
        yAxis: {
          minorTickInterval: 'auto',
          title: {
            text: 'Clients'
          },
        },
        plotOptions: {
          area: {
            stacking: 'normal',
            lineColor: '#666666',
            lineWidth: 1,
            marker: {
              lineWidth: 1,
              lineColor: '#666666'
            }
          }
        },
        series: [],
        colors: ['#55BF3B', '#DF5353', '#C6FF00', '#FFFF00', '#039BE5'],
      },

      /*** Dwell Time Pie Chart ***/
      optionsDwellTimeChartPie: {
        chart: {
          type: 'pie'
        },
        title: {
          text: 'Dwell Time Distribution'
        },
        subtitle: {
          text: 'Source: cisco-cmx.unit.ua'
        },
        plotOptions: {
          pie: {
            shadow: false,
            center: ['50%', '50%']
          }
        },
        series: [],
        colors: ['#55BF3B', '#DF5353', '#C6FF00', '#FFFF00', '#039BE5'],
      },

      /****  Repeat Visitors  ****/
      optionsRepeatVisitorsChartArea: {
        title: {
          text: 'Repeat Visitors'
        },
        subtitle: {
          text: 'Source: cisco-cmx.unit.ua'
        },
        xAxis: {
          gridLineWidth: 1,
          categories: [],
          tickmarkPlacement: 'on',
          title: {
            text: 'Hours'
          }
        },
        yAxis: {
          minorTickInterval: 'auto',
          title: {
            text: 'Clients'
          },
        },
        plotOptions: {
          area: {
            stacking: 'normal',
            lineColor: '#666666',
            lineWidth: 1,
            marker: {
              lineWidth: 1,
              lineColor: '#666666'
            }
          }
        },
        series: [],
        colors: ['#55BF3B', '#DF5353', '#0288D1', '#FB8C00', '#039BE5'],
      },
      optionsRepeatVisitorsChartPie: {
        chart: {
          type: 'pie'
        },
        title: {
          text: 'Repeat Visitors'
        },
        subtitle: {
          text: 'Source: cisco-cmx.unit.ua'
        },
        plotOptions: {
          pie: {
            shadow: false,
            center: ['50%', '50%']
          }
        },
        series: [],
        colors: ['#55BF3B', '#DF5353', '#0288D1', '#FB8C00', '#039BE5'],
      },

      /*** Forecasting chart Area ***/
      optionsForecastingConnectedChartArea: {
         title: {
          text: 'Repeat Visitors'
        },
        subtitle: {
          text: 'Source: cisco-cmx.unit.ua'
        },
        xAxis: {
          gridLineWidth: 1,
          categories: [],
          tickmarkPlacement: 'on',
          title: {
            text: 'Hours'
          }
        },
        yAxis: {
          minorTickInterval: 'auto',
          title: {
            text: 'Clients'
          },
        },
        plotOptions: {
          area: {
            stacking: 'normal',
            lineColor: '#666666',
            lineWidth: 1,
            marker: {
              lineWidth: 1,
              lineColor: '#666666'
            }
          }
        },
        series: [],
        colors: ['#55BF3B', '#DF5353', '#0288D1', '#FB8C00', '#039BE5'],
      },

      /*** Forecasting Visitors chart Area ***/
      optionsForecastingVisitorsChartArea: {
         title: {
          text: 'Repeat Visitors'
        },
        subtitle: {
          text: 'Source: cisco-cmx.unit.ua'
        },
        xAxis: {
          gridLineWidth: 1,
          categories: [],
          tickmarkPlacement: 'on',
          title: {
            text: 'Hours'
          }
        },
        yAxis: {
          minorTickInterval: 'auto',
          title: {
            text: 'Clients'
          },
        },
        plotOptions: {
          area: {
            stacking: 'normal',
            lineColor: '#666666',
            lineWidth: 1,
            marker: {
              lineWidth: 1,
              lineColor: '#666666'
            }
          }
        },
        series: [],
        colors: ['#55BF3B', '#DF5353', '#0288D1', '#FB8C00', '#039BE5'],
      },

      /*** Forecasting chart Area ***/
      optionsForecastingPasserbyChartArea: {
         title: {
          text: 'Repeat Visitors'
        },
        subtitle: {
          text: 'Source: cisco-cmx.unit.ua'
        },
        xAxis: {
          gridLineWidth: 1,
          categories: [],
          tickmarkPlacement: 'on',
          title: {
            text: 'Hours'
          }
        },
        yAxis: {
          minorTickInterval: 'auto',
          title: {
            text: 'Clients'
          },
        },
        plotOptions: {
          area: {
            stacking: 'normal',
            lineColor: '#666666',
            lineWidth: 1,
            marker: {
              lineWidth: 1,
              lineColor: '#666666'
            }
          }
        },
        series: [],
        colors: ['#55BF3B', '#DF5353', '#0288D1', '#FB8C00', '#039BE5'],
      },
    }
  },
  methods: {
    async loadPickedDate(pickedDate) {
      const response = await this.$store.dispatch('charts/loadPickedDateChart', pickedDate);

      this.showCharts(response.data);
    },

    async loadPickedRangeOfDates(data) {
      const response = await this.$store.dispatch('charts/loadPickedRangeDateChart', data);

      this.showCharts(response.data);
    },

    async loadCorrelations() {
      const response = await this.$store.dispatch('charts/loadCorrelations');
      this.showCharts(response.data);
    },

    async loadForecasting() {
      const response = await this.$store.dispatch('charts/loadForecasting');
      this.showForecastingCharts(response.data);
    },

    showCharts(data) {
      /***
       * Proximity 1 Charts
       **/
      if (data.hasOwnProperty('Proximity')) {
        this.optionsProximityChartColumn.title.text = 'Proximity';

        /**
         *   Chart
         **/
        if (data.Proximity.hasOwnProperty('chart')) {

          /*** xAxis ***/
          if (data.Proximity.chart.hasOwnProperty('xAxis')) {
            this.optionsProximityChartColumn.xAxis.categories = data.Proximity.chart.xAxis;
          }

          this.optionsProximityChartColumn.series = [];

          /*** Connected ***/
          if (data.Proximity.chart.hasOwnProperty('connected')) {
            let connected = {name: 'connected', data: []};
            /*** Initialize connected data ***/

            connected.data = data.Proximity.chart.connected;
            this.optionsProximityChartColumn.series.push(connected);
          } else {
            console.log('Connected error')
          }

          /*** Visitors ***/
          if (data.Proximity.chart.hasOwnProperty('visitors')) {
            let visitors = {name: 'visitors', data: []};
            /*** Initialize visitors data ***/
            visitors.data = data.Proximity.chart.visitors;
            this.optionsProximityChartColumn.series.push(visitors);
          } else {
            console.log('Visitors error')
          }

          /*** Passerby ***/
          if (data.Proximity.chart.hasOwnProperty('passerby')) {
            let passerby = {name: 'passerby', data: []};
            /*** Initialize passerby data ***/
            passerby.data = data.Proximity.chart.passerby;
            this.optionsProximityChartColumn.series.push(passerby);
          } else {
            console.log('Passerby error')
          }

        } else {
          console.log('chart error')
        }

        /**
         * Distribution
         **/
        if (data.Proximity.hasOwnProperty('distribution')) {

          this.optionsProximityChartPie.series = [];

          /*** Initialize outer pie chart data ***/
          let dataOuterPie = {name: 'Outer', data: [], size: '80%', innerSize: '60%',};
          dataOuterPie.data.push({name: 'Connected', y: data.Proximity.distribution.Connected, color: '#5FBF3F'});
          dataOuterPie.data.push({name: 'Probing', y: data.Proximity.distribution.Probing, color: '#DF5F59'});
          this.optionsProximityChartPie.series.push(dataOuterPie);

          /*** Initialize inner pie chart data ***/
          let dataInnerPie = {name: 'Inner', data: [], size: '60%',};
          dataInnerPie.data.push({name: 'Visitors', y: data.Proximity.distribution.Visitors, color: '#50B030'});
          dataInnerPie.data.push({name: 'Passerby', y: data.Proximity.distribution.Passerby, color: '#D05050'});
          this.optionsProximityChartPie.series.push(dataInnerPie);

        } else {
          console.log('Distribution error')
        }

      } else {
        console.log('Proximity error')
      }

      /***
       * Dwell Time 2 Charts
       **/
      if (data.hasOwnProperty('Dwell Time')) {
        this.optionsDwellTimeChartArea.title.text = 'Dwell Time';

        this.optionsDwellTimeChartArea.series = [];

        if (data['Dwell Time'].hasOwnProperty('chart')) {
          this.optionsDwellTimeChartArea.xAxis.categories = data['Dwell Time'].chart.xAxis;
          this.optionsDwellTimeChartArea.series.push({name: '5-30 mins', data: data['Dwell Time'].chart['5-30 mins']});
          this.optionsDwellTimeChartArea.series.push({
            name: '30-60 mins',
            data: data['Dwell Time'].chart['30-60 mins']
          });
          this.optionsDwellTimeChartArea.series.push({name: '1-5 hours', data: data['Dwell Time'].chart['1-5 hours']});
          this.optionsDwellTimeChartArea.series.push({name: '5-8 hours', data: data['Dwell Time'].chart['5-8 hours']});
          this.optionsDwellTimeChartArea.series.push({name: '8+ hours', data: data['Dwell Time'].chart['8+ hours']});
        } else {
          console.log('Dwell Time - chart error')
        }

        /**
         * Distribution
         **/
        if (data['Dwell Time'].hasOwnProperty('distribution')) {

          this.optionsDwellTimeChartPie.series = [];

          /*** Initialize outer pie chart data ***/
          let dataPie = {name: 'Dwell Time', data: []};
          dataPie.data.push({name: '5-30 mins', y: data['Dwell Time'].distribution['5-30 mins']});
          dataPie.data.push({name: '30-60 mins', y: data['Dwell Time'].distribution['30-60 mins']});
          dataPie.data.push({name: '1-5 hours', y: data['Dwell Time'].distribution['1-5 hours']});
          dataPie.data.push({name: '5-8 hours', y: data['Dwell Time'].distribution['5-8 hours']});
          dataPie.data.push({name: '8+ hours', y: data['Dwell Time'].distribution['8+ hours']});
          this.optionsDwellTimeChartPie.series.push(dataPie);

        } else {
          console.log('Distribution error')
        }

      } else {
        console.log('Dwell Time error')
      }

      /***
       * Repeat Visitors 2 Charts
       **/
      if (data.hasOwnProperty('Repeat Visitors')) {
        this.optionsRepeatVisitorsChartArea.title.text = 'Repeat Visitors';

        this.optionsRepeatVisitorsChartArea.series = [];

        if (data['Repeat Visitors'].hasOwnProperty('chart')) {
          this.optionsRepeatVisitorsChartArea.xAxis.categories = data['Repeat Visitors'].chart.xAxis;
          this.optionsRepeatVisitorsChartArea.series.push({
            name: 'DAILY',
            data: data['Repeat Visitors'].chart['DAILY']
          });
          this.optionsRepeatVisitorsChartArea.series.push({
            name: 'WEEKLY',
            data: data['Repeat Visitors'].chart['WEEKLY']
          });
          this.optionsRepeatVisitorsChartArea.series.push({
            name: 'OCCASIONAL',
            data: data['Repeat Visitors'].chart['OCCASIONAL']
          });
          this.optionsRepeatVisitorsChartArea.series.push({
            name: 'FIRST_TIME',
            data: data['Repeat Visitors'].chart['FIRST_TIME']
          });
        } else {
          console.log('Repeat Visitors - chart error')
        }

        /**
         * Distribution
         **/
        if (data['Repeat Visitors'].hasOwnProperty('distribution')) {

          this.optionsRepeatVisitorsChartPie.series = [];

          /*** Initialize Repeat Visitors Pie chart data ***/
          let dataPie = {name: 'Repeat Visitors', data: []};
          dataPie.data.push({name: 'DAILY', y: data['Repeat Visitors'].distribution['DAILY']});
          dataPie.data.push({name: 'WEEKLY', y: data['Repeat Visitors'].distribution['WEEKLY']});
          dataPie.data.push({name: 'OCCASIONAL', y: data['Repeat Visitors'].distribution['OCCASIONAL']});
          dataPie.data.push({name: 'FIRST_TIME', y: data['Repeat Visitors'].distribution['FIRST_TIME']});
          this.optionsRepeatVisitorsChartPie.series.push(dataPie);

        } else {
          console.log('Distribution error')
        }

      } else {
        console.log('Repeat Visitors error')
      }


      this.readyCharts = true;
    },

    showForecastingCharts(data) {
      /***
       * Connected 1 Charts
       **/
      if (data.hasOwnProperty('connected')) {
        this.optionsForecastingConnectedChartArea.title.text = 'Connected';

        /*** xAxis ***/
        if (data.connected.hasOwnProperty('xAxis')) {
          this.optionsForecastingConnectedChartArea.xAxis.categories = data.connected.xAxis;
        }

        this.optionsForecastingConnectedChartArea.series = [];

        /*** Past data ***/
        if (data.connected.hasOwnProperty('past_data')) {
          let pastData = {name: 'Past data', data: []};
          /*** Initialize Past data ***/

          pastData.data = data.connected.past_data;
          this.optionsForecastingConnectedChartArea.series.push(pastData);
        } else {
          console.log('Past data error')
        }

        /*** Trend data ***/
        if (data.connected.hasOwnProperty('trend')) {
          let trend = {name: 'Trend', data: []};
          /*** Initialize Trend data ***/

          trend.data = data.connected.trend;
          this.optionsForecastingConnectedChartArea.series.push(trend);
        } else {
          console.log('Trend data error')
        }

        /*** Forecast data ***/
        if (data.connected.hasOwnProperty('forecast')) {
          let forecast = {name: 'Forecast', data: []};
          /*** Initialize forecast data ***/

          forecast.data = data.connected.forecast;
          this.optionsForecastingConnectedChartArea.series.push(forecast);
        } else {
          console.log('Trend data error')
        }

      }

      /***
       * Visitors 2 Charts
       **/
      if (data.hasOwnProperty('visitors')) {
        this.optionsForecastingVisitorsChartArea.title.text = 'Visitors';

        /*** xAxis ***/
        if (data.visitors.hasOwnProperty('xAxis')) {
          this.optionsForecastingVisitorsChartArea.xAxis.categories = data.visitors.xAxis;
        }

        this.optionsForecastingVisitorsChartArea.series = [];

        /*** Past data ***/
        if (data.visitors.hasOwnProperty('past_data')) {
          let pastData = {name: 'Past data', data: []};
          /*** Initialize Past data ***/

          pastData.data = data.visitors.past_data;
          this.optionsForecastingVisitorsChartArea.series.push(pastData);
        } else {
          console.log('Past data error')
        }

        /*** Trend data ***/
        if (data.visitors.hasOwnProperty('trend')) {
          let trend = {name: 'Trend', data: []};
          /*** Initialize Trend data ***/

          trend.data = data.visitors.trend;
          this.optionsForecastingVisitorsChartArea.series.push(trend);
        } else {
          console.log('Trend data error')
        }

        /*** Forecast data ***/
        if (data.visitors.hasOwnProperty('forecast')) {
          let forecast = {name: 'Forecast', data: []};
          /*** Initialize forecast data ***/

          forecast.data = data.visitors.forecast;
          this.optionsForecastingVisitorsChartArea.series.push(forecast);
        } else {
          console.log('Trend data error')
        }

      }

      /***
       * Passerby 3 Charts
       **/
      if (data.hasOwnProperty('passerby')) {
        this.optionsForecastingPasserbyChartArea.title.text = 'Passerby';

        /*** xAxis ***/
        if (data.passerby.hasOwnProperty('xAxis')) {
          this.optionsForecastingPasserbyChartArea.xAxis.categories = data.passerby.xAxis;
        }

        this.optionsForecastingPasserbyChartArea.series = [];

        /*** Past data ***/
        if (data.passerby.hasOwnProperty('past_data')) {
          let pastData = {name: 'Past data', data: []};
          /*** Initialize Past data ***/

          pastData.data = data.passerby.past_data;
          this.optionsForecastingPasserbyChartArea.series.push(pastData);
        } else {
          console.log('Past data error')
        }

        /*** Trend data ***/
        if (data.passerby.hasOwnProperty('trend')) {
          let trend = {name: 'Trend', data: []};
          /*** Initialize Trend data ***/

          trend.data = data.passerby.trend;
          this.optionsForecastingPasserbyChartArea.series.push(trend);
        } else {
          console.log('Trend data error')
        }

        /*** Forecast data ***/
        if (data.passerby.hasOwnProperty('forecast')) {
          let forecast = {name: 'Forecast', data: []};
          /*** Initialize forecast data ***/

          forecast.data = data.passerby.forecast;
          this.optionsForecastingPasserbyChartArea.series.push(forecast);
        } else {
          console.log('Trend data error')
        }
      }
      this.readyCharts = true;
    }
  },

  computed: {
    pending() {
      return this.$store.getters['charts/pending']
    }
  }

};

export default ChartsMixin
