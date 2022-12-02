from django.urls import path
from AppSys.views import *

urlpatterns = [
    path("", inicio, name="inicio"),
    path("clientes/", clientes, name="clientes"),
    path("productos/", productos, name="productos"),
    path("vendedores/", vendedores, name="vendedores"),
    

]