from django.shortcuts import render

# Create your views here.
def Home(request):
    title='Home'
    PageData = {
        'title':title,
    }
    return render(request, 'Home/homepage.html', PageData)