from django.shortcuts import render
from django.contrib.auth import login,logout
from django.urls import reverse_lazy
from .forms import UserCreateForm
from django.views.generic import CreateView
# Create your views here.

class SignUpView(CreateView):
	form_class = UserCreateForm
	template_name = 'accounts/signup.html'
	success_url =reverse_lazy('accounts:login')
