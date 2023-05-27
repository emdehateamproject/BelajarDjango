from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import FormLogin, FormRegister
from django.contrib.auth.decorators import login_required
from django.conf import settings

from .models import Register

# Create your views here.

def create(request):
    akun_form = FormRegister(request.POST or None)
    if request.method == 'POST':
        if akun_form.is_valid():
            # get model object data from form here
            user = akun_form.save(commit=False)

            # Cleaned(normalized) data
            username = akun_form.cleaned_data['username']
            password = akun_form.cleaned_data['password']

            #  Use set_password here
            user.set_password(password)
            user.save()
            # akun_form.save()
        return redirect('login')
    context = {
        'judul' : 'Register page',
        'akun_form':akun_form,
    }

    return render(request, 'login/register_view.html', context)

def login_view(request):
    form = FormLogin()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'login/login_view.html', {'form':form})

def logout_view(request):
    logout(request)
    request.session.flush()
    return redirect('/login/')
