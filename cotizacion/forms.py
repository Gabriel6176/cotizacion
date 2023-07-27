from django import forms
from django.views.generic import ListView
from .models import Ventana, Presupuesto, DetallePresupuesto

class VentanaForm(forms.ModelForm):
    class Meta:
        model = Ventana
        fields = ['ancho', 'alto', 'color', 'tipo']

class PresupuestoForm(forms.ModelForm):
    class Meta:
        model = Presupuesto
        fields = ['numero_presupuesto', 'cliente']

class ListaPresupuestos(ListView):
    model = Presupuesto
    template_name='lista_presupuestos.html'
    context_object_name='Presupuesto'        

class DetallePresupuestoForm(forms.ModelForm):
    class Meta:
        model = DetallePresupuesto
        fields = ['ventana','cantidad']
