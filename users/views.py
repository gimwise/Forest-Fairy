from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, get_user_model, update_session_auth_hash
from users.forms import UserForm, CustomPasswordChangeForm, CustomUserChangeForm
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView as AuthPasswordChangeView
from django.urls import reverse_lazy
from users.models import *
from toilet.models import Bookmarks

class PasswordChangeView(LoginRequiredMixin, AuthPasswordChangeView):
    success_url = reverse_lazy('editPassword')
    template_name =  'users/editPassword.html'
    form_class = CustomPasswordChangeForm

    def form_valid(self, form):
        messages.success(self.request, '암호를 변경하였습니다.')
        return super().form_valid(form)

# Create your views here.
@login_required
def profile(request, id):
    User = get_user_model()
    user = get_object_or_404(User, pk=id)
    context = {
        'user' :user
    }
    return render(request, 'users/profile.html', context)

@login_required
def editProfile(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
        return redirect('/')
    else:
        form = CustomUserChangeForm(instance=request.user)
        return render(request, 'users/editProfile.html', {'form': form})

editPassword = PasswordChangeView.as_view()

@method_decorator(csrf_exempt)
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


