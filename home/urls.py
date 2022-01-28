from unicodedata import name
from django.urls import path
from django.contrib import admin

from . import views

app_name = 'home'

urlpatterns = [
    path('',views.home,name='home'),
    path('add/',views.add, name='add'),
    path('admin/', admin.site.urls),
]
