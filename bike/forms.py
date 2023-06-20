from django import forms
from .models import Bike
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Bike
from . import models


class ContactUsForm(forms.Form):
    name = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField(max_length=1000)

