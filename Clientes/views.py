from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request,'home.html')

def promo(request):
    return render(request,'promociones.html')



