from django import forms
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User, AbstractUser
from django.contrib.auth.forms import UserCreationForm
from .models import Hobby, Person

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
   

class PersonCreationForm(forms.ModelForm):
    class Meta:
        model = Person
        exclude = ['userID']
        #fields = ['userID','image', 'city', 'email', 'dob', 'hobbies']
        labels = {
        'userID': "Enter your username",
        'image': "Choose your image",
        'city':"City",
        'email':"Email",
        'dob':"Date of Birth",
        'hobbies':"Choose your hobbies"
        }
        #widgets = {
        #    'userID': forms.HiddenInput(),
        #}

    #userID = forms.CharField(max_length=20)
    #image = forms.ImageField()
    #city = forms.CharField(max_length=150)
    #email  = forms.CharField(max_length=150)
    #dob = forms.DateField()
    #hobbies = forms.ModelMultipleChoiceField(queryset=Hobby.objects.all())

    


