from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import auth
from django.urls import reverse
from django.contrib import messages

from users.forms import UserLoginForm

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']  # Лучше использовать cleaned_data
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                messages.success(request, 'Вы успешно вошли в систему')
                return HttpResponseRedirect(reverse('main:index'))
        # Если форма не валидна или аутентификация не удалась
        return render(request, 'users/login.html', {'form': form})
    
    # GET запрос
    form = UserLoginForm()
    return render(request, 'users/login.html', {'form': form})

def registration(request): 
    context = {
        'title': 'Home - Регистрация',
    }
    return render(request, 'users/registration.html', context)

def profile(request): 
    context = {
        'title': 'Home - Кабинет',
    }
    return render(request, 'users/profile.html', context)

def logout(request): 
    ...