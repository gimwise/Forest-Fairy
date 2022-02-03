from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def add(request):
    return render(request, 'toilet/add.html')

def about(request):
    return render(request, 'toilet/about.html')