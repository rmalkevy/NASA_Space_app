<template>
  <v-jumbotron height="100%">
    <v-container fill-height>
      <v-layout align-center>
        <v-flex>

          <h3 class="display-3">Welcome to the CCMN project !</h3>

          <v-card>
            <v-card-media>
              <v-container fill-height fluid>
                <v-layout fill-height>
                  <v-flex>
                    <img src="~/static/heat_map_cisco_cmx.jpg"/>
                  </v-flex>
                </v-layout>
              </v-container>
            </v-card-media>
          </v-card>

          <p class="subheading ma-3">{{textProjectRequirements.description}}</p>

          <v-divider class="my-3"></v-divider>

          <h4 class="display-1 py-2">Requirements:</h4>

          <!--<v-divider class="my-2"></v-divider>-->
          <p class="subheading pl-4 my-2" v-html="textProjectRequirements.item_1"></p>

          <!--<v-divider class="my-2"></v-divider>-->
          <p class="subheading pl-4 my-2" v-html="textProjectRequirements.item_2"></p>

          <!--<v-divider class="my-2"></v-divider>-->
          <p class="subheading pl-4 my-2" v-html="textProjectRequirements.item_3"></p>
          <p class="subheading pl-5 ma-2" v-html="textProjectRequirements.sub_item_1"></p>

          <!--<v-divider class="my-2"></v-divider>-->
          <p class="subheading pl-4 my-2" v-html="textProjectRequirements.item_4"></p>

          <!--<v-divider class="my-2"></v-divider>-->
          <p class="subheading pl-4 my-2" v-html="textProjectRequirements.item_5"></p>

          <!--<v-divider class="my-2"></v-divider>-->
          <p class="subheading pl-4 my-2" v-html="textProjectRequirements.item_6"></p>

          <!--<v-divider class="my-2"></v-divider>-->
          <p class="subheading pl-4 my-2" v-html="textProjectRequirements.item_7"></p>
        </v-flex>
      </v-layout>
    </v-container>
  </v-jumbotron>
</template>

<script>

export default {
  name: 'index',
  data() {
    return {
      textProjectRequirements: {
        description: 'Imagine that you must create a special software for clients who use the Cisco Mobility\n' +
        'Services solution. Your client wants to know more about customers, for example, how\n' +
        'many of them returned, how much time they spend in some zones, floors or buildings.\n' +
        'Your potential client can be an owner of a conference hall, clothing store, business center,\n' +
        'shopping mall.',
        item_1: '<b>• Turn-key vertical-focused application, program or web service.</b></br>',
        item_2: '<b>• User-friendly interface.</b></br>',
        item_3: '<b>• Your program or app must display and visualize next information:</b></br>',
        sub_item_1: '<b>1.</b> How many devices connected to the wi-fi network;</br>' +
        '<b>2.</b> Floor map with designated location searching by the WiFi MAC address and ' +
        'xlogin, if available;</br>' +
        '<b>3.</b> Analytics and Presence (Sum of Connected Visitor, number of repeat visitors ' +
        'over all available ranges, dwell time);</br>' +
        '<b>4.</b> Forecasting number of visitors;</br>' +
        '<b>5.</b> Construct correlations between session duration and the day of the week; number ' +
        'of connections and the day of the week; and some other correlations at your choice;</br>' +
        '<b>6.</b> Floor congestion.</br>',
        item_4: '<b>• You need to encode requests. You must handle errors (btw, you need to do the ' +
        'error-handling of your code all the time) and write it in some files or tables.</b></br>',
        item_5: '<b>• Program or app must work in all 3 clusters and be detected in each floor (zone) you ' +
        'are located.</b></br>',
        item_6: '<b>• Display a message when you find some devices. Your program should adapt messages ' +
        'depending on where you (connected devices) are.</b></br>' +
        '<b>For example</b>: "Hi, @xlogin or mac: 00:00:2a:01:00:06 now is on the first floor." ' +
        'You can use programming languages, frameworks and libraries that you need. It will ' +
        'be better for you if you write this project using object-oriented modeling.</br>',
        item_7: '<b>Don’t hardcode data and information, for example, floor images, siteID ' +
        'etc. You program/app must take all actual information from RESTful API.</b>',
      }
    }
  },

}
</script>
