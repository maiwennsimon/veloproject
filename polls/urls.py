from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [
    path("bikes/", views.index, name="bike-list"),
    path('bikes/<int:id>/', views.bike_detail, name="bike-detail"),
    path('contact-us/', views.contact, name='contact'),
    path('bikes/add/', views.bike_add, name='bike-add'),
    path('login', views.login_page, name='login'),
    path('register', views.create_account, name='register')
]