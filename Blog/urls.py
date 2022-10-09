from django.contrib import admin
from django.urls import path, include
<<<<<<< HEAD
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('AppBlog.urls')),

=======
from Blog.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("AppBlog/", include("AppBlog.urls")),
    path("",inicio,name="inicio")
>>>>>>> 590e3063093a3e4f85b7adfda9fc913212890b1c
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)