from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home/home.html')

def add(request):
    return render(request, 'home/add.html')