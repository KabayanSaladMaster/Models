from django.shortcuts import render
from .data.mainCss import Boostrap4

# Create your views here.
def Home(request):
    title='Home'
    PageData = {
        'title':title,
    }
    return render(request, 'Home/Page/homepage.html', PageData)