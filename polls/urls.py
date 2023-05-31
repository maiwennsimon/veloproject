from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("bikes/", views.index, name="bike-list"),
    path('bikes/<int:id>/', views.bike_detail, name="bike-detail"),
    path('contact-us/', views.contact, name='contact'),
    path('bikes/add/', views.bike_add, name='bike-add'),
    path('photo/upload/', views.photo_upload, name='photo_upload'),
    path('', views.login_page, name='login'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



