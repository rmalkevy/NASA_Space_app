from django.urls import path

from . import views
from .floors import getUsersByFloor, getImageFloor, getMaps
from .charts import getChartsInfoDaily, getChartsInfoRange
from .correlation import getCorrelations
from .forecasting import forecasting

app_name = 'queries'

urlpatterns = [
    path('getMaps/', getMaps.as_view()),
    path('getUsersByFloor/', getUsersByFloor.as_view()),
    path('getImageFloor/', getImageFloor.as_view()),
    path('getChartsInfoDaily/', getChartsInfoDaily.as_view()),
    path('getChartsInfoRange/', getChartsInfoRange.as_view()),
    path('getCorrelations/', getCorrelations.as_view()),
    path('forecasting/', forecasting.as_view())
]
