"""projekt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from start import views

urlpatterns = [
    path('', include('start.urls')),
    path('admin/', admin.site.urls),
    path('start/', include('start.urls')),

    path('dodaj_lek/', views.addLek, name="dodaj_lek"),
    path('edytuj_lek/<str:pk>/', views.editLek, name="edytuj_lek"),
    path('usun_lek/<str:pk>/', views.deleteLek, name="usun_lek"),
    
    path('dodaj_pacjent/', views.addPacjent, name="dodaj_pacjent"),
    path('edytuj_pacjent/<str:pk>/', views.editPacjent, name="edytuj_pacjent"),
    path('usun_pacjent/<str:pk>/', views.deletePacjent, name="usun_pacjent"),
    
    path('dodaj_choroba/', views.addChoroba, name="dodaj_choroba"),
    path('edytuj_choroba/<str:pk>/', views.editChoroba, name="edytuj_choroba"),
    path('usun_choroba/<str:pk>/', views.deleteChoroba, name="usun_choroba"),
    
    path('dodaj_lekarz/', views.addLekarz, name="dodaj_lekarz"),
    path('edytuj_lekarz/<str:pk>/', views.editLekarz, name="edytuj_lekarz"),
    path('usun_lekarz/<str:pk>/', views.deleteLekarz, name="usun_lekarz"),

    path('dodaj_recepta/', views.addRecepta, name="dodaj_recepta"),
    path('edytuj_recepta/<str:pk>/', views.editRecepta, name="edytuj_recepta"),
    path('usun_recepta/<str:pk>/', views.deleteRecepta, name="usun_recepta"),
]
