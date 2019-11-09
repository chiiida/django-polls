from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.signals import user_logged_out
from django.contrib.auth.forms import UserCreationForm

def index(request):
    """Redirects to polls index page."""
    return HttpResponseRedirect(reverse('polls:index'))

def successful_logout_message(sender, user, request, **kwargs):
    messages.info(request, 'You have successfully been signed out.')

def signup(request):
    """Register a new user."""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_passwd = form.cleaned_data.get('password')
            user = authenticate(username=username,password=raw_passwd)
            login(request, user)
            return redirect('polls:index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

user_logged_out.connect(successful_logout_message)