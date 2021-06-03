from django.shortcuts import render
from django.http import HttpResponse

from django.db import models

from start.models import Pacjent
# Create your views here.

def f_start(request):
    return render(request, 'start.html')

def f_info(request):
    pacjenci = Pacjent.objects.all()
    return render(request, 'info.html', {'pacjenci_all':pacjenci})