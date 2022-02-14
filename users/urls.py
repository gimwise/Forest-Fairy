from unicodedata import name
from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views

from . import views

app_name = 'users'

urlpatterns = [
    path("profile/<str:id>/", views.profile, name="profile"),
    path("editProfile/", views.editProfile, name="editProfile"),
    path("editPassword/", views.editPassword, name="editPassword"),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('join/', views.join, name='join'),
]