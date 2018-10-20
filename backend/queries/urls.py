from django.urls import path

from . import views
from .data import getData

app_name = 'queries'

urlpatterns = [
    path('getData/', getData.as_view()),
]
