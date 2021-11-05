from django.urls import path
from .views import index,contado

urlpatterns = [
    path('',index),
    path('contado',contado),
    
    ]
