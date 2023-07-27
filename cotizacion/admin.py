from django.contrib import admin
from .models import Ventana, Cliente, Insumo, Tipo, Color, Presupuesto, DetallePresupuesto, numerador_presupuesto

admin.site.register(Ventana)
admin.site.register(Cliente)
admin.site.register(Insumo)
admin.site.register(Tipo)
admin.site.register(Color)
"""
class DetallePresupuestoInline(admin.TabularInline):
    model = DetallePresupuesto

class PresupuestoAdmin(admin.ModelAdmin):
    inlines = [DetallePresupuestoInline]
    def save_model(self, request, obj, form, change):
        if not obj.numero_presupuesto:
            numerador_presupuesto(sender=Presupuesto, instance=obj)
        obj.save()
"""

admin.site.register(Presupuesto)
admin.site.register(DetallePresupuesto)
