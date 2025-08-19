from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib import auth
from django.urls import reverse
from django.contrib import messages

from users.forms import UserLoginForm, UserRegistrationForm

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                messages.success(request, 'Вы успешно вошли в систему')
                return HttpResponseRedirect(reverse('main:index'))
            
        return render(request, 'users/login.html', {'form': form}) # Если форма не валидна или аутентификация не удалась
    
    form = UserLoginForm() # GET запрос
    return render(request, 'users/login.html', {'form': form})

def registration(request): 
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            return HttpResponseRedirect(reverse('user:login'))
    else:
        form = UserRegistrationForm() # GET запрос

    context = {
        'title': 'Home - Регистрация',
        'form': form,
    }
    return render(request, 'users/registration.html', context)

def profile(request): 
    context = {
        'title': 'Home - Кабинет',
    }
    return render(request, 'users/profile.html', context)

def logout(request): 
    auth.logout(request)
    return redirect(reverse('main:index'))