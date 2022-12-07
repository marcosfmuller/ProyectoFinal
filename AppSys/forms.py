from django import forms

class ClienteForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    pais = forms.CharField(max_length=20)
    email = forms.EmailField()
    telefono = forms.CharField(max_length=20)

class ProductoForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    precio = forms.DecimalField(max_digits=10, decimal_places=2)
    stock = forms.IntegerField()

class VendedorForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    mercado = forms.CharField(max_length=20)
    email = forms.EmailField()
    telefono = forms.CharField(max_length=20)