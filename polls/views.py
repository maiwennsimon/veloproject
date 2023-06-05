import hashlib

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .utils import send_mail_to_client
from django.contrib import sessions
# Create your views here.
from django.http import HttpResponse
from polls.models import Bike, CustomUser
from polls.forms import BikeAddForm, ContactUsForm, LoginForm, RegistrationForm


def index(request):
    bikes = Bike.objects.all()
    return render(request, 'polls/bikes.html', {'bikes': bikes})


def bike_detail(request, id):
    bike = Bike.objects.get(id=id)
    if request.method == 'POST':
        bike.reserved = True
        bike.delete()
    return render(request, 'polls/bike_detail.html', {'bike': bike})


def bike_add(request):
    if request.method == 'POST':
        form = BikeAddForm(request.POST)
        if form.is_valid():
            bike = form.save()
    else:
        form = BikeAddForm()
    return render(request, 'polls/bike_add.html', {'form': form})


def contact(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['name']
            message = form.cleaned_data['message']
            email = form.cleaned_data['email']
            send_mail_to_client(subject, message, email)
        return redirect('/polls/bikes')
    else:
        form = ContactUsForm()
    return render(request, 'polls/FormContact.html', {'form': form})


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
                return redirect("/polls/bikes")
            else:
                message = 'Identifiants invalides.'
    return render(request, 'polls/login.html', context={'form': form})


def create_account(request):
    form = RegistrationForm()
    if request.session.get('username'):
        return render(request, 'polls/register.html', context={'form': form})
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            try:
                CustomUser.objects.get(username=username)
                return render(request, 'polls/register.html', context={'form': form})
            except CustomUser.DoesNotExist:
                pass

            # Use Django's built-in authentication system to handle password hashing
            user = form.save()
            login(request, user)
            message = f'Bonjour, {user.username}! Votre compte a été créé.'
            return redirect('/polls/bikes')  # Replace 'home' with your desired URL or view name

    return render(request, 'polls/register.html', context={'form': form})
