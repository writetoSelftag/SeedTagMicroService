from django.contrib import admin
from django.urls import path, include

from src.radars.views import RadarViewSet

urlpatterns = [

    path('radar', RadarViewSet.as_view({
        'post': 'scan',
    })),

]
