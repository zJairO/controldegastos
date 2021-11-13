from typing import List
from django.shortcuts import render
from django.http import request
from control.models import *
from django.views.generic import ListView

def Index(request):
    ingresos = Ingresos.objects.all()
    egresos = Egresos.objects.all()
    return render(request, 'index.html', {'ingresos': ingresos, 'egresos': egresos})

def IngresosList(request):
    ingresos = Ingresos.objects.all()
    return render(request, 'ingresos/list.html', {'ingresos': ingresos})

