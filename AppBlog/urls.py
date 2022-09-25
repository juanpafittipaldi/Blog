from django.urls import path
from AppBlog.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login_request, name="login"),
    path("register/", register, name="register"),
    path("logout/", LogoutView.as_view(template_name="AppBlog/logout.html"), name="Logout"),

]