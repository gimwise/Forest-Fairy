from django.urls import path
from django.contrib import admin

from . import views

app_name = 'home'

urlpatterns = [
    path('admin/', admin.site.urls),
]
