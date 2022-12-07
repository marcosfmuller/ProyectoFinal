from django.urls import path
from AppSys.views import *

urlpatterns = [
    path("", inicio, name="inicio"),
    path("clientes/", clientes, name="clientes"),
    path("clientesform/", clientesform, name="clientesform"),
    path("clienteslist/", clienteslist, name="clienteslist"),
    path("clientesbuscar/", clientesbuscar, name="clientesbuscar"),
    path("clientesresbuscar/", clientesresbuscar, name="clientesresbuscar"),

    path("productos/", productos, name="productos"),
    path("productosform/", productosform, name="productosform"),
    path("productoslist/", productoslist, name="productoslist"),
    path("productosbuscar/", productosbuscar, name="productosbuscar"),
    path("productosresbuscar/", productosresbuscar, name="productosresbuscar"),
   

    path("vendedores/", vendedores, name="vendedores"),
    path("vendedoresform/", vendedoresform, name="vendedoresform"),
    path("vendedoreslist/", vendedoreslist, name="vendedoreslist"),
    path("vendedoresbuscar/", vendedoresbuscar, name="vendedoresbuscar"),
    path("vendedoresresbuscar/", vendedoresresbuscar, name="vendedoresresbuscar"),
    
    

]