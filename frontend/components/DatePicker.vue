<template>
  <div>
    <v-menu
      :close-on-content-click="false"
      v-model="menu"
      :nudge-right="40"
      lazy
      transition="scale-transition"
      offset-y
      full-width
      max-width="290px"
      min-width="290px"
    >
      <v-text-field
        slot="activator"
        v-model="date"
        :label="labelText"
        prepend-icon="event"
        :error-messages="error_messages"
        box
        readonly
      ></v-text-field>
      <v-date-picker v-model="date" no-title @input="triggerEvent" :min="minDate" :max="currentDate"></v-date-picker>
    </v-menu>
  </div>
</template>

<script>
  export default {
    name: "DatePicker",
    props: {
      labelText: {
        type: String,
        default: 'date',
      },
      error_messages: {
        type: String
      }
    },
    data: () => ({
      date: '',
      menu: false,
      minDate: '2017-12-20',
      currentDate: null,
    }),
    created() {
      let currentDate = new Date();
      currentDate.setDate(currentDate.getDate() - 1);
      let day = currentDate.getDate().toString();
      day = day.length === 2 ? day : '0' + day;
      let month = (currentDate.getMonth() + 1).toString();
      month = month.length > 1 ? month : '0' + month;
      let year = currentDate.getFullYear();
      this.currentDate  = year + '-' + month + '-' + day;
    },
    methods: {
      triggerEvent() {
        this.menu = false;
        this.$emit('input', this.date);
      }
    }
  }
</script>

<style scoped>

</style>
