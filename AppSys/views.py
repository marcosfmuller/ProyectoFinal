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

def clientesform(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            nombre=informacion["nombre"]
            pais=informacion["pais"]
            email=informacion["email"]
            telefono=informacion["telefono"]
            cliente=Cliente(nombre=nombre, pais=pais, email=email, telefono=telefono)
            cliente.save()
            return render (request, "clientes.html", {"mensaje": "CLIENTE GUARDADO CORRECTAMENTE!"})
    else:
        formulario = ClienteForm()
    return render(request, 'clientes_form.html', {'form': formulario})

def productosform(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            nombre=informacion["nombre"]
            precio=informacion["precio"]
            stock=informacion["stock"]
            producto=Producto(nombre=nombre, precio=precio, stock=stock)
            producto.save()
            return render (request, "productos.html", {"mensaje": "PRODUCTO GUARDADO CORRECTAMENTE!"})
    else:
        formulario = ProductoForm()
    return render(request, 'productos_form.html', {'form': formulario})

def vendedoresform(request):
    if request.method == 'POST':
        form = VendedorForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            nombre=informacion["nombre"]
            mercado=informacion["mercado"]
            email=informacion["email"]
            telefono=informacion["telefono"]
            vendedor=Vendedor(nombre=nombre, mercado=mercado, email=email, telefono=telefono)
            vendedor.save()
            return render (request, "vendedores.html", {"mensaje": "VENDEDOR GUARDADO CORRECTAMENTE!"})
    else:
        formulario = VendedorForm()
    return render(request, 'vendedores_form.html', {'form': formulario})

def clienteslist(request):
    clientes = Cliente.objects.all
    return render(request, 'clientes_list.html', {'clientes': clientes})

def productoslist(request):
    productos = Producto.objects.all
    return render(request, 'productos_list.html', {'productos': productos})

def vendedoreslist(request):
    vendedores = Vendedor.objects.all
    return render(request, 'vendedores_list.html', {'vendedores': vendedores})

def clientesbuscar(request):
    return render(request, 'clientes_buscar.html')

def clientesresbuscar(request):
    if request.GET["pais"]:
        pais=request.GET["pais"]
        clientes=Cliente.objects.filter(pais__iexact=pais)
        return render(request, 'clientes_res_buscar.html', {'clientes': clientes})
    else:
        return render(request, "clientes_list.html", {"mensaje": "Ingrese un pais!"})

def productosbuscar(request):
    return render(request, 'productos_buscar.html')

def productosresbuscar(request):
    if request.GET["nombre"]:
        nombre=request.GET["nombre"]
        productos=Producto.objects.filter(nombre__icontains=nombre)
        return render(request, 'productos_res_buscar.html', {'productos': productos})
    else:
        return render(request, "productos_list.html", {"mensaje": "Ingrese un nombre!"})

def vendedoresbuscar(request):
    return render(request, 'vendedores_buscar.html')

def vendedoresresbuscar(request):
    if request.GET["nombre"]:
        nombre=request.GET["nombre"]
        vendedores=Vendedor.objects.filter(nombre__icontains=nombre)
        return render(request, 'vendedores_res_buscar.html', {'vendedores': vendedores})
    else:
        return render(request, "vendedores_list.html", {"mensaje": "Ingrese un nombre!"})
