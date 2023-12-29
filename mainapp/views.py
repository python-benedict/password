from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib.auth import login, logout
from django.contrib.auth.models import User

from django.core.mail import send_mail
from django.conf import settings
from .models import UserProfile
import random
import string
# Create your views here.

@login_required
def dashboard(request):
    return render(request, 'registration/dashboard.html', {'section':'dashboard'})


# def register(request):
#     if request.method == 'POST':
#         user_form = UserRegistrationForm(request.post)
#         if user_form.is_valid():
#             new_user = user_form.save(commit=False)
#             new_user.set_password(
#                 user_form.cleaned_data['password'])
#             user_form.save()
#             return render(request, 'registration/register_done.html', {'new_user':new_user})
#     else:
#         user_form = UserRegistrationForm()
#     return render(request, 'registration/register.html', {'user_form':user_form})


# def generate_random_password():
#     return ''.join(random.choices(string.ascii_letters + string.digits, k=12 ))

def generate_random_password():
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choices(characters, k=12))

# def register_user(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             email = form.cleaned_data['email']
#             password = generate_random_password()

#             # Save user data to the database
#             # user = UserProfile(username=username, email=email, password=password)
#             user = User.objects.create_user(username=username, email=email, password=password)
#             user.save()

#             # Send registration email
#             subject = 'Account Created'
#             message = f'An account has been created for you.Your username: {username}, email: {email}, Your password is {password}, Please follow this link to login: {settings.BASE_URL}/login/'
#             from_email = settings.DEFAULT_FROM_EMAIL
#             recipient_list = [email]

#             send_mail(subject, message, from_email, recipient_list)

#             return redirect('login')  # Create a success page in your templates
#     else:
#         form = UserRegistrationForm()

#     return render(request, 'registration/register.html', {'form': form})


def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = generate_random_password()

            # Save user data to the database using Django User model
            user = User.objects.create_user(username=username, email=email, password=password)

            # Send registration email
            subject = 'Account Created'
            message = f'An account has been created for you. Your username: {username}, email: {email}, Your password is {password}, Please follow this link to login: {settings.BASE_URL}/login/'
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [email]

            send_mail(subject, message, from_email, recipient_list)

            return redirect('login')  # Create a success page in your templates
    else:
        form = UserRegistrationForm()

    return render(request, 'registration/register.html', {'form': form})
