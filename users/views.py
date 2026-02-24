from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from django.template.context_processors import request
from django.views import View

from users.forms import UserCreateForm, UserUpdateForm


# Create your views here.


class RegisterView(View):
    def get(self, request):
        form = UserCreateForm()
        context = {
            "form":form
        }
        return render(request, 'users/register.html', context)
    def post(self, request):

        form = UserCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')
        else:
            context = {
                "form":form
            }
            return render(request, 'users/register.html', context)


class LoginView(View):
    def get(self, request):
        login_form = AuthenticationForm()
        return render(request, "users/login.html", {"login_form":login_form})


    def post(self, request):
        login_form = AuthenticationForm(data=request.POST)

        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            messages.success(request, "You have successfully logged in.")
            return redirect("books:list")
        else:
            return render(request, "users/login.html", {"login_form":login_form})

class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "users/profile.html", {"user":request.user})


class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.info(request, "You have successfully logged out.")
        return redirect("landing_page")

class ProfileUpdateView(LoginRequiredMixin, View):
    def get(self, request):
        user_update_form = UserUpdateForm(instance=request.user)
        return render(request, "users/profile_update.html", {"form":user_update_form})


    def post(self, request):
        user_update_form = UserUpdateForm(instance=request.user, data=request.POST)
        if user_update_form.is_valid():
            user_update_form.save()
            messages.success(request, "You have successfully update your profile")

            return redirect("users:profile")

        return render(request, "users/profile_edit.html", {'form':user_update_form})