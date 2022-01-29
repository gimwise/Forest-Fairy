from django.shortcuts import render

# Create your views here.

def home(req):
    return render(req, 'home.html')

def add(req):
    return render(req, 'toilet/add.html')

def info(req):
    return render(req, 'toilet/info.html')

def intro(req):
    return render(req, 'toilet/intro.html')