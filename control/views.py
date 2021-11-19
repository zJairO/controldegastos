from typing import List
from django.shortcuts import render, redirect, get_object_or_404 
from django.http import request, Http404
from control.models import *
from control.forms import *


def Index(request):
    ingresos = Ingresos.objects.all()
    egresos = Egresos.objects.all()
    return render(request, 'index.html', {'ingresos': ingresos, 'egresos': egresos})

def IngresosList(request):
    ingresos = Ingresos.objects.all()
    return render(request, 'ingresos/list.html', {'ingresos': ingresos})

def IngresosCreate(request):
    if request.method == "POST":
        form = IngresosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/ingresos')
    else:
        form = IngresosForm()
        return render(request, 'ingresos/create.html', {'form': form})

def IngresosDelete(request, _id):
    try:
        ingreso = get_object_or_404(Ingresos,id =_id)
    except Exception:
        raise Http404('No existe')
 
    if request.method == 'POST':
        ingreso.delete()
        return redirect('/ingresos')
    else:
        return render(request, 'ingresos/delete.html')