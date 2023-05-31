from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .utils import send_mail_to_client
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from polls.models import Bike
from polls.forms import ContactUsForm, BikeAddForm, LoginForm
from django.conf import settings
from . import forms, models
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login



def index(request):
    bikes = Bike.objects.all()
    bikes.all()
    return render(request, 'polls/bikes.html', {'bikes': bikes})


def bike_detail(request, id):
    bike = Bike.objects.get(id=id)
    return render(request, 'polls/bike_detail.html', {'bike': bike})



def contact(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['name']
            message = form.cleaned_data['message']
            email = form.cleaned_data['email']
            current_site = get_current_site(request)
            domain = current_site.domain

            send_mail_to_client(subject, message, email, domain)
            return redirect('/polls/bikes')
    else:
        form = ContactUsForm()
    return render(request, 'polls/FormContact.html', {'form': form})


def bike_add(request):
    if request.method == 'POST':
        form = BikeAddForm(request.POST)
        if form.is_valid():
            bike = form.save()
    else:
        form = BikeAddForm()
    return render(request, 'polls/bike_add.html', {'form': form})



def photo_upload(request):
    form = forms.PhotoForm()
    if request.method == 'POST':
        form = forms.PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            # set the uploader to the user before saving the model
            photo.uploader = request.user
            # now we can save
            photo.save()
            return redirect('home')
    return render(request, 'polls/photo_upload.html', context={'form': form})


@login_required
def home(request):
    photos = models.Photo.objects.all()
    return render(request, 'polls/home.html', context={'photos': photos})


def login_page(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                message = f'Bonjour, {user.username}! Vous êtes connecté.'
            else:
                message = 'Identifiants invalides.'
    return render(request, 'polls/login.html', context={'form': form})