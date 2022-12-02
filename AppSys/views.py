from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import Cliente, Producto, Vendedor
from .forms import ClienteForm, ProductoForm, VendedorForm
from django.template import loader

# Create your views here.

def inicio(request):
    return render(request, 'inicio.html')

def clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes.html', {'clientes': clientes})

def productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos.html', {'productos': productos})

def vendedores(request):
    vendedores = Vendedor.objects.all()
    return render(request, 'vendedores.html', {'vendedores': vendedores})

def clientes(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            Cliente.objects.create(nombre=informacion['nombre'], pais=informacion['pais'], email=informacion['email'], telefono=informacion['telefono'])
            cliente=Cliente.objects.get(nombre=informacion['nombre'])
            cliente.save()
            return render (request, "/inicio.html", {"mensaje": "CLIENTE GUARDADO CORRECTAMENTE!!"})
    else:
        form = ClienteForm()
    return render(request, 'clientes.html', {'form': form})

