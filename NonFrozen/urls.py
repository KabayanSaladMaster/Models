from django.urls import path
from . import views

app_name = 'NonFrozen'

urlpatterns = [
    path('', views.Home, name='Home'),
]