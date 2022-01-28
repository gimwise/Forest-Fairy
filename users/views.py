from django.shortcuts import render

# Create your views here.
def profile(req):
    return render(req,'users/profile.html')
    
def login(req):
    return render(req,'users/login.html')
    
def join(req):
    return render(req,'users/join.html')
    