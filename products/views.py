from itertools import product
from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

# Create your views here.
def get_home(request):
    return render(request,"home.html")

def get_product(request,product_id):
    product= Product.objects.get(id=product_id)
   
    context = {"product":
      {
        "name":product.name,
    
    "price":product.price
      }
              }
    return render(request,"product-detail.html",context)

def get_products(request):
    products= Product.objects.all()
    list=[]
    for i in products:
        list.append({"name":i.name,"price":i.price})
    context={"products":list}
    return render(request,"product-list.html",context)