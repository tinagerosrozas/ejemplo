from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from . models import Producto
# Create your views here.
def home (request):
    return HttpResponse ("Hola Mundo")
class ProductListView(ListView):
    model = Producto
class ProductDetailView(DetailView):
    model = Producto