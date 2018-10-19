from django.views import View
from django.http import JsonResponse, HttpResponse, HttpResponseServerError
from .query import *
from .clients import Clients

import copy
import logging
from collections import OrderedDict

class getChartsInfoDaily(View):
    def __init__(self):
        self.data_charts = {'chart':{}, 'distribution':{}}
        self.retInfo = {'Proximity':copy.deepcopy(self.data_charts), 'Dwell Time':copy.deepcopy(self.data_charts), 'Repeat Visitors':copy.deepcopy(self.data_charts)}
    
    def get(self, request):
        if 'date' in request.GET:
            self.date = request.GET['date']
            self.retInfo['Proximity'] = self.__getProximity(self.date)
            self.retInfo['Dwell Time'] = self.__getDwellTime(self.date)
            self.retInfo['Repeat Visitors'] = self.__getRepeatVisitors(self.date)
            return JsonResponse(OrderedDict(self.retInfo))
        else:
            logging.error("getChartsInfoDaily get data = %s ! This data have wrong patern", request.GET)
            return HttpResponseServerError()

    def __getProximity(self, date):
        data_charts = copy.deepcopy(self.data_charts)
        data_charts['chart']['xAxis'] = []
        connected_chart = requestServer.query.statistic("https://cisco-presence.unit.ua/api/presence/v1/connected/hourly?"
                                                + "siteId=" + GetQuery.aesUid
                                                + "&date=" + date).json()
        visitors_chart = requestServer.query.statistic("https://cisco-presence.unit.ua/api/presence/v1/visitor/hourly?"
                                                + "siteId=" + GetQuery.aesUid
                                                + "&date=" + date).json()
        passerby_chart = requestServer.query.statistic("https://cisco-presence.unit.ua/api/presence/v1/passerby/hourly?"
                                                + "siteId=" + GetQuery.aesUid
                                                + "&date=" + date).json()
        data_charts['chart']['connected'] = []
        data_charts['chart']['visitors'] = []
        data_charts['chart']['passerby'] = []
        for key, value in connected_chart.items():
            data_charts['chart']['xAxis'].append(key)
            data_charts['chart']['connected'].append(value)
        for key, value in visitors_chart.items():
            data_charts['chart']['visitors'].append(value)
        for key, value in passerby_chart.items():
            data_charts['chart']['passerby'].append(value)
        count_connected = requestServer.query.statistic("https://cisco-presence.unit.ua/api/presence/v1/connected/count?"
                                                + "siteId=" + GetQuery.aesUid
                                                + "&date=" + date).json()
        count_passerby = requestServer.query.statistic("https://cisco-presence.unit.ua/api/presence/v1/passerby/count?"
                                                + "siteId=" + GetQuery.aesUid
                                                + "&date=" + date).json()
        count_visitors = requestServer.query.statistic("https://cisco-presence.unit.ua/api/presence/v1/visitor/total?"
                                                + "siteId=" + GetQuery.aesUid
                                                + "&startDate=" + date
                                                + "&endDate=" + date).json()
        all_visitors = count_visitors + count_passerby
        count_probing = all_visitors - count_connected
        data_charts['distribution']['Connected'] = count_connected
        data_charts['distribution']['Probing'] = count_probing
        data_charts['distribution']['Visitors'] = count_visitors
        data_charts['distribution']['Passerby'] = count_passerby
        return data_charts

    def __getDwellTime(self, date):
        data_charts = copy.deepcopy(self.data_charts)
        data_charts['chart']['xAxis'] = []
        replace_names = {   "FIVE_TO_THIRTY_MINUTES": '5-30 mins',
                            "THIRTY_TO_SIXTY_MINUTES": '30-60 mins',
                            "ONE_TO_FIVE_HOURS": '1-5 hours',
                            "FIVE_TO_EIGHT_HOURS": '5-8 hours',
                            "EIGHT_PLUS_HOURS": '8+ hours'}
        dwell_time = requestServer.query.statistic("https://cisco-presence.unit.ua/api/presence/v1/dwell/hourly?"
                                                    + "siteId=" + GetQuery.aesUid
                                                    + "&date=" + date).json()
        dwell_distribution = requestServer.query.statistic("https://cisco-presence.unit.ua/api/presence/v1/dwell/count?"
                                                            + "siteId=" + GetQuery.aesUid
                                                            + "&date=" + date).json()
        for key, value in dwell_time.items():
            for old_name, new_name in replace_names.items():
                dwell_time[key][new_name] = dwell_time[key].pop(old_name)
        for old_name, new_name in replace_names.items():
                dwell_distribution[new_name] = dwell_distribution.pop(old_name)
        for key, value in dwell_time['0'].items():
            data_charts['chart'][key] = []
        for key, value in dwell_time.items():
            data_charts['chart']['xAxis'].append(key)
            for name, data in value.items():
                data_charts['chart'][name].append(data)
        data_charts['distribution'] = dwell_distribution
        return data_charts

    def __getRepeatVisitors(self, date):
        data_charts = copy.deepcopy(self.data_charts)
        data_charts['chart'] = {'xAxis': []}

        repeat_visitors = requestServer.query.statistic("https://cisco-presence.unit.ua/api/presence/v1/repeatvisitors/daysummary?"
                                                + "siteId=" + GetQuery.aesUid
                                                + "&date=" + date).json()
        for key, value in repeat_visitors['DAILY']['hourlyCounts'].items():
            data_charts['chart']['xAxis'].append(key)
        for key, value in repeat_visitors.items():
            if key != "YESTERDAY":
                data_charts['chart'][key] = []

        for name, data in repeat_visitors.items():
            if name != "YESTERDAY":
                for key, value in data['hourlyCounts'].items():
                    data_charts['chart'][name].append(value)
        count_repeat_visitors = requestServer.query.statistic("https://cisco-presence.unit.ua/api/presence/v1/repeatvisitors/count?"
                                                        + "siteId=" + GetQuery.aesUid
                                                        + "&date=" + date).json()
        for key, value in count_repeat_visitors.items():
            if key != "YESTERDAY":
                data_charts['distribution'][key] = value
        return data_charts


class getChartsInfoRange(View):
    def __init__(self):
        self.data_charts = {'chart':{}, 'distribution':{}}
        self.retInfo = {'Proximity':copy.deepcopy(self.data_charts), 'Dwell Time':copy.deepcopy(self.data_charts), 'Repeat Visitors':copy.deepcopy(self.data_charts)}
    
    def get(self, request):
        if ('startDate' in request.GET) and ('endDate' in request.GET):
            startDate = request.GET['startDate']
            endDate = request.GET['endDate']
            self.retInfo['Proximity'] = self.__getProximityRange(startDate, endDate)
            self.retInfo['Dwell Time'] = self.__getDwellTimeRange(startDate, endDate)
            self.retInfo['Repeat Visitors'] = self.__getRepeatVisitorsRange(startDate, endDate)
            return JsonResponse(OrderedDict(self.retInfo))
        else:
            logging.error("getChartsInfoRange get data = %s ! This data have wrong patern", request.GET)
            return HttpResponseServerError()


    def __getProximityRange(self, startDate, endDate):
        data_charts = copy.deepcopy(self.data_charts)
        data_charts['chart']['xAxis'] = []
        data_charts['chart']['connected'] = []
        data_charts['chart']['visitors'] = []
        data_charts['chart']['passerby'] = []

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

        for key, value in connected_chart.items():
            data_charts['chart']['xAxis'].append(key)
            data_charts['chart']['connected'].append(value)
        for key, value in visitors_chart.items():
            data_charts['chart']['visitors'].append(value)
        for key, value in passerby_chart.items():
            data_charts['chart']['passerby'].append(value)

        count_connected = requestServer.query.statistic("https://cisco-presence.unit.ua/api/presence/v1/connected/total?"
                                                        + "siteId=" + GetQuery.aesUid
                                                        + "&startDate=" + startDate
                                                        + "&endDate=" + endDate).json()
        count_passerby = requestServer.query.statistic("https://cisco-presence.unit.ua/api/presence/v1/passerby/total?"
                                                        + "siteId=" + GetQuery.aesUid
                                                        + "&startDate=" + startDate
                                                        + "&endDate=" + endDate).json()
        count_visitors = requestServer.query.statistic("https://cisco-presence.unit.ua/api/presence/v1/visitor/total?"
                                                        + "siteId=" + GetQuery.aesUid
                                                        + "&startDate=" + startDate
                                                        + "&endDate=" + endDate).json()

        all_visitors = count_visitors + count_passerby
        count_probing = all_visitors - count_connected

        data_charts['distribution']['Connected'] = count_connected
        data_charts['distribution']['Probing'] = count_probing
        data_charts['distribution']['Visitors'] = count_visitors
        data_charts['distribution']['Passerby'] = count_passerby

        return data_charts


    def __getDwellTimeRange(self, startDate, endDate):
        data_charts = copy.deepcopy(self.data_charts)
        data_charts['chart']['xAxis'] = []
        replace_names = { "FIVE_TO_THIRTY_MINUTES": '5-30 mins',
                          "THIRTY_TO_SIXTY_MINUTES": '30-60 mins',
                          "ONE_TO_FIVE_HOURS": '1-5 hours',
                          "FIVE_TO_EIGHT_HOURS": '5-8 hours',
                          "EIGHT_PLUS_HOURS": '8+ hours' }

        dwell_time = requestServer.query.statistic("https://cisco-presence.unit.ua/api/presence/v1/dwell/daily?"
                                                    + "siteId=" + GetQuery.aesUid
                                                    + "&startDate=" + startDate
                                                    + "&endDate=" + endDate).json()
        dwell_distribution = requestServer.query.statistic("https://cisco-presence.unit.ua/api/presence/v1/dwell/count?"
                                                            + "siteId=" + GetQuery.aesUid
                                                            + "&startDate=" + startDate
                                                            + "&endDate=" + endDate).json()

        for key, value in dwell_time.items():
            for old_name, new_name in replace_names.items():
                dwell_time[key][new_name] = dwell_time[key].pop(old_name)
        for old_name, new_name in replace_names.items():
                dwell_distribution[new_name] = dwell_distribution.pop(old_name)

        for key, value in dwell_time[startDate].items():
            data_charts['chart'][key] = []
        for key, value in dwell_time.items():
            data_charts['chart']['xAxis'].append(key)
            for name, data in value.items():
                data_charts['chart'][name].append(data)
        data_charts['distribution'] = dwell_distribution

        return data_charts


    def __getRepeatVisitorsRange(self, startDate, endDate):
        data_charts = copy.deepcopy(self.data_charts)
        data_charts['chart'] = {'xAxis': []}

        repeat_visitors = requestServer.query.statistic("https://cisco-presence.unit.ua/api/presence/v1/repeatvisitors/daily?"
                                                + "siteId=" + GetQuery.aesUid
                                                + "&startDate=" + startDate
                                                + "&endDate=" + endDate).json()

        for key, value in repeat_visitors.items():
            data_charts['chart']['xAxis'].append(key)
        for key, value in repeat_visitors[startDate].items():
            if key != "YESTERDAY":
                data_charts['chart'][key] = []
        for date, data in repeat_visitors.items():
            for key, value in data.items():
                if key != "YESTERDAY":
                    data_charts['chart'][key].append(value)

        count_repeat_visitors = requestServer.query.statistic("https://cisco-presence.unit.ua/api/presence/v1/repeatvisitors/count?"
                                                        + "siteId=" + GetQuery.aesUid
                                                        + "&startDate=" + startDate
                                                        + "&endDate=" + endDate).json()
        for key, value in count_repeat_visitors.items():
            if key != "YESTERDAY":
                data_charts['distribution'][key] = value
        return data_charts