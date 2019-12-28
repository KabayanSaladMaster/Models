from django.shortcuts import render
from .models import Product

# Create your views here.
def Home(request):
    product = Product.objects.all().order_by('PName')
    return render(request, 'NonFrozen/Page/homepage.html',{'product':product})