from django.views import View
from django.http import JsonResponse, HttpResponse, HttpResponseServerError
from django.conf import settings
from .query import *
from .clients import Clients


import copy
import logging
from collections import OrderedDict
from datetime import date
from datetime import timedelta
import dateutil.parser

class getCorrelations(View):
    def __init__(self):
        self.startDate = settings.START_DATE
        self.endDate = (date.today() - timedelta(days=1)).isoformat()
        self.data_charts = {'chart':{}, 'distribution':{}}
        self.days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        self.retInfo = { 'Proximity':copy.deepcopy(self.data_charts), 'Dwell Time':copy.deepcopy(self.data_charts),'Repeat Visitors':copy.deepcopy(self.data_charts)}
    
    def get(self, request):
        self.retInfo['Proximity'] = self.__getCorrelationProximity(self.startDate, self.endDate)
        self.retInfo['Dwell Time'] = self.__getCorrelationDwellTime(self.startDate, self.endDate)
        self.retInfo['Repeat Visitors'] = self.__getCorrelationRepeatVisitors(self.startDate, self.endDate)
        return JsonResponse(OrderedDict(self.retInfo))


    def __getCorrelationProximity(self, startDate, endDate):
        data_charts = copy.deepcopy(self.data_charts)
        data_charts['chart']['xAxis'] = self.days
        data_charts['distribution']['xAxis'] = self.days
        data_charts['chart']['connected'] = []
        data_charts['chart']['visitors'] = []
        data_charts['chart']['passerby'] = []
        data_charts['distribution']['connected'] = []
        data_charts['distribution']['visitors'] = []
        data_charts['distribution']['passerby'] = []

        connected_chart = requestServer.query.statistic("https://cisco-presence.unit.ua/api/presence/v1/connected/daily?"
                                                + "siteId=" + GetQuery.aesUid
                                                + "&startDate=" + startDate
                                                + "&endDate=" + endDate).json()
        visitors_chart = requestServer.query.statistic("https://cisco-presence.unit.ua/api/presence/v1/visitor/daily?"
                                                + "siteId=" + GetQuery.aesUid
                                                + "&startDate=" + startDate
                                                + "&endDate=" + endDate).json()
        passerby_chart = requestServer.query.statistic("https://cisco-presence.unit.ua/api/presence/v1/passerby/daily?"
                                                + "siteId=" + GetQuery.aesUid
                                                + "&startDate=" + startDate
                                                + "&endDate=" + endDate).json()

        sumByDays = {}
        contsDays = {}

        for i in range(7):
            sumByDays[i] = 0
            contsDays[i] = 0
        avarangeCounts = []
        for key, value in connected_chart.items():
            sumByDays[dateutil.parser.parse(key).weekday()] += value
            contsDays[dateutil.parser.parse(key).weekday()] += 1
        for key, value in sumByDays.items():
            avarangeCounts.append(round(value / contsDays[key]))
        data_charts['chart']['connected'] = avarangeCounts
        data_charts['distribution']['connected'] = avarangeCounts

        for i in range(7):
            sumByDays[i] = 0
            contsDays[i] = 0
        avarangeCounts = []
        for key, value in visitors_chart.items():
            sumByDays[dateutil.parser.parse(key).weekday()] += value
            contsDays[dateutil.parser.parse(key).weekday()] += 1
        for key, value in sumByDays.items():
            avarangeCounts.append(round(value / contsDays[key]))
        data_charts['chart']['visitors'] = avarangeCounts
        data_charts['distribution']['visitors'] = avarangeCounts

        for i in range(7):
            sumByDays[i] = 0
            contsDays[i] = 0
        avarangeCounts = []
        for key, value in passerby_chart.items():
            sumByDays[dateutil.parser.parse(key).weekday()] += value
            contsDays[dateutil.parser.parse(key).weekday()] += 1
        for key, value in sumByDays.items():
            avarangeCounts.append(round(value / contsDays[key]))
        data_charts['chart']['passerby'] = avarangeCounts
        data_charts['distribution']['passerby'] = avarangeCounts

        return data_charts


    def __getCorrelationDwellTime(self, startDate, endDate):
        data_charts = copy.deepcopy(self.data_charts)
        data_charts['chart']['xAxis'] = self.days
        data_charts['distribution']['xAxis'] = self.days

        replace_names = { "FIVE_TO_THIRTY_MINUTES": '5-30 mins',
                          "THIRTY_TO_SIXTY_MINUTES": '30-60 mins',
                          "ONE_TO_FIVE_HOURS": '1-5 hours',
                          "FIVE_TO_EIGHT_HOURS": '5-8 hours',
                          "EIGHT_PLUS_HOURS": '8+ hours' }
        for key, time_range in replace_names.items():
            data_charts['chart'][time_range] = []
            data_charts['distribution'][time_range] = []

        dwell_time = requestServer.query.statistic("https://cisco-presence.unit.ua/api/presence/v1/dwell/daily?"
                                            + "siteId=" + GetQuery.aesUid
                                            + "&startDate=" + startDate
                                            + "&endDate=" + endDate).json()
        for date, name in dwell_time.items():
            for old_name, new_name in replace_names.items():
                dwell_time[date][new_name] = dwell_time[date].pop(old_name)

        sumByDays = {}
        contsDays = {}
        avarangeCounts = {}
        for key, value in replace_names.items():
            sumByDays[value] = {}
            contsDays[value] = {}
            avarangeCounts[value] = []
        for key, value in replace_names.items():
            for i in range(7):
                sumByDays[value][i] = 0
                contsDays[value][i] = 0

        for date, time_range in dwell_time.items():
            for range_name, value in time_range.items():
                sumByDays[range_name][dateutil.parser.parse(date).weekday()] += value
                contsDays[range_name][dateutil.parser.parse(date).weekday()] += 1
        for key, data in sumByDays.items():
            for day, value in data.items():
                avarangeCounts[key].append(round(value / contsDays[key][day]))

        for key, value in avarangeCounts.items():
            data_charts['chart'][key] = value
            data_charts['distribution'][key] = value

        return data_charts


    def __getCorrelationRepeatVisitors(self, startDate, endDate):
        data_charts = copy.deepcopy(self.data_charts)
        data_charts['chart']['xAxis'] = self.days
        data_charts['distribution']['xAxis'] = self.days
        time_ranges = ['DAILY', 'WEEKLY', 'OCCASIONAL', 'FIRST_TIME']

        for i in range(len(time_ranges)):
            data_charts['chart'][time_ranges[i]] = []
            data_charts['distribution'][time_ranges[i]] = []


        repeat_visitors = requestServer.query.statistic("https://cisco-presence.unit.ua/api/presence/v1/repeatvisitors/daily?"
                                                + "siteId=" + GetQuery.aesUid
                                                + "&startDate=" + startDate
                                                + "&endDate=" + endDate).json()

        sumByDays = {}
        contsDays = {}
        avarangeCounts = {}
        for i in range(len(time_ranges)):
            sumByDays[time_ranges[i]] = {}
            contsDays[time_ranges[i]] = {}
            avarangeCounts[time_ranges[i]] = []

        for i in range(len(time_ranges)):
            for j in range(7):
                sumByDays[time_ranges[i]][j] = 0
                contsDays[time_ranges[i]][j] = 0

        for date, time_range in repeat_visitors.items():
            for range_name, value in time_range.items():
                if range_name != 'YESTERDAY':
                    sumByDays[range_name][dateutil.parser.parse(date).weekday()] += value
                    contsDays[range_name][dateutil.parser.parse(date).weekday()] += 1
        for key, data in sumByDays.items():
            for day, value in data.items():
                avarangeCounts[key].append(round(value / contsDays[key][day]))

        for key, value in avarangeCounts.items():
            data_charts['chart'][key] = value
            data_charts['distribution'][key] = value

        return data_charts