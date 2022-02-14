from django.urls import path, include
from django.contrib import admin
from . import views

app_name = 'toilet'

urlpatterns = [
<<<<<<< HEAD
    path('', views.home, name='home'),
    path('add/', views.add, name='add'),
    path('<int:id>/edit/', views.edit, name="edit"),
    path('<int:id>/', views.info, name='info'),
=======
    path('',views.home,name='home'),
    path('admin/', admin.site.urls),
    path('add/',views.add, name='add'),
    path('<int:id>/',views.info, name='info'),
>>>>>>> real/main
    path("intro/", views.intro, name="intro"),
    path('addBookmark/<int:toilet_id>/', views.addBookmark, name="addBookmark"),
    path('delBookmark/<int:toilet_id>/', views.delBookmark, name="delBookmark"),
    path('bookmarks/<str:id>/', views.bookmarks, name="bookmarks"),
    path('getJson/', views.getJson, name='getJson'),
    path('getScore/', views.getScore, name='getScore'),
<<<<<<< HEAD
]
=======
    path('myComments/', views.myComments, name='myComments')
]
>>>>>>> real/main
