from django import forms
<<<<<<< HEAD
from .models import Posteo

class PosteoForm(forms.ModelForm):

    class Meta:
        model = Posteo
        fields = ('titulo', 'contenido', 'imagen_posteo')

=======
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label="Ingrese Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repita Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_texts = {k:"" for k in fields}
>>>>>>> 590e3063093a3e4f85b7adfda9fc913212890b1c
