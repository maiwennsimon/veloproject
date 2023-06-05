from django import forms
from polls.models import Bike, CustomUser
from django.contrib.auth.forms import UserCreationForm


class ContactUsForm(forms.Form):
    name = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField(max_length=1000)


class BikeAddForm(forms.ModelForm):
    class Meta:
        model = Bike
        fields = '__all__'


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)


class RegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2']

