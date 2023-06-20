from .views import *
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', home, name="home"),
    path('login/', login_page, name="login_page"),
    path('register/', register_page, name="register_page"),
    path('bike_detail/<str:uid>/', views.bike_detail, name='bike_detail'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('contact-us/', views.contact, name='contact')
]


if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)


urlpatterns += staticfiles_urlpatterns()