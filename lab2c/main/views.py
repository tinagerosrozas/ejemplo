from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from . models import *
# Create your views here.
def home (request):
    return HttpResponse ("Hola Mundo. Te encuentras en la página de inicio de Linio Express")
class ProductListView(ListView):
    model = Producto
class ProductDetailView(DetailView):
    model = Producto

class ProveedorListView(ListView):
  model = Proveedor

class ProveedorDetailView(DetailView):
  model = Proveedor

class CategoriaListView(ListView):
  model = Categoria

class CategoriaDetailView(DetailView):
  model = Categoria

class LocalizacionListView(ListView):
  model = Localizacion

class LocalizacionDetailView(DetailView):
  model = Localizacion