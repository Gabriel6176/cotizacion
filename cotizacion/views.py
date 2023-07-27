from django.shortcuts import render, redirect, get_object_or_404
from .models import Ventana, Cliente, Presupuesto, DetallePresupuesto
from .forms import VentanaForm, PresupuestoForm, DetallePresupuestoForm


# CREAR

# Vista para crear un nuevo ventana
def crear_ventana(request):
    if request.method == 'POST':
        form = VentanaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_ventana')  # Redirige a la lista de ventana para deespués de crear uno nuevo
    else:
        form = VentanaForm()
    return render(request, 'crear_ventana.html', {'form': form})

# Vista para crear un nuevo Presupuesto 
def crear_presupuesto(request):
    if request.method == 'POST':
        form = PresupuestoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_presupuestos')
    else:
        form = PresupuestoForm()
    return render(request, 'crear_presupuesto.html', {'form':form})        
'''
def crear_presupuesto(request):
    if request.method == 'POST':
        form = PresupuestoForm(request.POST)
        if form.is_valid():
            presupuesto = form.save()
            return redirect('detalle_presupuesto', presupuesto_id=presupuesto.id)
    else:
        form = PresupuestoForm()
    return render(request, 'crear_presupuesto.html', {'form': form})
'''
# Vista para crear un nuevo DetallePresupuesto asociado a una Presupuesto existente
def crear_detalle_presupuesto(request, presupuesto_id):
    presupuesto = DetallePresupuesto.objects.get(id=presupuesto_id)
    if request.method == 'POST':
        form = DetallePresupuestoForm(request.POST)
        if form.is_valid():
            detalle_presupuesto = form.save(commit=False)
            detalle_presupuesto.presupuesto = presupuesto
            detalle_presupuesto.save()
            return redirect('detalle_presupuesto', presupuesto_id=presupuesto.id)
    else:
        form = DetallePresupuestoForm()
    return render(request, 'crear_detalle_presupuesto.html', {'form': form, 'presupuesto': presupuesto})

# LEER
# Vista para mostrar la lista de Ventanas
def lista_ventanas(request):
    ventana = Ventana.objects.all()
    return render(request, 'lista_ventana.html', {'ventana': ventana})

# Vista para mostrar la lista de Presupuestos
def lista_presupuestos(request):
    presupuestos = Presupuesto.objects.all()
    return render(request, 'lista_presupuestos.html', {'presupuestos': presupuestos})

# Vista para mostrar el detalle de una Presupuesto con sus Detalles de Presupuesto asociados
def detalle_presupuesto(request, presupuesto_id):
    presupuesto = get_object_or_404(Presupuesto, id=presupuesto_id)
    detalles = DetallePresupuesto.objects.filter(presupuesto=presupuesto)
    return render(request, 'detalle_presupuesto.html', {'presupuesto': presupuesto, 'detalles': detalles})

def detalle_ventana(request, ventana_id):
    ventana = get_object_or_404(Ventana, id=ventana_id)
    detalles = Ventana.objects.filter(ventana=ventana)
    return render(request, 'detalle_ventana.html', {'ventana':ventana, 'detalles':detalles})
# ACTUALIZAR

# Vista para editar un Item existente
def editar_ventana(request, ventana_id):
    ventana = get_object_or_404(Ventana, id=ventana_id)
    if request.method == 'POST':
        form = VentanaForm(request.POST, instance=ventana)
        if form.is_valid():
            form.save()
            return redirect('lista_ventanas')
    else:
        form = VentanaForm(instance=ventana)
    return render(request, 'editar_ventana.html', {'form': form})

# Vista para editar una Presupuesto existente
def editar_presupuesto(request, presupuesto_id):
    presupuesto = get_object_or_404(Presupuesto, id=presupuesto_id)
    if request.method == 'POST':
        form = PresupuestoForm(request.POST, instance=presupuesto)
        if form.is_valid():
            form.save()
            return redirect('detalle_presupuesto', presupuesto_id=presupuesto.id)
    else:
        form = PresupuestoForm(instance=presupuesto)
    return render(request, 'editar_presupuesto.html', {'form': form, 'presupuesto': presupuesto})

# Vista para editar un DetallePresupuesto existente
def editar_detalle_presupuesto(request, detalle_presupuesto_id):
    detalle_presupuesto = get_object_or_404(DetallePresupuesto, id=detalle_presupuesto_id)
    presupuesto = detalle_presupuesto.presupuesto
    if request.method == 'POST':
        form = DetallePresupuestoForm(request.POST, instance=detalle_presupuesto)
        if form.is_valid():
            form.save()
            return redirect('detalle_presupuesto', presupuesto_id=presupuesto.id)
    else:
        form = DetallePresupuestoForm(instance=detalle_presupuesto)
    return render(request, 'editar_detalle_presupuesto.html', {'form': form, 'presupuesto': presupuesto})


# ELIMINAR

# Vista para eliminar un ventana
def eliminar_ventana(request, ventana_id):
    ventana = get_object_or_404(Ventana, id=ventana_id)
    ventana.delete()
    return redirect('lista_ventanas')

# Vista para eliminar una Presupuesto
def eliminar_presupuesto(request, presupuesto_id):
    presupuesto = get_object_or_404(Presupuesto, id=presupuesto_id)
    presupuesto.delete()
    return redirect('lista_presupuestos')

# Vista para eliminar un DetallePresupuesto
def eliminar_detalle_presupuesto(request, detalle_presupuesto_id):
    detalle_presupuesto = get_object_or_404(DetallePresupuesto, id=detalle_presupuesto_id)
    presupuesto_id = detalle_presupuesto.presupuesto.id
    detalle_presupuesto.delete()
    return redirect('detalle_presupuesto', presupuesto_id=presupuesto_id)







"""
def lista_ventanas(request):
    ventanas = Ventana.objects.all()
    return render(request, 'lista_ventanas.html', {'ventanas': ventanas})

def crear_presupuesto(request):
    if request.method == 'POST':
        cliente_id = request.POST['cliente']
        cliente = Cliente.objects.get(pk=cliente_id)
        ancho = request.POST['ancho']
        alto = request.POST['alto']
        tipo = request.POST['tipo']
        ventana = Ventana.objects.create(ancho=ancho, alto=alto, tipo=tipo, cliente=cliente)
        ventana.save()
        return redirect('lista_ventanas')

    clientes = Cliente.objects.all()
    return render(request, 'crear_presupuesto.html', {'clientes': clientes})
"""



'''
def home(request):
    presupuesto=Presupuesto.objects.filter(is_completed=False).order_by('nombre_cliente')
    context={
        'presupuesto': presupuesto,
    }
    return render(request, 'home.html', context)

def cliente(request):
    cliente=Cliente.objects.all()
    context={
        'cliente': cliente
    }
    return render(request, 'home.html', context)
    '''