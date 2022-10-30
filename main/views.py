from django.shortcuts import render, redirect
from django.views.generic import ListView

from .forms import UserForm
from .models import User, Goods, Tattoo, Piercing
from django.contrib import messages
from django.http import HttpResponse



def free_records(request):
    search_query = request.GET.get('q')
    if search_query == None:
        records_pier = Piercing.objects.filter(is_busy_pier=False)
        records_tatt = Tattoo.objects.filter(is_busy_tatt=False)
    else:
        records_pier = Piercing.objects.filter(date__icontains=request.GET.get('q'), is_busy_pier=False)
        records_tatt = Tattoo.objects.filter(date__icontains=request.GET.get('q'), is_busy_tatt=False)

    return render(request, 'main/free_records.html', {'records_tatt': records_tatt, 'records_pier': records_pier})

def index(request):

    search_query = request.GET.get('q')

    if search_query == None:
        records_pier = Piercing.objects.filter(is_busy_pier=False)
        records_tatt = Tattoo.objects.filter(is_busy_tatt=False)
    else:
        records_pier = Piercing.objects.filter(date__icontains=request.GET.get('q'), is_busy_pier=False)
        records_tatt = Tattoo.objects.filter(date__icontains=request.GET.get('q'), is_busy_tatt=False)
    users = User.objects.all()
    return render(request, 'main/index.html', {'title': 'Пирсинг Тату Краснодар', 'users': users, 'records_tatt': records_tatt, 'records_pier': records_pier})

def catalog(request):
    goods = Goods.objects.all()
    return render(request, 'main/catalog.html', {'goods': goods})

def add_user(request):
    error = ''
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Успешная отправка формы! Вы будете перенаправлены на главную страницу!")
            return redirect('home')
        else:
            error = 'Некорректные данные в форме'


    form = UserForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/add_user.html', context)


