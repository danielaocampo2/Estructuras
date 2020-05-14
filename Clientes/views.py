from django.shortcuts import render
from Clientes.models import Cliente
# Create your views here.
def Home(request):
    return render(request,'Home.html')
def Registro(request):
    return render(request,'formulario.html')
def Login(request):
    return render(request,'login.html')
def Mensaje(request):
    return render(request,'mensaje.html')
def Registrar(request):
    if request.method=="POST":
        nombre=request.POST["nombre"]
        numero=request.POST["numero"]
        cumpleanos=request.POST["fecha"]
        email=request.POST["correo"]
        contrasena=request.POST["contrasena"]
        cli=Cliente(nombre=nombre,numero_contacto=numero,email=email,cumpleanos=cumpleanos, contrasena=contrasena)
        cli.save()
        return render(request,'Home.html')
    return render(request,'formulario.html') 
def promo(request):
    return render(request,'promociones.html')  



