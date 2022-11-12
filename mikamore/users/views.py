from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from users.forms import *


class SignIn(CreateView):
    form_class = UserCreationForm
    template_name = "users/sign_in.html"
    success_url = reverse_lazy("root")


class SignUp(CreateView):
    form_class = UserSignUpForm
    template_name = "users/sign_up.html"
    success_url = reverse_lazy("root")
