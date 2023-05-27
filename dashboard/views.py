from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings

from .models import dokumen, pegawai
from .forms import DokumenForm
from .functions import handle_uploaded_file
from django.db.models import Count

from django.db import models
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url=settings.LOGIN_URL)
def dashboard(request):
    data_dokumen = dokumen.objects.all()
    count = User.objects.all().count()

    count_emp = pegawai.objects.all().count()
    
    context = {
        'judul':'Dashboard Admin',
        'dokumen':data_dokumen,
        'count_user':count,
        'count_emp':count_emp,
    }
    return render(request, 'dashboard/dashboard.html', context)

@login_required(login_url=settings.LOGIN_URL)
def about(request):
    context = {
        'judul':'About',
    }
    return render(request, 'dashboard/about.html', context)


# save data to database
@login_required(login_url=settings.LOGIN_URL)
def create(request):
    post_form = DokumenForm()

    if request.method == 'POST':
        dokumens = DokumenForm(request.POST, request.FILES)
        if dokumens.is_valid():
            imgf = request.FILES['img_file']
            
            dokumen.objects.create(
                no      = request.POST['no'],
                name    = request.POST['name'],
                activity= request.POST['activity'],
                quantity= request.POST['quantity'],
                img_file = imgf,
            )
            handle_uploaded_file(imgf)
            
            print(request.POST)
            return redirect('master')
    else:
        context = {
            'judul' : 'Create Page',
            'post_form' : post_form,
        }

        return render(request, 'dashboard/create.html',context)

        
# def create(request):
#     if request.method == 'POST':
#         dokumen = DokumenForm(request.POST, request.FILES)
#         if dokumen.is_valid():
#             handle_uploaded_file(request.FILES['file'])
#             model_instance = dokumen.save(commit=False)
#             model_instance.save()
#             return render(request, 'dashboard/dashboard.html')

#     else:
#         dokumen=DokumenForm()
#         context = {
#             'judul':'About Page',
#         }
#         return render(request, 'dashboard/create.html',{'form':dokumen})

@login_required(login_url=settings.LOGIN_URL)
def master(request):
    data_dokumen =dokumen.objects.all()
    context = {
        'judul':'Master Page',
        'dokumen':data_dokumen,
    }
    return render(request, 'dashboard/master.html', context)

@login_required(login_url=settings.LOGIN_URL)
def report(request):
    context = {
        'judul':'Report Page',
    }
    return render(request, 'dashboard/report.html', context)

@login_required(login_url=settings.LOGIN_URL)
def service(request):
    context = {
        'judul':'Service Page',
    }
    return render(request, 'dashboard/service.html', context)

@login_required(login_url=settings.LOGIN_URL)
def setting(request):
    context = {
        'judul':'Setting Page',
    }
    return render(request, 'dashboard/setting.html', context)

def delete(request, delete_id):
    dokumen.objects.filter(id=delete_id).delete()

    return redirect('master')

def update(request, update_id):
    dokumen_update = dokumen.objects.get(id=update_id)
    data = {
        'no'            : dokumen_update.no,
        'name'          : dokumen_update.name,
        'activity'      : dokumen_update.activity,
        'quantity  '    : dokumen_update.quantity,
    }
    dokumen_form = DokumenForm(request.POST or None, initial=data, instance=dokumen_update)

    if request.method == 'POST':
        if dokumen_form.is_valid():
            dokumen_form.save()
            return redirect('master')
    else:
        context = {
            'judul' : 'Create Page',
            'post_form' : dokumen_form,
        }

        return render(request, 'dashboard/create.html',context)
    return redirect('master')
    # print(data)

    # return redirect('master')



def logout_view(request):
    logout(request)
    request.session.flush()
    return redirect('/login/')