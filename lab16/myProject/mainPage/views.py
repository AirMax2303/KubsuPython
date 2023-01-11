from django.shortcuts import render, redirect
from .forms import ShopForm, ManufacturerForm, TechForm
from .models import Tech, Shop, Manufacturer


def index(request):
    tech = Tech.objects.order_by('id')
    return render(request, 'mainPage/index.html', {'tech': tech})


def addShop(request):
    error = ''
    if request.method == 'POST':
        form = ShopForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
        else:
            error = 'Форма неверно заполнена'

    form = ShopForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'mainPage/addShop.html', context)

def addManufacturer(request):
    error = ''
    if request.method == 'POST':
        form = ManufacturerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
        else:
            error = 'Форма неверно заполнена'

    form = ManufacturerForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'mainPage/addManufacturer.html', context)

def addTech(request):
    error = ''
    if request.method == 'POST':
        form = TechForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
        else:
            error = 'Форма введена неверно'

    form = TechForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'mainPage/addTech.html', context)

def showDetails(request, manufacturer_id, model_id, _id):
    man = Manufacturer.objects.get(pk=manufacturer_id)
    shop = Shop.objects.get(pk=model_id)
    tech = Tech.objects.get(pk=_id)
    return render(request, 'mainPage/showDetails.html', {'man': man, 'shop': shop, 'tech': tech})
