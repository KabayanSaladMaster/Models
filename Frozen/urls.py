from django.urls import path
from . import views
app_name = 'Frozen'

urlpatterns = [
    path('',views.Home, name='Home')
]