
from django.urls import path
from .views import Home,Registro,Login,Mensaje,Registrar,promo
urlpatterns=[
    path('Home/',Home,name='home'),
    path('Registro/',Registro),
    path('Login/',Login),
    path('Mensaje/',Mensaje), 
    path('Registrar/',Registrar),
    path('promociones/',promo,name='promo'), 
]