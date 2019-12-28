from django.shortcuts import render
from .models import Product
# Create your views here.
def Home(request):
    product = Product.objects.all().order_by('PName')
    title = 'Frozen'
    return render(request, 'Frozen/Page/homepage.html',{'title':title, 
                                                        'product':product,
                                                        })