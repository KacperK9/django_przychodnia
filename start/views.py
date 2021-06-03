from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def f_start(request):
    return render(request, 'start.html')

def f_info(request):
    return render(request, 'info.html')