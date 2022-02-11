from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, get_user_model
from users.forms import UserForm
from django.views.decorators.csrf import csrf_exempt
from users.models import *
from toilet.models import Bookmarks


# Create your views here.
@login_required
def profile(request, id):
    User = get_user_model()
    user = get_object_or_404(User, pk=id)
    context = {
        'user' :user
    }
    return render(request, 'users/profile.html', context)

def editProfile(request, id):
    User = get_user_model()
    user = get_object_or_404(User, pk=id)
    context = {
        'user' :user
    }
    return render(request, 'users/editProfile.html', context)

def editPassword(request, id):
    User = get_user_model()
    user = get_object_or_404(User, pk=id)
    context = {
        'user' :user
    }
    return render(request, 'users/editPassword.html', context)

@csrf_exempt
def join(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.errors:
            return render(request, 'users/join.html', {'form': form})
        if form.is_valid():
            user = form.save()
            login(request, user)
        return redirect('toilet:home')
    else:
        if request.user.is_authenticated:
            return redirect('toilet:home')
        form = UserForm()
        return render(request, 'users/join.html', {'form': form})

def bookmarks(request, id):
    bookmarks = Bookmarks.objects.filter(user = id)

    context = {
        'bookmarks' : bookmarks
    }
    return render(request, 'toilet/bookmarks.html', context)