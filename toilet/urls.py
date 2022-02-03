from django.urls import path, include
from django.contrib import admin
from . import views

app_name = 'toilet'

urlpatterns = [
    path('',views.home,name='home'),
    path('add/',views.add, name='add'),
    path('<int:id>/',views.info, name='info'),
    path("intro/", views.intro, name="intro"),
    path('admin/', admin.site.urls),

    path('getJson/', views.getJson, name='getJson'),
]
