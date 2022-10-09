from django.urls import path
<<<<<<< HEAD
from . import views
from .models import Posteo

urlpatterns = [
    path('', views.lista_posteos, name='lista_posteos'),
    path('posteo/<int:pk>/', views.detalle_posteo, name='detalle_posteo'),
    path('posteo/nuevo/', views.posteo_nuevo, name='posteo_nuevo'),
    path('posteo/<int:pk>/editar/', views.editar_posteo, name='editar_posteo'),
    path('borradores/', views.posteo_borradores, name='posteo_borradores'),
    path('posteo/<pk>/publicar/', views.publicar_posteo, name='publicar_posteo'),
    path('posteo/<pk>/eliminar/', views.eliminar_posteo, name='eliminar_posteo'),
]


=======
from AppBlog.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login_request, name="login"),
    path("register/", register, name="register"),
    path("logout/", LogoutView.as_view(template_name="AppBlog/logout.html"), name="Logout"),

]
>>>>>>> 590e3063093a3e4f85b7adfda9fc913212890b1c
