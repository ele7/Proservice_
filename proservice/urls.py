from django.urls import path
from . import views
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage

urlpatterns = [

    path('', views.index, name='index'),      
    path('home/', views.home, name='home'),  
    path('portafolio/', views.portafolio, name='portafolio'),
    path('contact/', views.contact, name='contact'),
    path("favicon.ico", RedirectView.as_view(
        url=staticfiles_storage.url("favicon.ico"),
        permanent=True
    )),
]


