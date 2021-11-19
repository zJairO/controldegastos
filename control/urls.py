from django.urls import path
from control.views import *

urlpatterns = [
    path('', IngresosList, name='ingresos'),
    path('create', IngresosCreate, name="ingresos_create"),
    path('delete/<int:_id>', IngresosDelete, name="ingresos_delete")
]
