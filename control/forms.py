from django.forms import ModelForm
from control.models import *

class IngresosForm(ModelForm):
    class Meta:
        model = Ingresos
        fields = ('descripcion', 'monto')