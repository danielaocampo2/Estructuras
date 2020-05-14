from django.urls import path
from .views import Home
from .views import promo

urlpatterns=[
    path('',Home,name='home'), 
    path('promociones/',promo,name='promo'), 
]