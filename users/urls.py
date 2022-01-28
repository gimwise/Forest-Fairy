from unicodedata import name
from django.urls import path
from django.contrib import admin

from . import views

app_name = 'users'

urlpatterns = [
    path("profile/", views.profile, name="profile"),
    path('login/', views.login, name='login'),
    path('join/', views.join, name='join'),
]