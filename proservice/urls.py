from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),      
    path('home/', views.home, name='home'),  
    path('portafolio/', views.portafolio, name='portafolio'),
    path('contact/', views.contact, name='contact'), 
]



