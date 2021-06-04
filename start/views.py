from django.shortcuts import render
from django.http import HttpResponse

from django.db import models

from start.models import *
from start.lekarze import *


# Create your views here.

def f_start(request):
    pacjenci = Pacjent.objects.all()
    lekarze = Lekarz.objects.all()
    leki = Lek.objects.all()
    recepty = Recepta.objects.all()
    objawy = Objaw.objects.all()
    choroby = Choroba.objects.all()
    wizyty = Wizyta.objects.all()
    dyzury = Dyzur.objects.all()
    return render(request, 'start.html', {'pacjenci_all':pacjenci, 'lekarze_all': lekarze,
    'leki_all': leki, 'recepta_all': recepty, 'objawy_all': objawy,
    'choroby_all': choroby, 'wizyty_all': wizyty, 'dyzury_all': dyzury
    })



'''
def f_info(request, id=0):
    pacjenci = Pacjent.objects.all()
    return render(request, 'info.html', {'pacjenci_all':pacjenci})

def f_lekarze(request):
        formularz = LekarzForm(request.POST or None)
        lekarze_all = Lekarz.objects.all()
        if formularz.is_valid():
            formularz.save()
        return render(request, 'lekarze.html', {'form': formularz, 'lekarze': lekarze_all})
'''
#Lek

def addLek(request):
    form = LekForm()

    if request.method == 'POST':
        form = LekForm(request.POST)
        if form.is_valid():
            form.save() 
            return f_start(request)
    context = {'form': form}
    return render(request, 'lek_form.html', context)

def editLek(request, pk):
    lek = Lek.objects.get(id=pk)
    form = LekForm(instance=lek)

    if request.method == 'POST':
        form = LekForm(request.POST, instance=lek)
        if form.is_valid():
            form.save() 
            return f_start(request)
    
    context = {'form': form}
    return render(request, 'lek_form.html', context)

def deleteLek(request, pk):
    lek = Lek.objects.get(id=pk)
    delLink = 'usun_lek'
    if request.method=='POST':
        lek.delete()
        return f_start(request)
    context = {'item':lek, 'delLink': delLink}
    return render(request, 'delete.html', context)

#pacjent

def addPacjent(request):
    form = PacjentForm()

    if request.method == 'POST':
        form = PacjentForm(request.POST)
        if form.is_valid():
            form.save() 
            return f_start(request)
    context = {'form': form}
    return render(request, 'pacjent_form.html', context)

def editPacjent(request, pk):
    pacjent = Pacjent.objects.get(id=pk)
    form = PacjentForm(instance=pacjent)

    if request.method == 'POST':
        form = PacjentForm(request.POST, instance=pacjent)
        if form.is_valid():
            form.save() 
            return f_start(request)
    
    context = {'form': form}
    return render(request, 'pacjent_form.html', context)

def deletePacjent(request, pk):
    pacjent = Pacjent.objects.get(id=pk)
    delLink = 'usun_pacjent'
    if request.method=='POST':
        pacjent.delete()
        return f_start(request)
    context = {'item':pacjent, 'delLink': delLink}
    return render(request, 'delete.html', context)


# choroba

def addChoroba(request):
    form = ChorobaForm()

    if request.method == 'POST':
        form = ChorobaForm(request.POST)
        if form.is_valid():
            form.save() 
            return f_start(request)
    context = {'form': form}
    return render(request, 'choroba_form.html', context)

def editChoroba(request, pk):
    choroba = Choroba.objects.get(id=pk)
    form = ChorobaForm(instance=choroba)

    if request.method == 'POST':
        form = ChorobaForm(request.POST, instance=choroba)
        if form.is_valid():
            form.save() 
            return f_start(request)
    
    context = {'form': form}
    return render(request, 'choroba_form.html', context)

def deleteChoroba(request, pk):
    choroba = choroba.objects.get(id=pk)
    delLink = 'usun_choroba'
    if request.method=='POST':
        Choroba.delete()
        return f_start(request)
    context = {'item':choroba, 'delLink': delLink}
    return render(request, 'delete.html', context)

#lekarz

def addLekarz(request):
    form = LekarzForm()

    if request.method == 'POST':
        form = LekarzForm(request.POST)
        if form.is_valid():
            form.save() 
            return f_start(request)
    context = {'form': form}
    return render(request, 'lekarz_form.html', context)

def editLekarz(request, pk):
    lekarz = Lekarz.objects.get(id=pk)
    form = LekarzForm(instance=lekarz)

    if request.method == 'POST':
        form = LekarzForm(request.POST, instance=lekarz)
        if form.is_valid():
            form.save() 
            return f_start(request)
    
    context = {'form': form}
    return render(request, 'lekarz_form.html', context)

def deleteLekarz(request, pk):
    lekarz = Lekarz.objects.get(id=pk)
    delLink = 'usun_lekarz'
    if request.method=='POST':
        Lekarz.delete()
        return f_start(request)
    context = {'item':lekarz, 'delLink': delLink}
    return render(request, 'delete.html', context)


#recepta

def addRecepta(request):
    form = ReceptaForm()

    if request.method == 'POST':
        form = ReceptaForm(request.POST)
        if form.is_valid():
            form.save() 
            return f_start(request)
    context = {'form': form}
    return render(request, 'recepta_form.html', context)

def editRecepta(request, pk):
    recepta = Recepta.objects.get(id=pk)
    form = ReceptaForm(instance=recepta)

    if request.method == 'POST':
        form = ReceptaForm(request.POST, instance=recepta)
        if form.is_valid():
            form.save() 
            return f_start(request)
    
    context = {'form': form}
    return render(request, 'recepta_form.html', context)

def deleteRecepta(request, pk):
    lekarz = Recepta.objects.get(id=pk)
    delLink = 'usun_lekarz'
    if request.method=='POST':
        recepta.delete()
        return f_start(request)
    context = {'item':recepta, 'delLink': delLink}
    return render(request, 'delete.html', context)

#objaw

def addObjaw(request):
    form = ObjawForm()

    if request.method == 'POST':
        form = ObjawForm(request.POST)
        if form.is_valid():
            form.save() 
            return f_start(request)
    context = {'form': form}
    return render(request, 'objaw_form.html', context)

def editObjaw(request, pk):
    objaw = Objaw.objects.get(id=pk)
    form = ObjawForm(instance=recepta)

    if request.method == 'POST':
        form = ObjawForm(request.POST, instance=objaw)
        if form.is_valid():
            form.save() 
            return f_start(request)
    
    context = {'form': form}
    return render(request, 'objaw_form.html', context)

def deleteObjaw(request, pk):
    lekarz = Objaw.objects.get(id=pk)
    delLink = 'usun_objaw'
    if request.method=='POST':
        objaw.delete()
        return f_start(request)
    context = {'item':objaw, 'delLink': delLink}
    return render(request, 'delete.html', context)




#objaw

def addWizyta(request):
    form = WizytaForm()

    if request.method == 'POST':
        form = ObjawForm(request.POST)
        if form.is_valid():
            form.save() 
            return f_start(request)
    context = {'form': form}
    return render(request, 'objaw_form.html', context)

def editObjaw(request, pk):
    objaw = Objaw.objects.get(id=pk)
    form = ObjawForm(instance=recepta)

    if request.method == 'POST':
        form = ObjawForm(request.POST, instance=objaw)
        if form.is_valid():
            form.save() 
            return f_start(request)
    
    context = {'form': form}
    return render(request, 'objaw_form.html', context)

def deleteObjaw(request, pk):
    lekarz = Objaw.objects.get(id=pk)
    delLink = 'usun_objaw'
    if request.method=='POST':
        objaw.delete()
        return f_start(request)
    context = {'item':objaw, 'delLink': delLink}
    return render(request, 'delete.html', context)





















