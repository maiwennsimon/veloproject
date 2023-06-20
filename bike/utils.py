from .models import Bike
import time
from django.core.mail import send_mail
from django.conf import settings
from django import forms



def send_mail_to_client(subject, message, email):
    recipient = ['bikes.fi93@gmail.com']
    email_body = f"Message de {email}\n\n{message}"
    send_mail(subject, email_body, email, recipient, fail_silently=False)
