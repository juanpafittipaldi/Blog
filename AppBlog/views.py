<<<<<<< HEAD
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .forms import PosteoForm
from .models import Posteo
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

#Read
def lista_posteos(request):
    posteos = Posteo.objects.filter(fecha_publicado__lte=timezone.now()).order_by('-fecha_creado')
    return render(request, 'html/lista_posteos.html', {'posteos':posteos})

#Read
def detalle_posteo(request, pk):
    posteo = get_object_or_404(Posteo, pk=pk)
    return render(request, 'html/detalle_posteo.html', {'posteo': posteo})

@login_required

#Create
def posteo_nuevo(request):
    if request.method == "POST":
        form = PosteoForm(request.POST, request.FILES)
        if form.is_valid():
            posteo = form.save(commit=False)
            posteo.autor = request.user
            posteo.save()
            return redirect('detalle_posteo', pk=posteo.pk)
    else:
        form = PosteoForm()
    return render(request, 'html/editar_posteo.html', {'form': form})

@login_required
#Update
def editar_posteo(request, pk):
    posteo = get_object_or_404(Posteo, pk=pk)
    if request.method == "POST":
        form = PosteoForm(request.POST, request.FILES,instance=posteo)
        if form.is_valid():
            posteo = form.save(commit=False)
            posteo.autor = request.user
            posteo.save()
            return redirect('detalle_posteo', pk=posteo.pk)
    else:
        form = PosteoForm(instance=posteo)  
    return render(request, 'html/editar_posteo.html', {'form': form, 'posteo':posteo})

@login_required
#Read
def posteo_borradores(request):
    posteos = Posteo.objects.filter(fecha_publicado__isnull=True).order_by('-fecha_creado')
    return render(request, 'html/posteo_borradores.html', {'posteos': posteos})
@login_required
#Create
def publicar_posteo(request, pk):
    posteo = get_object_or_404(Posteo, pk=pk)
    if posteo.imagen_posteo: 
        posteo.publicar()
        return redirect('lista_posteos')
    else: 
        return editar_posteo(request, pk)
@login_required
#Delete
def eliminar_posteo(request, pk):
    posteo = get_object_or_404(Posteo, pk=pk)
    posteo.delete()
    return redirect('lista_posteos')
    
=======
from http.client import HTTPResponse
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from AppBlog.forms import UserRegisterForm

# Create your views here.

def login_request(request):
    if request.method== "POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usu=request.POST["username"]
            clave=request.POST["password"]
            usuario=authenticate(username=usu, password=clave)
            if usuario is not None:
                login(request, usuario)
                return render(request, "AppBlog/logueado.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "AppBlog/login.html",{"formulario":form, "mensaje":"usuario o contaseña incorrectos 2"})
        else:
            return render(request, "AppBlog/login.html",{"formulario":form, "mensaje":"usuario o contaseña incorrectos"})
    else:
        form=AuthenticationForm
        return render(request, "AppBlog/login.html",{"formulario":form})

def register(request):
    if request.method == "POST":
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            formlogin=AuthenticationForm()
            return render(request,"AppBlog/login.html",{"formulario":formlogin,"mensaje":"Usuario creado correctamente"})
        else:
            form=UserRegisterForm()
            return render(request,"AppBlog/register.html",{"formulario":form,"mensaje":"Error al registrarse, vuelva a intentarlo"})
    else:
        form=UserRegisterForm()
        return render(request, "AppBlog/register.html",{"formulario":form})
>>>>>>> 590e3063093a3e4f85b7adfda9fc913212890b1c
