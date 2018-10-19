from django.views import View
from django.http import JsonResponse, HttpResponse, HttpResponseServerError
from django.conf import settings
from .query import *

import copy
import logging
import csv
import pandas as pd
from collections import OrderedDict
from datetime import date
from datetime import timedelta

class forecasting(View):
    def get(self, request):
        from fbprophet import Prophet
        forecast_period = 7
        dataFormat = {'xAxis':[], 'past_data':[], 'trend':[], 'forecast':[]}
        retInfo = {'connected':dataFormat, 'visitors':copy.deepcopy(dataFormat), 'passerby':copy.deepcopy(dataFormat)}
        endDate = (date.today() - timedelta(days=1)).isoformat()
        dates = []
        count_connected = []
        count_visitors = []
        count_passerby = []

        connected_date = requestServer.query.statistic("https://cisco-presence.unit.ua/api/presence/v1/connected/daily?"
                                                        + "siteId=" + GetQuery.aesUid
                                                        + "&startDate=" + settings.START_DATE
                                                        + "&endDate=" + endDate).json()
        visitors_date = requestServer.query.statistic("https://cisco-presence.unit.ua/api/presence/v1/visitor/daily?"
                                                        + "siteId=" + GetQuery.aesUid
                                                        + "&startDate=" + settings.START_DATE
                                                        + "&endDate=" + endDate).json()
        passerby_date = requestServer.query.statistic("https://cisco-presence.unit.ua/api/presence/v1/passerby/daily?"
                                                        + "siteId=" + GetQuery.aesUid
                                                        + "&startDate=" + settings.START_DATE
                                                        + "&endDate=" + endDate).json()

        for day, value in connected_date.items():
            dates.append(day)
            count_connected.append(value)
            count_visitors.append(visitors_date[day])
            count_passerby.append(passerby_date[day])

        for i in range(forecast_period):
            dates.append((date.today() + timedelta(days=i)).isoformat())
        for name, value in retInfo.items():
            retInfo[name]['xAxis'] = dates
        retInfo['connected']['past_data'] = count_connected
        retInfo['visitors']['past_data'] = count_visitors
        retInfo['passerby']['past_data'] = count_passerby

        csv_data_connected = open('./ConnectedData.csv', 'w')
        csv_data_visitors = open('./VisitorsData.csv', 'w')
        csv_data_passerby = open('./PasserbyData.csv', 'w')

        csvwriter_connected = csv.writer(csv_data_connected)
        csvwriter_visitors = csv.writer(csv_data_visitors)
        csvwriter_passerby = csv.writer(csv_data_passerby)

        csvwriter_connected.writerow(['ds', 'y'])
        csvwriter_visitors.writerow(['ds', 'y'])
        csvwriter_passerby.writerow(['ds', 'y'])

        for key, value in connected_date.items():
            csvwriter_connected.writerow([key, value])
            csvwriter_visitors.writerow([key, value])
            csvwriter_passerby.writerow([key, value])

        csv_data_connected.close()
        csv_data_visitors.close()
        csv_data_passerby.close()

        df_connected = pd.read_csv('./ConnectedData.csv')
        df_visitors = pd.read_csv('./VisitorsData.csv')
        df_passerby = pd.read_csv('./PasserbyData.csv')

        df_connected.head()
        df_visitors.head()
        df_passerby.head()

        connected = Prophet()
        connected.fit(df_connected)

        visitors = Prophet()
        visitors.fit(df_visitors)

        passerby = Prophet()
        passerby.fit(df_passerby)

        future_connected = connected.make_future_dataframe(periods=forecast_period)
        future_connected.tail()
        forecast_connected = connected.predict(future_connected)
        forecast_dict_connected = forecast_connected.to_dict()
        for key, value in forecast_dict_connected['trend'].items():
            retInfo['connected']['trend'].append(round(value))
            retInfo['connected']['forecast'].append(round(forecast_dict_connected['yhat'][key]))

        future_visitors = visitors.make_future_dataframe(periods=forecast_period)
        future_visitors.tail()
        forecast_visitors = visitors.predict(future_visitors)
        forecast_dict_visitors = forecast_visitors.to_dict()
        for key, value in forecast_dict_visitors['trend'].items():
            retInfo['visitors']['trend'].append(round(value))
            retInfo['visitors']['forecast'].append(round(forecast_dict_visitors['yhat'][key]))

        future_passerby = passerby.make_future_dataframe(periods=forecast_period)
        future_passerby.tail()
        forecast_passerby = passerby.predict(future_passerby)
        forecast_dict_passerby = forecast_passerby.to_dict()
        for key, value in forecast_dict_passerby['trend'].items():
            retInfo['passerby']['trend'].append(round(value))
            retInfo['passerby']['forecast'].append(round(forecast_dict_passerby['yhat'][key]))

        return JsonResponse(OrderedDict(retInfo))

