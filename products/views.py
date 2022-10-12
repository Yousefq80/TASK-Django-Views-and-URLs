from itertools import product
from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

# Create your views here.
def get_home(request):
    return HttpResponse(f"<h1>Welcome</h1>")

def get_product(request,product_id):
    p= Product.objects.get(id=product_id)
    return HttpResponse(p)