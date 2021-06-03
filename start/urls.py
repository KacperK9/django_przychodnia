from django.contrib import admin
from django.urls import path

from start.views import f_start, f_info

urlpatterns = [
    path('', f_start),
    path('info', f_info)
]