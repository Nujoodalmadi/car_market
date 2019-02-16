from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Car
from .forms import CarForm

def car_list(request):
    cars = Car.objects.all()
    context = {
        "cars": cars,
    }
    return render(request, 'car_list.html', context)


def car_detail(request, car_id):
    car = Car.objects.get(id=car_id)
    context = {
        "car": car,
    }
    return render(request, 'car_detail.html', context)


def car_create(request):
    form = CarForm()
    if request.method == "POST": 
        form = CarForm(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'car created')
            return redirect('car-list')

    context = {
        "form": form,
    }
    return render(request, 'create.html', context)
    

def car_update(request, car_id):
    car_obj = Car.objects.get(id=car_id)
    form = CarForm(instance=car_obj)
    if request.method == "POST" : 
        form = CarForm(request.POST, request.FILES or None, instance=car_obj)
        if form.is_valid():
            form.save()
            messages.info(request, 'updated')
            return redirect('car-list')
    
    context = {
        "car_obj": car_obj,
        "form": form,
    }
    return render(request, 'update.html', context)




def car_delete(request, car_id):
    car_obj = Car.objects.get(id=car_id)
    car_obj.delete()
    messages.warning(request, 'deleted')
    return redirect('car-list')






