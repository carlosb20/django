from django.urls import path
from .views import index,contados

urlpatterns = [
    path('',index,name='index'),
    path('contado/<int:pk>',contados,name='contados'),
    
    ]
