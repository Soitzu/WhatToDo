from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.redirect_homepage, name='redirect'),
    path('loginpage/', views.login_user, name='loginpage'),
    path('logout/', views.logout_user, name='logout'),
    path('homepage/', views.homepage, name='homepage'),
]