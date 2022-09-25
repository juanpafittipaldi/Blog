from http.client import HTTPResponse
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from AppBlog.forms import UserRegisterForm
from django.http import HttpResponse
# Create your views here.

def login_request(request):
    if request.method=="POST":
        form=AuthenticationForm(request.POST)
        if form.is_valid():
            usu=request.POST["username"]
            clave=request.POST["password"]
            usuario=authenticate(username=usu, password=clave)
            if usuario is not None:
                login(request, usuario)
                return render(request, "inicio.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "AppBlog/login.html",{"formulario":form, "mensaje":"usuario o contaseña incorrectos"})
        else:
            return render(request, "AppBlog/login.html",{"formulario":form, "mensaje":"usuario o contaseña incorrectos"})
    else:
        form=AuthenticationForm
        return render(request, "AppBlog/login.html",{"formulario":form})

def register(request):
    if request.method=="POST":
        form=UserRegisterForm(request.method)
        if form.is_valid():
            form.save()
            return render(request,"AppBlog/login.html",{"mensaje":"Usuario creado correctamente"})
        else:
            return render(request,"AppBlog/register.html",{"mensaje":"Error al registrarse, vuelva a intentarlo"})
    else:
        form=UserRegisterForm()
        return render(request, "AppBlog/register.html",{"formulario":form})