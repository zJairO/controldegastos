from django.urls import path
from control.views import *

urlpatterns = [
    path('', IngresosList, name='ingresos'),
]
