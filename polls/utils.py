from polls.models import Bike
import time
from django.core.mail import send_mail
from django.conf import settings


def send_mail_to_client(subject, message, email):
    sujet = f"Contact from {subject}"
    recipient = ["yan.meddour2001@gmail.com"]
    send_mail(sujet, message,"<email>", recipient)
