from django.contrib import admin
from django.urls import path
from . import views

app_name= 'cotizacion'

urlpatterns = [
    path('ventanas/', views.lista_ventanas, name='lista_ventanas'),
    path('crear_presupuesto/', views.crear_presupuesto, name='crear_presupuesto'),
    
    # URLs para Ventanas
    path('ventas/', views.lista_ventanas, name='lista_ventanas'),
    path('ventanas/crear/', views.crear_ventana, name='crear_ventana'),
    path('ventanas/editar/<int:ventana_id>/', views.editar_ventana, name='editar_ventana'),
    path('ventanas/eliminar/<int:ventana_id>/', views.eliminar_ventana, name='eliminar_ventana'),

    # URLs para Presupuestos
    path('presupuestos/', views.lista_presupuestos, name='lista_presupuestos'),
    path('presupuestos/crear/', views.crear_presupuesto, name='crear_presupuesto'),
    path('presupuestos/editar/<int:presupuesto_id>/', views.editar_presupuesto, name='editar_presupuesto'),
    path('presupuestos/eliminar/<int:presupuesto_id>/', views.eliminar_presupuesto, name='eliminar_presupuesto'),

    # URLs para Detalle de Presupuestos
    path('presupuestos/detalle/<int:presupuesto_id>/', views.detalle_presupuesto, name='detalle_presupuesto'),
    path('presupuestos/detalle/<int:presupuesto_id>/agregar/', views.crear_detalle_presupuesto, name='crear_detalle_presupuesto'),
    path('presupuestos/detalle/editar/<int:detalle_presupuesto_id>/', views.editar_detalle_presupuesto, name='editar_detalle_presupuesto'),
    path('presupuestos/detalle/eliminar/<int:detalle_presupuesto_id>/', views.eliminar_detalle_presupuesto, name='eliminar_detalle_presupuesto'),
]

