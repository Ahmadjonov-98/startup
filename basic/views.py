from django.shortcuts import render, redirect, HttpResponseRedirect
from .forms import CustomUserForm
from django.contrib.auth.models import User, auth
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.models import AbstractUser
from .models import *
from django.db import IntegrityError
# Create your views here.

def home(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        username = request.POST['username']
        email = request.POST['email'] 
        phone = request.POST['phone'] 
        user_type = request.POST['user_type']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            try:
                user = CustomUser.objects.create_user(
                                                        full_name=full_name,
                                                        username=username, 
                                                        phone=phone, 
                                                        password=password1, 
                                                        user_type=user_type,  
                                                        email=email,
                                                        )         
                user.save()
                login(request, user)
            except IntegrityError:
                messages.info(request, "Bunday telefon nomer avval ro`yxatdan o'tgan!")
                registr_form = CustomUserForm()
                return render(request, 'home.html', {'form':registr_form})

        else:
            messages.info(request, "Parollar bir xil emas!")
            return redirect('/')
        
        return redirect('/')
    else:
        registr_form = CustomUserForm()
        return render(request, 'home.html', {'form':registr_form})
