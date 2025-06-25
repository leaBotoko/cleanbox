from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class InscriptionForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Adresse email")

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
